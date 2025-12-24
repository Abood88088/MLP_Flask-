# 🚗 Araba Fiyat Tahmini – BLG407 Projesi  

**Ders:** BLG407 Makine Öğrenmesi  
**Öğrenci:** ABDUL RAHMAN KHANOUM (No: 2212721317)  
**GitHub Repo:** [MLP_Flask-](https://github.com/Abood88088/MLP_Flask-)  

---

## 🎯 Proje Amacı  
Bu proje, **çoklu doğrusal regresyon (MLR)** yöntemini kullanarak **ikinci el araç fiyatlarını tahmin etmeyi** hedefler.  
Model, araç yaşı, motor hacmi, kilometre, beygir gücü ve marka gibi bağımsız değişkenleri kullanarak fiyat tahmini yapar.  

---

## 🔑 Metodoloji  

- **Veri Hazırlığı:** Gerçekçi ve tutarlı değerlerden oluşan veri seti oluşturuldu.  
- **EDA (Keşifsel Veri Analizi):** Eksik ve anlamsız değişkenler incelendi.  
- **Modelleme:**  
  - OLS (Ordinary Least Squares) yöntemi kullanıldı.  
  - p-value analizleri ile anlamsız değişkenler çıkarıldı.  
- **Performans Ölçümü:**  
  - R², MAE, MSE metrikleri hesaplandı.  
  - Gerçek vs Tahmin grafikleri ile görselleştirme yapıldı.  
- **Model Kaydı:** Eğitilen model `.pkl` dosyası olarak kaydedildi.  
- **Flask GUI:** Kullanıcı dostu web arayüzü geliştirildi.  

---

## 📊 Model Başarımı  

- **R² Skoru:** `0.9397` → Model fiyat varyasyonunun %94’ünü açıklıyor.  
- **MAE:** `22,571.98` → Ortalama hata seviyesi.  
- **MSE:** `1,177,751,557.55` → Büyük hataların sınırlı olduğunu gösteriyor.  

---

Harika! İki ekran görüntüsünü README dosyana entegre edecek şekilde aşağıdaki bölümü hazırladım. Markdown formatında, görsel açıklamalarıyla birlikte modern ve düzenli bir yapı sunuyor:

---

## 🖼️ Uygulama Arayüzü  

Aşağıda, Flask tabanlı web arayüzün nasıl çalıştığını gösteren iki örnek ekran görüntüsü yer almaktadır. Kullanıcı, araç bilgilerini girerek tahmini fiyatı anlık olarak görebilmektedir.

### 🔧 Örnek 1 – BMW (2020 Model)  
Kullanıcı aşağıdaki bilgileri girmiştir:  
- Yıl: 2020  
- Motor Hacmi: 3.0 L  
- Kilometre: 40,000 km  
- Beygir Gücü: 300 HP  
- Marka: BMW  

Tahmin edilen fiyat: **💰 927,791 TL**

![BMW Tahmin Ekranı](./attachments/HxyMxUfzhkL5GSvjPYy3g.png)

---

### 🔧 Örnek 2 – Mercedes (2021 Model)  
Kullanıcı aşağıdaki bilgileri girmiştir:  
- Yıl: 2021  
- Motor Hacmi: 2.0 L  
- Kilometre: 30,000 km  
- Beygir Gücü: 190 HP  
- Marka: Mercedes  

Tahmin edilen fiyat: **💰 824,249 TL**

![Mercedes Tahmin Ekranı](./attachments/J9vngqMmYjBRUeDB1UPVE.png)

---
## 🖥️ Uygulama Kullanımı  

### 1️⃣ Gerekli Kütüphaneler  
```bash
pip install flask pandas scikit-learn numpy statsmodels
```

### 2️⃣ Uygulamayı Çalıştır  
```bash
python app.py
```

### 3️⃣ Tarayıcıdan Aç  
```bash
http://127.0.0.1:5000
```

---


## 🎨 Arayüz Özellikleri  

- Modern tasarım: **HTML, CSS, Bootstrap, JavaScript**  
- Kullanıcı dostu form yapısı  
- Form verilerinin gönderim sonrası korunması  
- Anlık tahmin sonucu görüntüleme  

---

## 👨‍💻 Geliştirici Bilgileri  

- **Ad Soyad:** ABDUL RAHMAN KHANOUM  
- **Öğrenci No:** 2212721317  
- **Ders:** BLG407 – Makine Öğrenmesi  
- **Öğretim Üyesi:** Doç. Dr. Sinan Uğuz  

---


