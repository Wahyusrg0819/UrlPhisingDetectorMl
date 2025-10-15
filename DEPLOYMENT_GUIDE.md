## 🌐 **Deployment Guide - Expose Backend**

### **Quick Start dengan Ngrok** ⭐

#### 1. Install Ngrok
```bash
# Download dari: https://ngrok.com/download
# Atau via Chocolatey (Windows):
choco install ngrok
```

#### 2. Setup Ngrok
```bash
# Sign up di ngrok.com (gratis)
# Get authtoken dari dashboard
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

#### 3. Run Backend + Ngrok
```bash
# Windows
cd backend
run_with_ngrok.bat

# Linux/Mac
cd backend
chmod +x run_with_ngrok.sh
./run_with_ngrok.sh
```

#### 4. Copy Public URL
```
Forwarding  https://abc123.ngrok-free.app -> http://localhost:8000
```

#### 5. Update Frontend
```typescript
// frontend/app/page.tsx
const response = await fetch('https://abc123.ngrok-free.app/api/predict/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ url }),
})
```

---

### **Alternatif: LocalTunnel**

```bash
# Install
npm install -g localtunnel

# Run Django
python manage.py runserver 0.0.0.0:8000

# Expose
lt --port 8000 --subdomain mybackend
```

**URL:** `https://mybackend.loca.lt`

---

### **Alternatif: Network Lokal (LAN)**

#### 1. Cek IP Laptop
```bash
# Windows
ipconfig
# Cari IPv4 Address, contoh: 192.168.1.100

# Linux/Mac
ifconfig
# atau
ip addr show
```

#### 2. Run Django
```bash
python manage.py runserver 0.0.0.0:8000
```

#### 3. Akses dari Device Lain (WiFi sama)
```
http://192.168.1.100:8000/api/predict/
```

---

### **Perbandingan Metode**

| Metode | Akses | Setup | Gratis | Permanent |
|--------|-------|-------|--------|-----------|
| **Ngrok** | Internet | Easy | ✅ | ❌ (URL berubah) |
| LocalTunnel | Internet | Easy | ✅ | ❌ |
| LAN | WiFi sama | Very Easy | ✅ | ✅ |
| Cloudflare | Internet | Medium | ✅ | ✅ |
| VPS | Internet | Hard | ❌ | ✅ |

---

### **Testing Endpoint**

```bash
# Test dengan curl
curl -X POST https://your-ngrok-url.ngrok-free.app/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"url": "https://google.com"}'

# Test dengan browser
https://your-ngrok-url.ngrok-free.app/api/predict/
```

---

### **Troubleshooting**

#### Error: "Invalid Host header"
**Solusi:** Tambahkan domain ke `ALLOWED_HOSTS` di `settings.py`

#### Error: "CORS policy"
**Solusi:** Set `CORS_ALLOW_ALL_ORIGINS = True` di `settings.py`

#### Error: "Connection refused"
**Solusi:** Pastikan Django run di `0.0.0.0:8000` bukan `127.0.0.1:8000`

#### Ngrok URL berubah setiap restart
**Solusi:** 
- Upgrade ke Ngrok paid plan (fixed domain)
- Atau gunakan Cloudflare Tunnel (gratis, permanent)

---

### **Security Notes** ⚠️

1. **Jangan expose production** dengan `DEBUG = True`
2. **Gunakan HTTPS** (ngrok otomatis provide)
3. **Limit CORS** di production
4. **Jangan share authtoken** ngrok
5. **Monitor traffic** di ngrok dashboard

---

### **Production Deployment**

Untuk production, gunakan:
- **Heroku** (free tier)
- **Railway** (free tier)
- **Render** (free tier)
- **DigitalOcean** ($5/month)
- **AWS EC2** (free tier 1 tahun)

---

Untuk pertanyaan, hubungi: [email/contact]
