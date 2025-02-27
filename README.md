# Parkinson's Disease Detection

A machine learning project to detect Parkinson's Disease using SVM classification based on biomedical voice measurements. The project involves data preprocessing, model training, and evaluation to achieve accurate predictions.

## Overview

This project aims to detect Parkinson's Disease using biomedical voice measurement data. The dataset is preprocessed, analyzed, and used to train a Support Vector Machine (SVM) model for classification.

## Dataset

The dataset contains multiple biomedical voice measurements, with key attributes including:
- **MDVP:Fo(Hz)** - Fundamental frequency
- **MDVP:Fhi(Hz)** - Highest vocal frequency
- **MDVP:Flo(Hz)** - Lowest vocal frequency
- **Jitter(%)** - Frequency variation
- **Shimmer(dB)** - Amplitude variation
- **HNR** - Harmonics-to-noise ratio
- **Status** - Target variable (1: Parkinson's, 0: Healthy)

## Data Preprocessing

1. **Handling Missing Values**: Checked for and handled missing values if necessary.
2. **Feature Selection**: Dropped the `name` column as it is not useful for prediction.
3. **Data Normalization**: Standardized the features using `StandardScaler`.
4. **Splitting Data**: Separated features (X) and target variable (Y), then split into training and test sets (80/20 split).

## Model Training

- Implemented **Support Vector Machine (SVM)** with a linear kernel for classification.
- Trained the model on the preprocessed dataset.
- Evaluated model performance using various classification metrics.

## Model Performance Metrics

- **Training Accuracy**: 88.46%
- **Testing Accuracy**: 87.18%
- **Precision**: 85.71%
- **Recall**: 90.12%
- **F1-Score**: 87.86%
- **Confusion Matrix**: Displayed TP, TN, FP, FN values to analyze classification performance.

## Installation

To run this project locally, install the required dependencies:

```bash
pip install numpy pandas scikit-learn
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/parkinsons-detection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd parkinsons-detection
   ```
3. Run the detection script:
   ```bash
   python detect_parkinsons.py --input sample_data.csv
   ```

## Model Saving

- The trained model is saved as `trained_model.pkl` for future use.

## Future Improvements

- Test different classification models such as Random Forest and Neural Networks.
- Improve feature engineering for better accuracy.
- Collect a larger dataset for better generalization.
