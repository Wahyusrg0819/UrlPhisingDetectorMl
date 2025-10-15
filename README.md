# Phishing URL Detector

Aplikasi web untuk mendeteksi URL phishing menggunakan analisis fitur lexical dengan Machine Learning.

## Teknologi

- **Frontend**: Next.js 14 + TypeScript
- **Backend**: Django REST Framework
- **Model**: Scikit-learn Random Forest Classifier (100 trees)
- **Model File**: RandomForest_phishing_model.pkl

## Fitur Lexical yang Dianalisis

Model mengekstrak 7 fitur lexical dari URL (identik dengan training):

1. **url_length**: Panjang total URL
2. **num_dots**: Jumlah karakter titik (.)
3. **has_www**: Keberadaan substring "www" (case-sensitive)
4. **has_https**: Keberadaan substring "https" 
5. **num_hyphens**: Jumlah karakter hyphen (-)
6. **num_slashes**: Jumlah karakter slash (/)
7. **has_numeric**: Keberadaan angka (regex: \d)

## Instalasi & Menjalankan

### Backend (Django)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Backend akan berjalan di `http://localhost:8000`

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

Frontend akan berjalan di `http://localhost:3000`

## Training Model

Model dilatih menggunakan dataset `malicious_phish.csv` dengan:
- **Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Train/Test Split**: 80/20
- **Random State**: 42
- **Model File**: `RandomForest_phishing_model.pkl`

**Catatan**: Model ini menggunakan 7 fitur leksikal sederhana. Untuk production, disarankan menambah fitur tambahan seperti domain age, SSL certificate, dan content-based features untuk meningkatkan akurasi.

## Cara Penggunaan

1. Buka browser dan akses `http://localhost:3000`
2. Masukkan URL yang ingin dianalisis
3. Klik tombol "Analisis"
4. Lihat hasil prediksi dan probabilitas untuk setiap kategori

## Kategori Prediksi

- **benign**: URL aman/legitimate
- **phishing**: URL phishing
- **malware**: URL mengandung malware
- **defacement**: URL defacement
- **defaceme**: URL defacement (variant)

## API Endpoint

### POST /api/predict/

Request:
```json
{
  "url": "https://example.com"
}
```

Response:
```json
{
  "url": "https://example.com",
  "prediction": "benign",
  "probabilities": {
    "benign": 0.95,
    "phishing": 0.03,
    "malware": 0.01,
    "defacement": 0.005,
    "defaceme": 0.005
  },
  "features": {
    "url_length": 19,
    "num_dots": 1,
    "has_www": false,
    "has_https": true,
    "num_hyphens": 0,
    "num_slashes": 2,
    "has_numeric": false
  }
}
```
