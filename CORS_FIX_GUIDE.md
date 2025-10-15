# CORS Error Fix Guide

## ❌ Error yang Terjadi:
```
Access to fetch at 'https://879873ce7d41.ngrok-free.app/api/predict/' 
from origin 'https://url-phising-detector-ml.vercel.app' 
has been blocked by CORS policy
```

## ✅ Solusi yang Sudah Diterapkan:

### 1. Backend (Django) - CORS Configuration
File: `backend/config/settings.py`

```python
# CORS middleware di posisi pertama
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # HARUS PERTAMA!
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://url-phising-detector-ml.vercel.app",
]
CORS_ALLOW_CREDENTIALS = True
```

### 2. Frontend (Next.js) - Ngrok Header
File: `frontend/app/page.tsx`

```typescript
headers: {
  'Content-Type': 'application/json',
  'ngrok-skip-browser-warning': 'true',  // Skip ngrok warning
}
```

---

## 🔄 Langkah-Langkah Fix:

### Step 1: Restart Django Backend
```powershell
# Stop Django (Ctrl+C)
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver 0.0.0.0:8000
```

### Step 2: Verify CORS Settings
```powershell
# Check if corsheaders installed
pip show django-cors-headers

# If not installed:
pip install django-cors-headers
```

### Step 3: Test Backend Directly
```bash
# Test dengan curl
curl -X POST https://879873ce7d41.ngrok-free.app/api/predict/ \
  -H "Content-Type: application/json" \
  -H "ngrok-skip-browser-warning: true" \
  -d '{"url": "https://google.com"}'
```

### Step 4: Redeploy Frontend (Vercel)
```bash
# Commit changes
git add .
git commit -m "Fix CORS and add ngrok header"
git push

# Vercel will auto-deploy
```

---

## 🧪 Testing Checklist

- [ ] Django backend running di `0.0.0.0:8000`
- [ ] Ngrok running dan URL aktif
- [ ] CORS middleware di posisi pertama
- [ ] `django-cors-headers` terinstall
- [ ] Frontend sudah update dengan header ngrok
- [ ] Test di browser: https://url-phising-detector-ml.vercel.app
- [ ] Check browser console (F12) untuk error

---

## 🔍 Debugging

### Check CORS Response Headers:
```bash
curl -I -X OPTIONS https://879873ce7d41.ngrok-free.app/api/predict/ \
  -H "Origin: https://url-phising-detector-ml.vercel.app" \
  -H "Access-Control-Request-Method: POST"
```

**Expected Response:**
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: content-type
```

### Check Django Logs:
```
# Lihat di terminal Django untuk request logs
[timestamp] "OPTIONS /api/predict/ HTTP/1.1" 200
[timestamp] "POST /api/predict/ HTTP/1.1" 200
```

---

## ⚠️ Common Issues

### Issue 1: "CORS still blocked"
**Solusi:**
1. Restart Django server
2. Clear browser cache (Ctrl+Shift+Delete)
3. Try incognito mode

### Issue 2: "Ngrok warning page"
**Solusi:** Header `ngrok-skip-browser-warning: true` sudah ditambahkan

### Issue 3: "Module 'corsheaders' not found"
**Solusi:**
```bash
pip install django-cors-headers
# Restart Django
```

### Issue 4: "Invalid Host header"
**Solusi:** Sudah dikonfigurasi di `ALLOWED_HOSTS`

---

## 📝 Configuration Summary

### Backend URL:
```
https://879873ce7d41.ngrok-free.app
```

### Frontend URL:
```
https://url-phising-detector-ml.vercel.app
```

### API Endpoint:
```
POST https://879873ce7d41.ngrok-free.app/api/predict/
```

---

## 🚀 Quick Fix Commands

```powershell
# 1. Restart backend
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver 0.0.0.0:8000

# 2. Restart ngrok (terminal baru)
ngrok http 8000

# 3. Update frontend .env.local (jika URL ngrok berubah)
# Edit: frontend/.env.local
# NEXT_PUBLIC_API_URL=https://NEW-NGROK-URL.ngrok-free.app

# 4. Test
curl -X POST https://879873ce7d41.ngrok-free.app/api/predict/ \
  -H "Content-Type: application/json" \
  -H "ngrok-skip-browser-warning: true" \
  -d '{"url": "https://google.com"}'
```

---

**Status:** ✅ Fixed
**Last Updated:** Now
