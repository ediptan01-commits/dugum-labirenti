const fs = require('node:fs');
const assert = require('node:assert/strict');
const html = fs.readFileSync('assets/game.html','utf8');
const m = html.match(/const LEVELS=(\[[^;]+\]);\s*const COLORS=/);
assert(m, 'LEVELS data not found');
const levels = JSON.parse(m[1]);
assert.equal(levels.length, 10, 'Exactly 10 levels required');
for (let i=0;i<levels.length;i++) {
  const l=levels[i];
  assert(l.n>=7 && l.n<=9);
  assert.equal(l.paths.length,l.checkpoints.length);
  const occupied=new Set();
  for(let g=0;g<l.paths.length;g++){
    const route=l.paths[g]; assert(route.length>=2);
    for(let j=0;j<route.length;j++){
      const p=route[j],k=p.join(',');
      assert(p[0]>=0&&p[0]<l.n&&p[1]>=0&&p[1]<l.n);
      assert(!occupied.has(k), 'route overlap '+(i+1)+':'+k);
      occupied.add(k);
      if(j>0) assert.equal(Math.abs(p[0]-route[j-1][0])+Math.abs(p[1]-route[j-1][1]),1,'route disconnected');
    }
    for(const cp of l.checkpoints[g]) assert(route.some(p=>p[0]===cp[0]&&p[1]===cp[1]),'crystal not on route');
  }
  for(const p of l.walls) assert(!occupied.has(p.join(',')),'wall blocks solution');
  for(const gate of l.gates||[]) {
    assert(gate.after>=0 && gate.after<l.paths.length-1,'gate trigger invalid');
    assert(occupied.has(gate.at.join(',')),'gate not on route');
  }
}
console.log('OK: 10 levels, route connectivity, walls, crystals and gates.');
