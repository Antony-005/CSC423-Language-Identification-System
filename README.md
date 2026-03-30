# CSC423 - Language Identification System

## Overview
An NLP system that detects the language of short text in:
- Swahili
- English
- Sheng (Nairobi urban slang)
- Luo (Dholuo)

## Files
| File | Description |
|------|-------------|
| language_dataset.csv | 300 labelled samples (75 per language) |
| app.py | Streamlit web interface |
| language_id_model.pkl | Trained Logistic Regression model |
| confusion_matrices.png | Model evaluation heatmaps |
| model_comparison.png | Accuracy comparison chart |

## Models Used
- Multinomial Naive Bayes
- Logistic Regression (best performer)
- SVM (LinearSVC)

## Course
CSC423 - Special Topics in NLP
