# Update Backend URL

## 🔄 Cara Update URL Ngrok

Setiap kali restart ngrok, URL akan berubah. Ikuti langkah ini untuk update:

### **Opsi 1: Edit .env.local (Recommended)**

```bash
# 1. Buka file .env.local
# 2. Update URL ngrok yang baru
NEXT_PUBLIC_API_URL=https://NEW-NGROK-URL.ngrok-free.app

# 3. Restart Next.js dev server
npm run dev
```

### **Opsi 2: Edit Langsung di Code**

```typescript
// frontend/app/page.tsx
// Cari baris ini dan update URL:
const BACKEND_URL = process.env.NEXT_PUBLIC_API_URL || 'https://NEW-URL.ngrok-free.app'
```

---

## 📝 **Current Configuration**

**Backend URL:** `https://879873ce7d41.ngrok-free.app`

**API Endpoint:** `https://879873ce7d41.ngrok-free.app/api/predict/`

---

## 🧪 **Testing**

### Test Backend (Browser/Postman):
```
GET https://879873ce7d41.ngrok-free.app/api/predict/
```

### Test dengan curl:
```bash
curl -X POST https://879873ce7d41.ngrok-free.app/api/predict/ \
  -H "Content-Type: application/json" \
  -d '{"url": "https://google.com"}'
```

### Test Frontend:
```bash
cd frontend
npm run dev
# Buka http://localhost:3000
# Input URL dan klik Analisis
```

---

## 🔧 **Troubleshooting**

### Error: "Failed to fetch"
**Penyebab:** Backend tidak running atau URL salah

**Solusi:**
1. Pastikan Django running: `python manage.py runserver 0.0.0.0:8000`
2. Pastikan ngrok running: `ngrok http 8000`
3. Check URL di ngrok terminal
4. Update URL di `.env.local`
5. Restart Next.js: `npm run dev`

### Error: "CORS policy"
**Penyebab:** CORS tidak dikonfigurasi

**Solusi:** Sudah dikonfigurasi di `backend/config/settings.py`
```python
CORS_ALLOW_ALL_ORIGINS = True
```

### Error: "Invalid Host header"
**Penyebab:** Ngrok domain tidak di ALLOWED_HOSTS

**Solusi:** Sudah dikonfigurasi di `backend/config/settings.py`
```python
ALLOWED_HOSTS = [
    '.ngrok.io',
    '.ngrok-free.app',
    '*',
]
```

---

## 🌐 **Environment Variables**

### Development (Local Backend):
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Development (Ngrok):
```env
NEXT_PUBLIC_API_URL=https://879873ce7d41.ngrok-free.app
```

### Production:
```env
NEXT_PUBLIC_API_URL=https://your-production-api.com
```

---

## 📋 **Quick Commands**

```bash
# Get current ngrok URL
curl http://localhost:4040/api/tunnels | grep -o 'https://[^"]*ngrok-free.app'

# Update .env.local (manual)
echo "NEXT_PUBLIC_API_URL=https://NEW-URL.ngrok-free.app" > frontend/.env.local

# Restart frontend
cd frontend
npm run dev
```

---

## 💡 **Tips**

1. **Bookmark ngrok dashboard:** http://localhost:4040
2. **Copy URL dari ngrok terminal** setiap restart
3. **Gunakan .env.local** untuk easy update
4. **Restart Next.js** setelah update .env.local
5. **Untuk fixed URL:** Upgrade ngrok atau gunakan Cloudflare Tunnel

---

**Last Updated:** URL ngrok saat ini
**Expires:** Saat ngrok di-restart
