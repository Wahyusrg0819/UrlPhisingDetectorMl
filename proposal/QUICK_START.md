# Quick Start Guide

## Langkah Cepat Compile Proposal

### 1. Persiapan (Hanya sekali)

#### A. Install Java
```bash
java -version
```
Jika belum ada, install dari https://www.java.com/download/

#### B. Download PlantUML
```bash
cd proposal/diagrams
```
Download dari: https://plantuml.com/download
Letakkan file `plantuml.jar` di folder `diagrams/`

#### C. Siapkan Logo
Letakkan `logo-universitas.png` di folder `proposal/`

### 2. Generate Diagram

```bash
cd proposal/diagrams

# Windows
compile.bat

# Linux/Mac
chmod +x compile.sh
./compile.sh
```

**Output:** 4 file PNG akan ter-generate di folder `diagrams/`

### 3. Compile LaTeX

```bash
cd proposal
pdflatex main.tex
pdflatex main.tex
```

**Output:** File `main.pdf` akan ter-generate

### 4. Buka PDF

```bash
# Windows
start main.pdf

# Mac
open main.pdf

# Linux
xdg-open main.pdf
```

## Troubleshooting Cepat

### Gambar tidak muncul?
1. Pastikan file PNG sudah ada di `diagrams/`
2. Compile LaTeX 2x

### Error plantuml.jar?
Download dari: https://plantuml.com/download

### Error logo?
Comment baris logo di `main.tex`:
```latex
% \includegraphics[width=0.3\textwidth]{logo-universitas.png}
```

### Masih error?
Baca `COMPILE_INSTRUCTIONS.md` untuk detail lengkap

## Alternative: Overleaf

1. Upload semua file .tex ke Overleaf
2. Compile diagram dulu, upload PNG ke folder diagrams/
3. Upload logo
4. Compile di Overleaf

## Struktur File Penting

```
proposal/
├── main.tex                    # File utama
├── bab1.tex, bab2.tex, bab3.tex
├── logo-universitas.png        # Logo (siapkan!)
└── diagrams/
    ├── *.puml                  # Source diagram
    ├── *.png                   # Output (setelah compile)
    └── plantuml.jar            # Compiler (download!)
```

## Konten Proposal

- **BAB 1**: Pendahuluan (Latar Belakang, Masalah, Tujuan)
- **BAB 2**: Landasan Teori (Phishing, ML, Teknologi)
- **BAB 3**: Metodologi (Tahapan, Diagram, Jadwal)

Total: ~18 halaman

## Tips

✅ Compile diagram **sebelum** compile LaTeX
✅ Compile LaTeX **2x** untuk ToC yang benar
✅ Gunakan **Overleaf** jika ada masalah local
✅ Backup file sebelum edit besar

Selamat mengerjakan! 🎓
