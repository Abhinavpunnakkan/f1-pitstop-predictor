import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv('src/ml_dataset_monza_2023.csv')

# Select features and label
X = df[['Driver', 'LapNumber', 'Compound', 'TyreLife', 'LapTime']]
y = df['PitNextLap']

# One-hot encode categorical columns
X_encoded = pd.get_dummies(X, columns=['Driver', 'Compound'])

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("🏁 Classification Report:")
print(classification_report(y_test, y_pred))

print("🧱 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
