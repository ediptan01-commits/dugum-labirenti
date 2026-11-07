# Blok Birleştirme — Google Play kapalı test hazırlığı

## Mağaza metinleri

**Uygulama adı:** Blok Birleştirme

**Kısa açıklama (80 karakteri aşmaz):**
Numaralı blokları bağla, engelleri aş ve enerji zincirini tamamla!

**Tam açıklama:**

Blok Birleştirme, renkli enerji yollarını doğru sırayla birleştirdiğin bir mantık ve bulmaca oyunudur.

Aynı numaralı BAŞLA ve HEDEF bloklarını birbirine bağla. Her bağlantıda engelleri aş, enerji kristallerinden geç ve yolların kesişmesine izin verme. Bir hattı tamamladığında sonraki bağlantı etkinleşir.

- 10 oynanabilir bölüm
- Renkli bağlantılar, engeller ve enerji kristalleri
- Hamle geri alma, yenileme ve ipucu
- Puan kazanma ve ilerleme kaydı
- Çevrimdışı oynanış

Doğru rotayı keşfet, bağlantıları sırayla tamamla ve zincir reaksiyonunu başlat!

## Kapalı test sürümü

- **Görünen ad:** Blok Birleştirme
- **Paket adı:** `com.teknolojix.dugum_labirenti` — mevcut build yapılandırmasından; Play Console'da ilk yüklemede kontrol et.
- **Sürüm:** `1.0.0+1`
- **Yükleme dosyası:** GitHub Actions'taki `Blok-Birlestirme-PLAY-SIGNED-AAB` artifact içindeki `app-release.aab`.
- **Telefon testi:** `Blok-Birlestirme-SIGNED-APK` artifact içindeki `app-release.apk`.
- **İmzalama:** Play upload anahtarıyla imzalı olmalı; GitHub release doğrulama raporunu kontrol et.
- **Oyun ikonu:** Beş Android yoğunluğunda paketlenmiş; mağaza için `Blok-Birlestirme-RELEASE-VERIFICATION` artifact içindeki 512×512 PNG mevcut.

## Play Console yapılacaklar

1. Uygulamayı **Oyun** türünde, Türkçe, **Blok Birleştirme** adıyla aç.
2. Gizlilik politikası için **herkese açık HTTPS bağlantısı** ekle. Kaynak dosyası `docs/index.html`; GitHub Pages dağıtımı ve erişilebilirlik doğrulanmadan URL'yi Play Console'a yazma.
3. Veri güvenliği formunu uygulamanın gerçek davranışına göre yanıtla. Çevrimdışı WebView oyunu; hesap, reklam, analitik ve sunucu trafiği eklenip eklenmediğini yeniden kontrol et.
4. İçerik derecelendirmesi, hedef kitle, reklam beyanı, uygulama erişimi, ülke/bölge ve iletişim bilgilerini tamamla.
5. 512×512 uygulama simgesi, 1024×500 özellik grafiği ve en az iki **gerçek oyun ekran görüntüsü** yükle. Önceki temsili/üretilmiş görselleri gerçek ekran görüntüsü olarak kullanma.
6. **Kapalı test** sürümüne imzalı AAB'yi yükle. İlk yüklemede Google Play App Signing yönergelerini takip et.
7. Test kullanıcılarını ekle ve katılım bağlantısını paylaş. Hesabın 12 test kullanıcısı/14 gün koşuluna tabiyse Play Console'daki şartları tamamla.
8. Kapalı test cihazlarında kurulum, 10 bölüm, kayıt, geri alma, yeniden başlatma, ipucu, ses ve ekran uyumunu denetle.

## Güvenlik

`.jks`, şifreler ve Base64 içeriği **GitHub deposuna, Actions artifact'larına veya mağaza sayfasına eklenmemelidir**. Güvenli yedek korunmalı. Yeni yayınlarda aynı upload key kullanılmalı.

## İlgili yollar

- [Android Actions](https://github.com/ediptan01-commits/dugum-labirenti/actions)
- [Gizlilik politikası kaynak dosyası](https://github.com/ediptan01-commits/dugum-labirenti/blob/main/docs/index.html)
