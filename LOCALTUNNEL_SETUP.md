# LocalTunnel Setup Guide

## 🚀 Quick Start

### 1. Install LocalTunnel (Sekali Saja)
```powershell
npm install -g localtunnel
```

### 2. Run Backend + LocalTunnel

**Windows:**
```powershell
cd backend
.\run_with_localtunnel.bat
```

**PowerShell:**
```powershell
cd backend
.\run_with_localtunnel.ps1
```

**Manual (2 Terminal):**
```powershell
# Terminal 1 - Django
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver 0.0.0.0:8000

# Terminal 2 - LocalTunnel
lt --port 8000
```

### 3. Copy URL
```
your url is: https://random-xyz.loca.lt
```

### 4. Update Frontend
```powershell
# Edit file: frontend/.env.local
NEXT_PUBLIC_API_URL=https://random-xyz.loca.lt
```

### 5. Restart Frontend (Local)
```powershell
cd frontend
npm run dev
```

### 6. Deploy ke Vercel
```powershell
git add frontend/.env.local
git commit -m "Update backend URL to LocalTunnel"
git push
```

**ATAU** update di Vercel Dashboard:
1. Go to: https://vercel.com/dashboard
2. Select project: url-phising-detector-ml
3. Settings → Environment Variables
4. Add/Update: `NEXT_PUBLIC_API_URL` = `https://random-xyz.loca.lt`
5. Redeploy

---

## 🔧 LocalTunnel Options

### Custom Subdomain (Recommended)
```powershell
lt --port 8000 --subdomain mybackend
```
URL: `https://mybackend.loca.lt`

**Keuntungan:** URL tidak berubah setiap restart!

### With Password Protection
```powershell
lt --port 8000 --subdomain mybackend --print-requests
```

---

## 🧪 Testing

### Test Backend Directly
```powershell
curl -X POST https://your-url.loca.lt/api/predict/ `
  -H "Content-Type: application/json" `
  -d '{\"url\":\"https://google.com\"}'
```

### Test from Vercel
1. Open: https://url-phising-detector-ml.vercel.app
2. Input URL: `https://google.com`
3. Click "Analisis"
4. Should work! ✅

---

## 📝 Environment Variable Workflow

### Development (Local)
```env
# frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Development (LocalTunnel)
```env
# frontend/.env.local
NEXT_PUBLIC_API_URL=https://mybackend.loca.lt
```

### Production (Vercel)
Set di Vercel Dashboard:
```
NEXT_PUBLIC_API_URL=https://mybackend.loca.lt
```

---

## ⚠️ Important Notes

### LocalTunnel First-Time Access
Saat pertama kali akses URL LocalTunnel, akan muncul halaman:
```
"Click Continue" to visit this site
```

Ini normal, klik "Continue" dan akan redirect ke aplikasi.

### URL Persistence
- **Tanpa subdomain:** URL berubah setiap restart
- **Dengan subdomain:** URL tetap sama (recommended!)

### Keep Alive
LocalTunnel akan disconnect jika tidak ada traffic. Untuk keep alive:
```powershell
# Ping setiap 5 menit
while ($true) { 
    curl https://your-url.loca.lt/api/predict/ 
    Start-Sleep 300 
}
```

---

## 🔄 Update URL Workflow

### Jika URL LocalTunnel Berubah:

1. **Update .env.local:**
```powershell
# Edit: frontend/.env.local
NEXT_PUBLIC_API_URL=https://NEW-URL.loca.lt
```

2. **Commit & Push:**
```powershell
git add frontend/.env.local
git commit -m "Update backend URL"
git push
```

3. **Vercel Auto-Deploy** (tunggu ~1 menit)

4. **Test:** https://url-phising-detector-ml.vercel.app

---

## 💡 Pro Tips

### Use Custom Subdomain
```powershell
lt --port 8000 --subdomain phishing-detector-backend
```
URL: `https://phishing-detector-backend.loca.lt`

### Monitor Requests
```powershell
lt --port 8000 --subdomain mybackend --print-requests
```

### Check LocalTunnel Status
```powershell
# LocalTunnel dashboard
# No dashboard, check terminal output
```

---

## 🆘 Troubleshooting

### Error: "lt: command not found"
```powershell
npm install -g localtunnel
```

### Error: "Connection refused"
```powershell
# Pastikan Django running di 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
```

### Error: "Subdomain already taken"
```powershell
# Gunakan subdomain lain atau tanpa subdomain
lt --port 8000
```

### CORS Error
Sudah dikonfigurasi di Django, seharusnya tidak ada masalah.

---

## 📊 Comparison

| Feature | Ngrok | LocalTunnel |
|---------|-------|-------------|
| Free | ✅ (banned) | ✅ |
| Custom subdomain | ❌ (paid) | ✅ |
| Stable | ✅ | ⚠️ (disconnect) |
| Speed | Fast | Medium |
| Setup | Easy | Very Easy |
| **Recommended** | ❌ | ✅ |

---

Gunakan LocalTunnel dengan custom subdomain untuk URL yang konsisten! 🎯
