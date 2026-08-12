# Kalp Hastalığı Tahmini

Bu projede, klinik hasta verileri kullanılarak kalp hastalığı riskini tahmin eden makine öğrenmesi modelleri geliştirilmiştir.

## Amaç

Amaç, hastanın yaş, cinsiyet, göğüs ağrısı tipi, kolesterol düzeyi, maksimum kalp atış hızı ve egzersiz kaynaklı anjina gibi bilgilerini kullanarak kalp hastalığı riski olup olmadığını tahmin etmektir.

> Bu proje eğitim amaçlıdır; tıbbi tanı veya klinik karar desteği yerine kullanılamaz.

## Veri Seti

- Toplam kayıt: 920
- Hedef değişken: `target`
  - `0`: Kalp hastalığı yok
  - `1`: Kalp hastalığı riski var
- Eksik değer içeren sütunlar uygun yöntemlerle model işlem hattında doldurulmuştur.
- Çok fazla eksik değer içeren `ca`, `thal` ve `slope` sütunları çıkarılmıştır.
- Veri kaynağı bilgisinin genellenebilirliği azaltmaması için `dataset` sütunu nihai modellerde kullanılmamıştır.

## Kullanılan Modeller

- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Naive Bayes
- Decision Tree
- Random Forest
- Artificial Neural Network (ANN / MLP)

## Model Karşılaştırması

| Model | Accuracy | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|
| SVM | %80.9 | %85.1 | 0.831 | 0.885 |
| Random Forest | %82.0 | %83.1 | 0.836 | 0.880 |
| KNN | %81.8 | %86.1 | 0.840 | 0.869 |
| Naive Bayes | %80.1 | %81.7 | 0.820 | 0.882 |
| Decision Tree | %76.6 | %76.4 | 0.783 | 0.837 |
| ANN | %72.9 | %75.6 | 0.755 | 0.771 |

## Nihai Model

KNN modeli, kalp hastalığı vakalarını yakalama oranı (`recall`) ve F1 skoru açısından en iyi sonuçları verdiği için nihai model olarak seçilmiştir.

Nihai model dosyası:

```text
models/heart_disease_knn_final_model.joblib
```

## Proje Yapısı

```text
heart-disease-ml/
│
├── data/
│   └── heart_disease_uci.csv
│
├── notebooks/
│   └── heart_disease_analysis.ipynb
│
├── models/
│   ├── heart_disease_model.joblib
│   ├── heart_disease_final_model.joblib
│   └── heart_disease_knn_final_model.joblib
│
└── README.md
```

## Çalıştırma

Gerekli paketleri yüklemek için:

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel joblib
```

Ardından Jupyter Notebook veya VS Code üzerinden aşağıdaki notebook dosyası açılabilir:

```text
notebooks/heart_disease_analysis.ipynb
```