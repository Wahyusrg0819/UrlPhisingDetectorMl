"""
Generate visualizations untuk hasil evaluasi model
Output: PNG files untuk presentasi
"""

import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import re
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def extract_features(url):
    """Extract lexical features dari URL"""
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_www': 1 if 'www' in url else 0,
        'has_https': 1 if 'https' in url else 0,
        'num_hyphens': url.count('-'),
        'num_slashes': url.count('/'),
        'has_numeric': 1 if bool(re.search(r'\d', url)) else 0,
    }
    
    return [
        features['url_length'],
        features['num_dots'],
        features['has_www'],
        features['has_https'],
        features['num_hyphens'],
        features['num_slashes'],
        features['has_numeric']
    ]

print("="*80)
print("GENERATING VISUALIZATIONS FOR MODEL EVALUATION")
print("="*80)
print()

# Load model
print("1. Loading model...")
model = joblib.load('phishing_model.pkl')
print(f"   ✓ Model: {type(model).__name__}")
print(f"   ✓ Trees: {model.n_estimators}")
print()

# Load dataset
print("2. Loading dataset...")
df = pd.read_csv('malicious_phish.csv')
print(f"   ✓ Total samples: {len(df):,}")
print()

# Extract features
print("3. Extracting features...")
X = []
y = []

for idx, row in df.iterrows():
    try:
        url = str(row['url'])
        label = str(row['type'])
        features = extract_features(url)
        X.append(features)
        y.append(label)
    except:
        continue

X = np.array(X)
y = np.array(y)
print(f"   ✓ Features extracted: {len(X):,}")
print()

# Split data
print("4. Splitting data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"   ✓ Test set: {len(X_test):,}")
print()

# Predictions
print("5. Making predictions...")
y_pred = model.predict(X_test)
print(f"   ✓ Predictions completed")
print()

print("6. Generating visualizations...")
print("-" * 80)

# Create output directory
import os
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# ========== VISUALIZATION 1: Overall Metrics Bar Chart ==========
print("   Creating: 1_overall_metrics.png")

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

metrics = {
    'Accuracy': accuracy_score(y_test, y_pred),
    'Precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
    'Recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
    'F1-Score': f1_score(y_test, y_pred, average='weighted', zero_division=0)
}

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(metrics.keys(), [v*100 for v in metrics.values()], 
              color=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D'], 
              edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}%',
            ha='center', va='bottom', fontsize=14, fontweight='bold')

ax.set_ylabel('Score (%)', fontsize=14, fontweight='bold')
ax.set_title('Overall Model Performance Metrics', fontsize=16, fontweight='bold', pad=20)
ax.set_ylim(0, 100)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.axhline(y=90, color='green', linestyle='--', alpha=0.5, label='90% Threshold')
ax.legend()

plt.tight_layout()
plt.savefig('visualizations/1_overall_metrics.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved")

# ========== VISUALIZATION 2: Confusion Matrix Heatmap ==========
print("   Creating: 2_confusion_matrix.png")

cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=model.classes_, 
            yticklabels=model.classes_,
            cbar_kws={'label': 'Count'},
            linewidths=0.5, linecolor='gray',
            ax=ax)

ax.set_xlabel('Predicted Label', fontsize=14, fontweight='bold')
ax.set_ylabel('True Label', fontsize=14, fontweight='bold')
ax.set_title('Confusion Matrix', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('visualizations/2_confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved")

# ========== VISUALIZATION 3: Per-Class Performance ==========
print("   Creating: 3_per_class_performance.png")

from sklearn.metrics import precision_recall_fscore_support

precision, recall, f1, support = precision_recall_fscore_support(
    y_test, y_pred, labels=model.classes_, zero_division=0
)

x = np.arange(len(model.classes_))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width, precision*100, width, label='Precision', 
               color='#2E86AB', edgecolor='black', linewidth=1)
bars2 = ax.bar(x, recall*100, width, label='Recall', 
               color='#A23B72', edgecolor='black', linewidth=1)
bars3 = ax.bar(x + width, f1*100, width, label='F1-Score', 
               color='#F18F01', edgecolor='black', linewidth=1)

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}',
                ha='center', va='bottom', fontsize=9)

