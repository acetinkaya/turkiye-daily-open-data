# 🇹🇷 Türkiye Daily Open Data

**Türkiye'ye özgü verilerin otomatik olarak toplandığı, her gün güncellenen ve yapay zekâ / makine öğrenmesi / zaman serisi araştırmalarında kullanılmak üzere hazırlanan açık veri deposu.**

---

## 📌 Proje Hakkında

`turkiye-daily-open-data`, Türkiye kaynaklı verileri **tamamen otomatik** biçimde günlük olarak toplayan, arşivleyen ve analiz edilebilir hâle getiren bir açık veri projesidir. Depo, GitHub Actions üzerinde çalışan zamanlanmış (scheduled) iş akışları sayesinde insan müdahalesi olmadan her gün yeni veri kaydı ekler; böylece zaman içinde organik olarak büyüyen, gerçek dünya kaynaklı bir zaman serisi veri kümesi oluşur.

Proje, kişisel akademik araştırma ihtiyacından doğmuştur: yapay zekâ ve makine öğrenmesi tabanlı tahmin (forecasting) modellerini gerçekçi, sürekli büyüyen ve Türkiye bağlamına özgü bir veri kümesi üzerinde test edebilmek için hazır, güncel ve düzenli aralıklarla büyüyen Türkiye kaynaklı günlük veri seti bulmak oldukça zordur. Bu depo tam olarak bu boşluğu doldurmak amacıyla geliştirilmiş; zaman içinde kapsamı genişletilecek bir altyapı olarak tasarlanmıştır.

## 🎯 Kapsam

### Şu an depoda bulunanlar
- **Hava durumu verileri** — [OpenWeatherMap](https://openweathermap.org/api) API'si üzerinden günlük olarak çekilir ve `data/weather/` klasörü altında arşivlenir.
- **Otomatik görselleştirme / raporlama** — Toplanan veriler `matplotlib` ile işlenerek `reports/` klasörü altında grafik ve özet raporlar hâline getirilir.
- **Uçtan uca otomasyon** — `.github/workflows/` altındaki GitHub Actions tanımları sayesinde tüm süreç (veri çekme → işleme → raporlama → commit) günlük olarak, insan müdahalesi olmadan çalışır.

### 🗺️ Yol Haritası (Planlanan Genişleme)
Deponun adının da işaret ettiği gibi nihai hedef yalnızca hava durumuyla sınırlı değildir. Zaman içinde Türkiye'ye dair başka açık veri kategorilerinin de eklenmesi planlanmaktadır. Örnek olabilecek başlıklar:
- Döviz kurları / finansal göstergeler
- Enflasyon ve TÜİK bazlı ekonomik göstergeler
- Hava kalitesi ve çevresel veriler
- Deprem/afet verileri

> *Not: Yol haritası maddeleri örnek niteliğindedir — eklenecek gerçek veri setlerine karar verdikçe bu bölümü güncellemen yeterli.*

## 🗂️ Depo Yapısı

```
turkiye-daily-open-data/
├── .github/
│   └── workflows/       # Günlük otomasyonu tetikleyen GitHub Actions iş akışları
├── data/
│   └── weather/          # OpenWeatherMap'ten çekilen günlük ham/işlenmiş hava durumu verileri
├── reports/               # Otomatik üretilen grafik ve özet raporlar
├── scripts/               # Veri çekme, işleme ve raporlama işlemlerini yürüten Python betikleri
├── .gitignore
├── LICENSE                # CC BY 4.0
└── README.md
```

## ⚙️ Nasıl Çalışır?

1. **Zamanlama:** `.github/workflows/` içindeki GitHub Actions iş akışı, günlük olarak otomatik tetiklenir (cron tabanlı zamanlama).
2. **Veri Çekme:** `scripts/` altındaki Python betikleri, OpenWeatherMap API'sine istek atarak güncel hava durumu verisini alır.
3. **Arşivleme:** Alınan veri `data/weather/` klasörüne düzenli (tarih temelli) biçimde kaydedilir.
4. **Raporlama:** Veriler `matplotlib` kullanılarak görselleştirilir ve `reports/` klasörüne yeni bir rapor/grafik eklenir.
5. **Otomatik Commit:** Süreç sonunda değişiklikler otomatik olarak depoya commit edilir — bu sayede depo geçmişi başlı başına bir zaman çizelgesi hâline gelir.

## 🚀 Yerel Kurulum

Depoyu kendi bilgisayarınızda çalıştırmak ya da betikleri incelemek isterseniz:

```bash
git clone https://github.com/acetinkaya/turkiye-daily-open-data.git
cd turkiye-daily-open-data
pip install requests pandas matplotlib   # scripts/ altındaki olası bağımlılıklar; varsa requirements.txt dosyasını tercih edin
```

OpenWeatherMap API'sini kullanabilmek için kendi API anahtarınızı bir ortam değişkeni (ör. `OPENWEATHERMAP_API_KEY`) veya GitHub Actions "Secrets" olarak tanımlamanız gerekir.

> Normal kullanımda betikleri elle çalıştırmanıza gerek yoktur; tüm süreç GitHub Actions ile otomatik yürütülür. Bu adımlar yalnızca yerelde geliştirme/test yapmak isteyenler içindir.

## 📊 Kullanım Alanları

Bu veri seti özellikle şu amaçlarla kullanılabilir:
- Zaman serisi tahmin (forecasting) modellerinin eğitilmesi ve test edilmesi
- Makine öğrenmesi / derin öğrenme algoritmalarının gerçek ve sürekli büyüyen bir veri kümesi üzerinde denenmesi
- Hava durumu trendlerinin ve mevsimsel örüntülerin analizi
- Akademik çalışmalar, tez/proje çalışmaları ve ders materyali için referans veri kaynağı

## 🧾 Veri Kaynağı ve Atıf

Hava durumu verileri [OpenWeatherMap](https://openweathermap.org/) servisinden alınmaktadır. Bu veriyi kullanan çalışmalarda OpenWeatherMap'e atıf yapılması önerilir.

## 📄 Lisans

Bu proje [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) lisansı ile lisanslanmıştır. Depodaki veri ve içerikleri, kaynağa atıf yapmak kaydıyla özgürce kullanabilir, paylaşabilir ve uyarlayabilirsiniz.

Telif hakkı © 2026 Ali Çetinkaya

## 👤 Yazar

**Ali Çetinkaya**

Yapay zekâ, algoritma tasarımı ve otonom sistemler alanlarında çalışan akademisyen ve araştırmacı. Çalışma alanları arasında yapay zekâ ve makine öğrenmesi, derin öğrenme ve bulanık mantık sistem tasarımı, algoritma geliştirme ve optimizasyon, robotik ve otonom sistemler, gömülü sistemler ve akıllı mühendislik uygulamaları yer almaktadır.

- 🔗 GitHub: [@acetinkaya](https://github.com/acetinkaya)
- 🎓 Google Scholar: [Ali Çetinkaya](https://scholar.google.com/citations?user=GXJajLgAAAAJ)

> 🚀 *"Bilgiyi oluşturalım, yayalım, koruyalım ve birlikte geliştirelim!"* — Öğr. Gör. Ali Çetinkaya 2025

## 🤝 Katkıda Bulunma

Öneri, hata bildirimi veya yeni veri kaynağı fikirleri için issue açabilir ya da pull request gönderebilirsiniz.

---

⭐ Projeyi faydalı bulduysanız yıldızlamayı unutmayın!
