# Random Forest Model Information

## Model Details

- **File**: `RandomForest_phishing_model.pkl`
- **Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Framework**: Scikit-learn 1.6.1
- **Training Date**: 2024

## Classes

Model dapat mengklasifikasikan URL ke dalam 4 kategori:

1. **benign** - URL legitimate/aman
2. **phishing** - URL phishing
3. **malware** - URL mengandung malware
4. **defacement** - URL defacement

## Features (7 Fitur Leksikal)

Model menggunakan 7 fitur yang diekstrak dari URL:

| No | Feature Name | Description | Type | Example |
|----|--------------|-------------|------|---------|
| 1 | url_length | Panjang total URL | Integer | 45 |
| 2 | num_dots | Jumlah karakter titik (.) | Integer | 2 |
| 3 | has_www | Keberadaan substring "www" | Binary (0/1) | 1 |
| 4 | has_https | Keberadaan substring "https" | Binary (0/1) | 1 |
| 5 | num_hyphens | Jumlah karakter hyphen (-) | Integer | 0 |
| 6 | num_slashes | Jumlah karakter slash (/) | Integer | 3 |
| 7 | has_numeric | Keberadaan angka | Binary (0/1) | 0 |

## Feature Importance

Berdasarkan model Random Forest:

```
num_slashes    : 28.53%  (paling penting)
has_www        : 22.50%
url_length     : 22.31%
num_dots       : 14.53%
num_hyphens    :  5.86%
has_https      :  4.09%
has_numeric    :  2.18%
```

## Model Performance

### Training Dataset
- **Source**: Malicious Phish Dataset
- **Total Samples**: 10,000+ URLs
- **Split**: 80% training, 20% testing
- **Random State**: 42

### Limitations

⚠️ **Catatan Penting**: Model ini memiliki keterbatasan karena:

1. **Fitur Terbatas**: Hanya menggunakan 7 fitur leksikal sederhana
2. **False Positive**: Cenderung memprediksi URL benign sebagai phishing
3. **False Negative**: Beberapa URL phishing diprediksi sebagai benign
4. **Generalization**: Performa pada real-world URLs mungkin berbeda dari training data

### Recommended Improvements

Untuk meningkatkan akurasi model:

1. **Tambah Fitur**:
   - Domain age (umur domain)
   - SSL certificate validity
   - WHOIS information
   - Page rank
   - Content-based features (HTML, JavaScript)
   - Blacklist checking

2. **Dataset**:
   - Gunakan dataset lebih besar dan balanced
   - Include more recent phishing samples
   - Regular model retraining

3. **Algorithm**:
   - Experiment dengan XGBoost, LightGBM
   - Deep Learning (LSTM, CNN)
   - Ensemble methods

## Usage in Application

### Backend (Django)

```python
import joblib
from detector.feature_extractor import extract_features

# Load model
model = joblib.load('RandomForest_phishing_model.pkl')

# Predict
url = "https://example.com"
features = extract_features(url)
prediction = model.predict([features])[0]
probabilities = model.predict_proba([features])[0]
```

### API Response

```json
{
  "url": "https://example.com",
  "prediction": "benign",
  "confidence": 0.892,
  "probabilities": {
    "benign": 0.892,
    "phishing": 0.054,
    "malware": 0.032,
    "defacement": 0.022
  },
  "features": {
    "url_length": 19,
    "num_dots": 1,
    "has_www": false,
    "has_https": true,
    "num_hyphens": 0,
    "num_slashes": 2,
    "has_numeric": false
  },
  "model_info": {
    "algorithm": "Random Forest",
    "n_estimators": 100,
    "classes": ["benign", "defacement", "malware", "phishing"]
  }
}
```

## Model Versioning

| Version | Date | Changes | File |
|---------|------|---------|------|
| 1.0 | 2024 | Initial Random Forest model | RandomForest_phishing_model.pkl |

## Future Work

- [ ] Retrain dengan dataset lebih besar
- [ ] Tambah fitur domain-based dan content-based
- [ ] Implement model monitoring dan retraining pipeline
- [ ] A/B testing dengan algoritma lain
- [ ] Deploy model dengan versioning (MLflow)

## References

- Scikit-learn Random Forest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- Phishing Detection Research: Various academic papers on URL-based phishing detection
