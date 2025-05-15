# Monza Pit Stop Predictor

A machine learning project that predicts whether a Formula 1 driver will pit on the next lap — built using historical race data from the Monza Grand Prix. The goal is to use this as a stepping stone toward building a full race strategy optimizer.

## Overview

This project uses:
- **Historical lap-by-lap telemetry and timing data**
- **Tyre compounds, life, lap times, and more**
- A **classification ML model** trained on past data to predict pit stops

It was created as part of my learning journey into machine learning through real-world motorsport applications.

---

## 📊 Data

- Source: [FastF1](https://theoehrly.github.io/Fast-F1/)
- Race: **Monza Grand Prix**
- Data includes:
  - Lap number
  - Tyre compound
  - Tyre life
  - Lap time
  - Driver
  - Pit stop indicator

---

## ML Model

We used a **Random Forest Classifier** to predict whether a pit stop will occur on the next lap based on current lap conditions.

### 🔧 Features Used
- Driver
- Lap Number
- Tyre Compound
- Tyre Life
- Lap Time

### Results

```text
Classification Report:
              precision    recall  f1-score   support

           0       0.98      1.00      0.99       183
           1       1.00      0.43      0.60         7

    accuracy                           0.98       190
   macro avg       0.99      0.71      0.79       190
weighted avg       0.98      0.98      0.97       190
