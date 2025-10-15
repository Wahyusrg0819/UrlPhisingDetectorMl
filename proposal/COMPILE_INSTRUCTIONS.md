# Instruksi Kompilasi Proposal

## Struktur File

```
proposal/
├── main.tex              # File utama LaTeX
├── bab1.tex              # BAB 1: Pendahuluan
├── bab2.tex              # BAB 2: Landasan Teori
├── bab3.tex              # BAB 3: Metodologi Penelitian
├── diagrams/             # Folder diagram PlantUML
│   ├── *.puml           # File diagram PlantUML
│   ├── *.png            # Output PNG (setelah compile)
│   ├── plantuml.jar     # PlantUML compiler (download dulu)
│   ├── compile.bat      # Script compile Windows
│   └── compile.sh       # Script compile Linux/Mac
└── logo-universitas.png  # Logo UIR (siapkan dulu)
```

## Langkah-Langkah Kompilasi

### 1. Persiapan Diagram

#### A. Download PlantUML

```bash
cd proposal/diagrams
```

Download plantuml.jar dari: https://plantuml.com/download

Atau gunakan wget:
```bash
wget https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-1.2024.0.jar -O plantuml.jar
```

#### B. Compile Diagram

**Windows:**
```bash
compile.bat
```

**Linux/Mac:**
```bash
chmod +x compile.sh
./compile.sh
```

Atau manual:
```bash
java -jar plantuml.jar *.puml
```

**Output:** File PNG akan ter-generate:
- system-flowchart.png
- usecase-diagram.png
- sequence-diagram.png
- architecture-diagram.png

### 2. Persiapan Logo

Letakkan file `logo-universitas.png` di folder `proposal/`

Download logo UIR dari website resmi atau:
- Format: PNG
- Ukuran: 1000x1000 pixels (optimal)

### 3. Kompilasi LaTeX

#### Opsi 1: Command Line (pdflatex)

```bash
cd proposal
pdflatex main.tex
pdflatex main.tex  # Jalankan 2x untuk ToC dan referensi
```

#### Opsi 2: Overleaf (Online)

1. Upload semua file .tex ke Overleaf
2. Upload folder diagrams/ dengan file PNG
3. Upload logo-universitas.png
4. Set main.tex sebagai main document
5. Compile

#### Opsi 3: TeXstudio/TeXworks

1. Buka main.tex
2. Klik Build & View (F5)
3. Jika error, compile 2x

### 4. Verifikasi Output

File `main.pdf` akan berisi:
- Cover (halaman i)
- Daftar Isi (halaman ii)
- BAB 1: Pendahuluan (halaman 1-5)
- BAB 2: Landasan Teori (halaman 6-12)
- BAB 3: Metodologi Penelitian (halaman 13-18)

## Troubleshooting

### Error: "File not found: diagrams/xxx.png"

**Solusi:**
1. Pastikan diagram sudah di-compile
2. Cek file PNG ada di folder diagrams/
3. Atau comment baris `\includegraphics` sementara

### Error: "File not found: logo-universitas.png"

**Solusi:**
1. Siapkan file logo
2. Atau comment baris logo di main.tex:
```latex
% \includegraphics[width=0.3\textwidth]{logo-universitas.png}
```

### Error: "Package babel Error: Unknown option 'bahasa'"

**Solusi:**
Install package babel-indonesian:
```bash
# MiKTeX
mpm --install=babel-indonesian

# TeX Live
tlmgr install babel-indonesian
```

### Error: "Font Times New Roman not found"

**Solusi:**
Package mathptmx sudah include Times New Roman.
Jika masih error, gunakan:
```latex
\usepackage{times}
```

### Diagram tidak muncul di PDF

**Solusi:**
1. Pastikan file PNG sudah ter-generate
2. Cek path file di .tex (harus relatif)
3. Compile LaTeX 2x

## Tips

1. **Compile diagram dulu** sebelum compile LaTeX
2. **Compile LaTeX 2x** untuk ToC dan referensi yang benar
3. **Gunakan Overleaf** jika ada masalah dengan local installation
4. **Backup file** sebelum edit besar-besaran

## Kontak

Jika ada masalah, cek:
- LaTeX error log (main.log)
- PlantUML error message
- README.md di folder diagrams/
