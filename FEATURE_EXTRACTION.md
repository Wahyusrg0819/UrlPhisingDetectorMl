# Feature Extraction Documentation

## Model: Random Forest Classifier (100 trees)

File: `RandomForest_phishing_model.pkl`

## Konsistensi dengan Training Code

Feature extraction di backend **100% identik** dengan training code untuk memastikan prediksi akurat.

## Implementasi Fitur

### 1. url_length
```python
len(url)
```
Menghitung total karakter dalam URL.

### 2. num_dots
```python
url.count('.')
```
Menghitung jumlah karakter titik.

### 3. has_www
```python
1 if 'www' in url else 0
```
**PENTING**: Case-sensitive, mencari substring "www" dalam URL.

### 4. has_https
```python
1 if 'https' in url else 0
```
**PENTING**: Substring match, bukan parsing scheme. Akan match "https" di mana saja dalam URL.

### 5. num_hyphens
```python
url.count('-')
```
Menghitung jumlah karakter hyphen.

### 6. num_slashes
```python
url.count('/')
```
Menghitung jumlah karakter slash.

### 7. has_numeric
```python
1 if bool(re.search(r'\d', url)) else 0
```
Menggunakan regex untuk mendeteksi keberadaan angka.

## Contoh Ekstraksi

### URL: `https://www.google.com/search?q=test123`

```python
{
    'url_length': 40,
    'num_dots': 2,
    'has_www': 1,        # 'www' ditemukan
    'has_https': 1,      # 'https' ditemukan
    'num_hyphens': 0,
    'num_slashes': 2,
    'has_numeric': 1     # '123' ditemukan
}
```

### URL: `http://suspicious-site.tk/login.php`

```python
{
    'url_length': 37,
    'num_dots': 2,
    'has_www': 0,        # tidak ada 'www'
    'has_https': 0,      # tidak ada 'https'
    'num_hyphens': 1,
    'num_slashes': 2,
    'has_numeric': 0     # tidak ada angka
}
```

## Catatan Penting

1. **Case Sensitivity**: `has_www` adalah case-sensitive sesuai training
2. **Substring Match**: `has_https` mencari substring, bukan parsing URL scheme
3. **Order Matters**: Urutan fitur dalam array harus sesuai dengan training:
   ```python
   [url_length, num_dots, has_www, has_https, num_hyphens, num_slashes, has_numeric]
   ```

## Validasi

Untuk memastikan konsistensi, test dengan URL yang sama di training dan production harus menghasilkan fitur yang identik.
