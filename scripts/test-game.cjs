const { chromium } = require('playwright');
const fs = require('node:fs');
const http = require('node:http');
const assert = require('node:assert/strict');
(async () => {
  const html=fs.readFileSync('assets/game.html','utf8');
  const levels=JSON.parse(html.match(/const LEVELS=(\[[^;]+\]);\s*const COLORS=/)[1]);
  const out='build/store-assets'; fs.mkdirSync(out,{recursive:true});
  const server=http.createServer((req,res)=>{res.setHeader('Content-Type','text/html; charset=utf-8');res.end(html)});
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const browser=await chromium.launch();
  const page=await browser.newPage({viewport:{width:540,height:960},deviceScaleFactor:2});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  try {
    await page.goto('http://127.0.0.1:'+server.address().port);
    await page.locator('#board .cell').first().waitFor();
    await page.screenshot({path:out+'/01-oyun.png'});
    await page.locator('#hint').click();
    assert.equal(await page.locator('.cell.preview').count(),1,'Hint missing');
    const first=levels[0].paths[0][0];
    await page.locator('.cell[data-r="'+first[0]+'"][data-c="'+first[1]+'"]').click({force:true});
    await page.locator('#undo').click();
    assert.equal(await page.locator('#moves').innerText(),'0','Undo failed');
    await page.locator('#restart').click();
    const results=[];
    for(let i=0;i<levels.length;i++){
      assert.equal(await page.locator('#levelNo').innerText(),(i+1)+'/10');
      if(i===6) await page.screenshot({path:out+'/03-usta-bolum.png'});
      for(let g=0;g<levels[i].paths.length;g++){
        for(const [r,c] of levels[i].paths[g]){
          await page.locator('.cell[data-r="'+r+'"][data-c="'+c+'"]').click({force:true});
        }
        if(i===0 && g===0) {
          await page.waitForTimeout(1800);
          await page.screenshot({path:out+'/02-baglanti.png'});
        }
      }
      assert.equal(await page.locator('#victory').isVisible(),true,'Level '+(i+1)+' did not finish');
      results.push({level:i+1,solved:true,moves:Number(await page.locator('#moves').innerText())});
      if(i<levels.length-1) await page.locator('#next').click();
    }
    assert.deepEqual(errors,[],'Browser errors');
    await page.reload();
    assert.equal(await page.locator('#levelrow button:disabled').count(),0,'Progress was not saved');
    fs.writeFileSync(out+'/gameplay-test.json',JSON.stringify({levels:results,hint:true,undo:true,restart:true,persistence:true,errors},null,2));
    console.log('PASS: all 10 levels solved by pointer input; hints, undo, restart and persistence verified.');
  } finally {await browser.close(); server.close();}
})().catch(e=>{console.error(e);process.exit(1)});
