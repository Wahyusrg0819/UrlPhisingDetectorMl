# Proposal Proyek - Sistem Klasifikasi URL Phishing

## Struktur File

```
proposal/
├── main.tex          # File utama LaTeX
├── bab1.tex          # BAB 1: Pendahuluan
└── README.md         # Dokumentasi ini
```

## Isi Proposal

### BAB 1: PENDAHULUAN

1. **Latar Belakang**
   - Konteks penggunaan internet dan ancaman phishing
   - Statistik serangan phishing global
   - Pentingnya deteksi otomatis URL phishing
   - Pendekatan machine learning berbasis fitur leksikal

2. **Identifikasi Masalah** (4 poin)
   - Peningkatan serangan phishing
   - Kesulitan deteksi manual
   - Keterbatasan sistem existing
   - Kurangnya sistem real-time

3. **Rumusan Masalah** (3 poin)
   - Ekstraksi fitur leksikal
   - Pembangunan model ML
   - Integrasi ke sistem web

4. **Tujuan**
   - Tujuan umum: Merancang aplikasi web deteksi phishing
   - Tujuan khusus: 6 poin detail implementasi dan evaluasi

### BAB 2: LANDASAN TEORI

1. **Phishing**
   - Definisi dan jenis-jenis phishing
   - Karakteristik URL phishing

2. **Machine Learning**
   - Definisi dan jenis ML
   - Algoritma: Logistic Regression & Random Forest

3. **Fitur Leksikal**
   - 7 fitur yang digunakan

4. **Teknologi Web**
   - Django REST Framework
   - Next.js
   - RESTful API

5. **Evaluasi Model**
   - Metrik: Akurasi, Presisi, Recall, F1-Score

6. **Penelitian Terkait**

### BAB 3: METODOLOGI PENELITIAN

1. **Metode Penelitian** (R&D dengan Waterfall)

2. **Tahapan Penelitian**
   - Analisis Kebutuhan
   - Perancangan Sistem
   - Pengembangan Model ML
   - Implementasi Aplikasi Web
   - Testing & Evaluasi
   - Dokumentasi

3. **Diagram Alur Sistem**
   - Flowchart Sistem
   - Use Case Diagram
   - Sequence Diagram
   - Arsitektur Sistem

4. **Alat dan Bahan**
   - Hardware & Software
   - Dataset

5. **Jadwal Penelitian** (4 bulan)

## Cara Kompilasi

### Menggunakan pdflatex

```bash
cd proposal
pdflatex main.tex
pdflatex main.tex  # Jalankan 2x untuk table of contents
```

### Menggunakan Overleaf

1. Upload semua file .tex ke Overleaf
2. Set `main.tex` sebagai main document
3. Compile

### Menggunakan TeXstudio/TeXworks

1. Buka `main.tex`
2. Klik tombol Build & View (F5)

## Catatan Penting

1. **Logo Universitas**: 
   - Letakkan file `logo-universitas.png` di folder `proposal/`
   - Format: PNG, JPG, atau PDF
   - Ukuran optimal: 1000x1000 pixels
   - Jika tidak ada logo, comment baris logo di `main.tex`

2. **Informasi Mahasiswa**: 
   - Nama: Wahyu Muliadi Siregar
   - NPM: 223510883
   - Program Studi: Informatika
   - Fakultas: Teknik
   - Universitas: Universitas Islam Riau

3. **Font**: Times New Roman (seluruh dokumen)

4. **Format**: 
   - Cover: Font 14pt, margin 2cm
   - Daftar Isi: Margin 2cm
   - Isi: Font 12pt, margin 4-3-3-3, spasi 1.5

## Customization

### Mengubah Margin

Edit di `main.tex`:
```latex
\geometry{
    left=4cm,    % Margin kiri
    right=3cm,   % Margin kanan
    top=3cm,     % Margin atas
    bottom=3cm   % Margin bawah
}
```

### Mengubah Spasi

Edit di `main.tex`:
```latex
\onehalfspacing  % Spasi 1.5
% atau
\doublespacing   % Spasi 2
```

### Menambahkan BAB Baru

1. Buat file baru, misal `bab2.tex`
2. Tambahkan di `main.tex`:
```latex
\input{bab2.tex}
```

## Output

File PDF yang dihasilkan akan bernama `main.pdf` dengan struktur:
- Halaman judul
- Daftar isi
- BAB 1: Pendahuluan (4 section)

## Dependencies

Package LaTeX yang dibutuhkan:
- babel (bahasa Indonesia)
- geometry (margin)
- setspace (line spacing)
- graphicx (gambar)
- hyperref (hyperlink)
- titlesec (format judul)
- fancyhdr (header/footer)
