# Instalasi PlantUML

## Download plantuml.jar

### Opsi 1: Download Langsung

1. Kunjungi: https://plantuml.com/download
2. Download file `plantuml.jar` (latest version)
3. Letakkan file di folder `proposal/diagrams/`

### Opsi 2: Menggunakan wget (Linux/Mac)

```bash
cd proposal/diagrams
wget https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-1.2024.0.jar -O plantuml.jar
```

### Opsi 3: Menggunakan curl (Linux/Mac)

```bash
cd proposal/diagrams
curl -L https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-1.2024.0.jar -o plantuml.jar
```

## Verifikasi Java

Pastikan Java sudah terinstall:

```bash
java -version
```

Jika belum terinstall:
- **Windows**: Download dari https://www.java.com/download/
- **Mac**: `brew install openjdk`
- **Linux**: `sudo apt install default-jre`

## Compile Diagram

Setelah plantuml.jar tersedia:

**Windows:**
```bash
compile.bat
```

**Linux/Mac:**
```bash
chmod +x compile.sh
./compile.sh
```

## Troubleshooting

### Error: "java: command not found"
- Install Java terlebih dahulu

### Error: "plantuml.jar not found"
- Pastikan file plantuml.jar ada di folder diagrams/
- Cek nama file (harus persis "plantuml.jar")

### Diagram tidak ter-generate
- Cek syntax file .puml
- Pastikan Java versi 8 atau lebih tinggi
- Jalankan manual: `java -jar plantuml.jar namafile.puml`

## Alternative: Online Compiler

Jika tidak bisa install Java/PlantUML:

1. Buka https://www.plantuml.com/plantuml/uml/
2. Copy-paste isi file .puml
3. Download PNG yang dihasilkan
4. Rename sesuai nama file asli
5. Letakkan di folder diagrams/