ax.set_ylabel('Score (%)', fontsize=14, fontweight='bold')
ax.set_xlabel('Class', fontsize=14, fontweight='bold')
ax.set_title('Per-Class Performance Metrics', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(model.classes_, fontsize=12)
ax.legend(fontsize=12)
ax.set_ylim(0, 105)
ax.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/3_per_class_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved")

# ========== VISUALIZATION 4: Class Distribution ==========
print("   Creating: 4_class_distribution.png")

class_counts = pd.Series(y_test).value_counts()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Bar chart
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
bars = ax1.bar(class_counts.index, class_counts.values, 
               color=colors, edgecolor='black', linewidth=1.5)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax1.set_ylabel('Count', fontsize=14, fontweight='bold')
ax1.set_xlabel('Class', fontsize=14, fontweight='bold')
ax1.set_title('Test Set Class Distribution (Bar)', fontsize=14, fontweight='bold')
ax1.grid(axis='y', alpha=0.3, linestyle='--')

# Pie chart
ax2.pie(class_counts.values, labels=class_counts.index, autopct='%1.1f%%',
        colors=colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'},
        wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
ax2.set_title('Test Set Class Distribution (Pie)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/4_class_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved")

# ========== VISUALIZATION 5: Feature Importance ==========
print("   Creating: 5_feature_importance.png")

feature_names = ['url_length', 'num_dots', 'has_www', 'has_https', 
                'num_hyphens', 'num_slashes', 'has_numeric']
importances = model.feature_importances_

# Sort by importance
indices = np.argsort(importances)[::-1]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh([feature_names[i] for i in indices], 
               [importances[i]*100 for i in indices],
               color='#2E86AB', edgecolor='black', linewidth=1.5)

# Add value labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f'{width:.2f}%',
            ha='left', va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Importance (%)', fontsize=14, fontweight='bold')
ax.set_title('Feature Importance in Random Forest Model', fontsize=16, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('visualizations/5_feature_importance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved")

# ========== VISUALIZATION 6: Accuracy Summary Card ==========
print("   Creating: 6_accuracy_card.png")

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Main accuracy
accuracy = accuracy_score(y_test, y_pred)
ax.text(0.5, 0.7, f'{accuracy*100:.2f}%', 
        ha='center', va='center', fontsize=80, fontweight='bold',
        color='#2E86AB')

ax.text(0.5, 0.5, 'Overall Accuracy', 
        ha='center', va='center', fontsize=24, fontweight='bold')

# Additional info
info_text = f'Random Forest (100 trees)\n{len(X_test):,} test samples\n4 classes'
ax.text(0.5, 0.3, info_text, 
        ha='center', va='center', fontsize=16, style='italic')

# Border
rect = plt.Rectangle((0.05, 0.15), 0.9, 0.7, fill=False, 
                     edgecolor='#2E86AB', linewidth=3)
ax.add_patch(rect)

plt.savefig('visualizations/6_accuracy_card.png', dpi=300, bbox_inches='tight', 
            facecolor='white')
plt.close()
print("   ✓ Saved")

print()
print("="*80)
print("VISUALIZATION GENERATION COMPLETED")
print("="*80)
print()
print("Generated files in 'visualizations/' folder:")
print("  1. 1_overall_metrics.png       - Bar chart of overall metrics")
print("  2. 2_confusion_matrix.png      - Confusion matrix heatmap")
print("  3. 3_per_class_performance.png - Per-class metrics comparison")
print("  4. 4_class_distribution.png    - Class distribution (bar + pie)")
print("  5. 5_feature_importance.png    - Feature importance ranking")
print("  6. 6_accuracy_card.png         - Accuracy summary card")
print()
print("All images are 300 DPI, ready for presentation!")
print("="*80)
