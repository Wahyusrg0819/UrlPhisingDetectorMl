# Model Evaluation Visualizations

## 📊 Generated Visualizations

Folder ini berisi 6 visualisasi hasil evaluasi model Random Forest untuk presentasi.

### 1. Overall Metrics (1_overall_metrics.png)
**Bar chart** menampilkan 4 metrik utama:
- Accuracy: 90.82%
- Precision: 90.67%
- Recall: 90.82%
- F1-Score: 90.63%

**Penggunaan**: Slide evaluasi model, overview performance

### 2. Confusion Matrix (2_confusion_matrix.png)
**Heatmap** confusion matrix 4x4 untuk 4 kelas:
- Benign, Defacement, Malware, Phishing
- Menunjukkan true positive, false positive, dll
- Warna biru gradient (semakin gelap = semakin banyak)

**Penggunaan**: Detail analisis prediksi, error analysis

### 3. Per-Class Performance (3_per_class_performance.png)
**Grouped bar chart** menampilkan Precision, Recall, F1-Score untuk setiap kelas:
- Benign: 93% / 97% / 95%
- Defacement: 84% / 83% / 84%
- Malware: 92% / 86% / 89%
- Phishing: 87% / 74% / 80%

**Penggunaan**: Perbandingan performa antar kelas

### 4. Class Distribution (4_class_distribution.png)
**Bar chart + Pie chart** distribusi kelas di test set:
- Benign: 65.7%
- Defacement: 14.8%
- Phishing: 14.5%
- Malware: 5.0%

**Penggunaan**: Menunjukkan dataset balance/imbalance

### 5. Feature Importance (5_feature_importance.png)
**Horizontal bar chart** ranking fitur berdasarkan importance:
1. num_slashes: 28.53%
2. has_www: 22.50%
3. url_length: 22.31%
4. num_dots: 14.53%
5. num_hyphens: 5.86%
6. has_https: 4.09%
7. has_numeric: 2.18%

**Penggunaan**: Menjelaskan fitur mana yang paling berpengaruh

### 6. Accuracy Card (6_accuracy_card.png)
**Summary card** dengan angka akurasi besar:
- 90.82% (font besar, eye-catching)
- Info: Random Forest 100 trees, 130,239 test samples

**Penggunaan**: Slide pembuka hasil, highlight achievement

## 🎨 Spesifikasi Teknis

- **Resolution**: 300 DPI (print quality)
- **Format**: PNG with transparency support
- **Color Scheme**: Professional (blue, purple, orange, red)
- **Font**: Default matplotlib (readable)
- **Size**: Optimized for 16:9 presentation

## 📝 Cara Menggunakan di Presentasi

### PowerPoint:
1. Insert → Pictures
2. Pilih file PNG yang diinginkan
3. Resize sesuai kebutuhan (maintain aspect ratio)
4. Posisikan di slide

### LaTeX (Proposal):
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{visualizations/1_overall_metrics.png}
    \caption{Overall Model Performance Metrics}
    \label{fig:overall-metrics}
\end{figure}
```

## 🔄 Regenerate Visualizations

Jika perlu regenerate (misalnya setelah retrain model):

```bash
python generate_visualizations.py
```

Script akan:
1. Load model terbaru
2. Load dataset
3. Extract features
4. Split data (80-20)
5. Generate 6 visualizations
6. Save ke folder visualizations/

## 📊 Rekomendasi Penggunaan

### Untuk Presentasi (10 slide):
- **Slide 9**: Gunakan `1_overall_metrics.png` atau `6_accuracy_card.png`
- Tambahan: `3_per_class_performance.png` jika ada waktu

### Untuk Proposal (BAB 3):
- **Hasil Evaluasi**: `1_overall_metrics.png`
- **Confusion Matrix**: `2_confusion_matrix.png`
- **Feature Analysis**: `5_feature_importance.png`

### Untuk Laporan Lengkap:
- Gunakan semua 6 visualisasi
- Tambahkan caption dan penjelasan

## 💡 Tips

1. **High Quality**: Semua gambar 300 DPI, cocok untuk print
2. **Consistent Style**: Warna dan style konsisten antar visualisasi
3. **Clear Labels**: Semua axis dan legend jelas terbaca
4. **Professional**: Cocok untuk presentasi akademik/profesional

## 📁 File Structure

```
visualizations/
├── 1_overall_metrics.png       (10x6 inches)
├── 2_confusion_matrix.png      (10x8 inches)
├── 3_per_class_performance.png (12x6 inches)
├── 4_class_distribution.png    (14x6 inches)
├── 5_feature_importance.png    (10x6 inches)
├── 6_accuracy_card.png         (10x6 inches)
└── README.md                   (dokumentasi ini)
```

Semua visualisasi siap digunakan untuk presentasi dan dokumentasi! 🎯
