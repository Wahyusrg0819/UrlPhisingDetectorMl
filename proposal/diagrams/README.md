# Diagram PlantUML

Folder ini berisi diagram-diagram untuk proposal dalam format PlantUML (.puml).

## Daftar Diagram

### Diagram Utama (4)
1. **system-flowchart.puml** - Flowchart sistem keseluruhan
2. **usecase-diagram.puml** - Use case diagram
3. **sequence-diagram.puml** - Sequence diagram prediksi URL
4. **architecture-diagram.puml** - Arsitektur sistem

### Diagram Detail (4)
5. **process-flowchart.puml** - Flowchart proses aplikasi web (swimlane)
6. **logic-flowchart.puml** - Flowchart logika prediksi model
7. **feature-extraction-flowchart.puml** - Flowchart detail ekstraksi fitur
8. **model-prediction-flowchart.puml** - Flowchart logika Random Forest

### Diagram SDLC (8 variasi)
9. **sdlc-waterfall.puml** - SDLC Waterfall vertikal (classic)
10. **sdlc-waterfall-cascade.puml** - SDLC cascade seperti air terjun
11. **sdlc-zigzag.puml** - SDLC zigzag flow (kanan-bawah-kanan)
12. **sdlc-horizontal.puml** - SDLC horizontal (left to right)
13. **sdlc-circular.puml** - SDLC circular/state view
14. **sdlc-mindmap.puml** - SDLC mind map view
15. **sdlc-phases-detail.puml** - SDLC detail aktivitas per fase
16. **sdlc-timeline.puml** - SDLC timeline/gantt chart

## Cara Kompilasi

### Opsi 1: Menggunakan plantuml.jar (Recommended)

1. Download `plantuml.jar` dari https://plantuml.com/download
2. Letakkan file `plantuml.jar` di folder `proposal/diagrams/`
3. Jalankan compile script:

**Windows:**
```bash
cd proposal/diagrams
compile.bat
```

**Linux/Mac:**
```bash
cd proposal/diagrams
chmod +x compile.sh
./compile.sh
```

Atau compile manual:
```bash
java -jar plantuml.jar *.puml
```

### Opsi 2: Menggunakan VS Code Extension

1. Install extension "PlantUML" di VS Code
2. Buka file .puml
3. Tekan `Alt+D` untuk preview
4. Klik kanan → Export Current Diagram → PNG

### Opsi 3: Online Editor

1. Buka https://www.plantuml.com/plantuml/uml/
2. Copy-paste isi file .puml
3. Download PNG yang dihasilkan

## Output

Setelah kompilasi, akan dihasilkan file PNG:
- `system-flowchart.png`
- `usecase-diagram.png`
- `sequence-diagram.png`
- `architecture-diagram.png`

File PNG ini akan digunakan di dokumen LaTeX (BAB 3).

## Catatan

- Pastikan Java sudah terinstall untuk menjalankan plantuml.jar
- Cek versi Java: `java -version`
- Font yang digunakan: Times New Roman (sesuai dokumen)
