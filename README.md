# Düğüm Labirenti NEXUS

Orijinal tam ekran oyunu koruyan Android (Flutter WebView) sürümü.

## İçerik
- `assets/game.html`: 10 bölümlü, beyaz numaralı bloklu orijinal oyun
- `lib/main.dart`: çevrimdışı Flutter Android WebView kabuğu
- `.github/workflows/android.yml`: GitHub Actions APK/AAB derlemesi

## Android derleme
GitHub > Actions > **Düğüm Labirenti Android APK ve AAB** > en güncel başarılı çalışma > Artifacts içinden APK ve AAB dosyalarını indir.

İlk kurulumda Actions, Android platform dosyalarını `flutter create` ile üretir.

## Play Store uyarısı
CI'ın ürettiği AAB, Play Store için uygun **özel upload keystore ile imzalanmış dağıtım paketi değildir**. Google Play'e üretim yüklemesi öncesinde upload anahtarı, signing config, kalıcı uygulama kimliği, simge, gizlilik politikası ve cihaz testleri tamamlanmalıdır. CI'ın ilk amacı derleme doğrulama ve test APK'sı üretimidir.
