# Düğüm Labirenti NEXUS 2.0

10 bölümlü Android Flutter/WebView bulmaca oyunu. Tek parça kanallar, beyaz numaralı bloklar, kristaller, enerji kapıları, ses efektleri ve ilerleme kaydı.

## GitHub Actions

[Android derlemeleri](https://github.com/ediptan01-commits/dugum-labirenti/actions)

- **Dugum-Labirenti-TEST-APK**: test için; Play Store'a yüklenmez.
- **Dugum-Labirenti-PLAY-SIGNED-AAB**: yalnızca gerçek ve özel bir upload key tanımlandıysa oluşturulur.
- **Dugum-Labirenti-SIGNED-APK**: aynı özel anahtarla imzalanan dağıtım APK'sı.

## İlk Google Play yükleme imzası

Google Play App Signing kullan. Play Console'da yeni uygulama oluşturduktan sonra yükleme anahtarını güvenli bir yerde sakla.

Kendi bilgisayarında, kimseyle paylaşmayacağın bir klasörde örnek komut:

```sh
keytool -genkeypair -v -keystore upload-keystore.jks -storetype JKS -keyalg RSA -keysize 3072 -validity 10000 -alias upload
```

Oluşan **upload-keystore.jks** dosyasını ve parolaları yedekle. **Depoya, sohbet mesajına veya herkese açık bir dosya paylaşımına ekleme.**

Keystore dosyasını tek satırlık base64'e çevir:

- macOS/Linux: `base64 -w 0 upload-keystore.jks` (macOS'ta `base64 < upload-keystore.jks | tr -d '\\n'`)
- Windows PowerShell: `[Convert]::ToBase64String([IO.File]::ReadAllBytes("upload-keystore.jks"))`

GitHub deposunda **Settings → Secrets and variables → Actions → New repository secret** yoluyla şu dört sırrı oluştur:

1. `PLAY_UPLOAD_KEYSTORE_BASE64` — keystore dosyasının base64 içeriği.
2. `PLAY_STORE_PASSWORD` — keystore parolası.
3. `PLAY_KEY_PASSWORD` — `upload` anahtarının parolası.
4. `PLAY_KEY_ALIAS` — `upload`.

Sırları ekledikten sonra Actions bölümünden workflow'u yeniden çalıştır. Başarılı çalışmada **Dugum-Labirenti-PLAY-SIGNED-AAB** indir. Workflow `jarsigner -verify` ile AAB imzasını da doğrular.

## Kimlik ve sürüm

- Uygulama kimliği: `com.teknolojix.dugum_labirenti` (Flutter'ın `--org com.teknolojix` + proje adı sonucu)
- Sürüm: `1.0.0+1`
- Google Play'e ilk kayıt öncesinde kimliği kesinleştir. İlk yüklemeden sonra kimlik değiştirilemez.
- İlk AAB yüklemesi için Play Console'da `Yeni uygulama oluştur` ekranını tamamla.

## Önemli

Secrets tanımlanmadan oluşturulan test APK Play Store'a uygun AAB yerine geçmez. İş akışı bilinçli olarak secrets yokken Play AAB üretmez. Uygulama ikonunu, veri güvenliği beyanını, mağaza görsellerini ve testleri ayrıca tamamla.
