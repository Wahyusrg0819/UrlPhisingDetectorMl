# Large Files - Download Instructions

File-file besar tidak di-commit ke Git karena melebihi limit GitHub (100MB).

## 📦 File yang Perlu Didownload

### 1. **Model Files** (360MB+)
- `phishing_model.pkl` - Random Forest model (trained)
- `RandomForest_phishing_model.pkl` - Alternative model name

**Download dari:**
- Google Drive: [Link akan ditambahkan]
- Dropbox: [Link akan ditambahkan]

**Letakkan di:** Root folder project

### 2. **Dataset** (85MB+)
- `malicious_phish.csv` - Training dataset (651,191 URLs)

**Download dari:**
- Kaggle: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
- Google Drive: [Link akan ditambahkan]

**Letakkan di:** Root folder project

### 3. **PlantUML JAR** (10MB+)
- `plantuml.jar` - Untuk compile diagram

**Download dari:**
- Official: https://plantuml.com/download
- Direct: https://github.com/plantuml/plantuml/releases/latest

**Letakkan di:** `proposal/diagrams/` folder

---

## 🚀 Quick Setup

```bash
# 1. Clone repository
git clone https://github.com/Wahyusrg0819/UrlPhisingDetectorMl.git
cd UrlPhisingDetectorMl

# 2. Download file besar (manual)
# - Download phishing_model.pkl → letakkan di root
# - Download malicious_phish.csv → letakkan di root
# - Download plantuml.jar → letakkan di proposal/diagrams/

# 3. Verify files
ls -lh phishing_model.pkl
ls -lh malicious_phish.csv
ls -lh proposal/diagrams/plantuml.jar

# 4. Install dependencies
cd backend
pip install -r requirements.txt

cd ../frontend
npm install

# 5. Run application
# Backend: python backend/manage.py runserver
# Frontend: npm run dev (di folder frontend)
```

---

## 📊 File Sizes

| File | Size | Required For |
|------|------|--------------|
| phishing_model.pkl | ~360 MB | Backend prediction |
| malicious_phish.csv | ~85 MB | Model training/testing |
| plantuml.jar | ~10 MB | Diagram generation |

---

## 💡 Alternative: Git LFS

Jika ingin menggunakan Git LFS untuk file besar:

```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.pkl"
git lfs track "*.csv"
git lfs track "plantuml.jar"

# Add .gitattributes
git add .gitattributes
git commit -m "Add Git LFS tracking"

# Add large files
git add phishing_model.pkl malicious_phish.csv
git commit -m "Add large files with LFS"
git push
```

---

## ⚠️ Important Notes

1. **Jangan commit file besar** langsung ke Git (akan error)
2. **File sudah di .gitignore** untuk mencegah accident commit
3. **Download manual** dari link yang disediakan
4. **Atau gunakan Git LFS** untuk manajemen file besar

---

## 📝 Checklist Setup

- [ ] Clone repository
- [ ] Download phishing_model.pkl
- [ ] Download malicious_phish.csv
- [ ] Download plantuml.jar (optional, untuk diagram)
- [ ] Install backend dependencies
- [ ] Install frontend dependencies
- [ ] Run backend server
- [ ] Run frontend server
- [ ] Test aplikasi

---

## 🆘 Troubleshooting

### Error: "Model not found"
- Pastikan `phishing_model.pkl` ada di root folder
- Check path di `backend/detector/views.py`

### Error: "Dataset not found"
- Pastikan `malicious_phish.csv` ada di root folder
- Hanya diperlukan untuk training/testing, tidak untuk running app

### Error: "plantuml.jar not found"
- Hanya diperlukan untuk generate diagram
- Aplikasi web bisa jalan tanpa ini

---

Untuk pertanyaan, hubungi: [email/contact]
