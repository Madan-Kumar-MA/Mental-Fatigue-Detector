import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Simulated dataset (randomly generated for demo purposes)
# In a real project, use actual keystroke data
X = np.array([
    [0.12, 2.0],  # Not fatigued
    [0.11, 2.5],
    [0.30, 1.0],  # Fatigued
    [0.28, 0.8],
    [0.15, 1.9],
    [0.31, 0.9],
    [0.10, 2.6],
    [0.33, 0.7],
])
y = [0, 0, 1, 1, 0, 1, 0, 1]  # 0 = Not Fatigued, 1 = Fatigued

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

model = RandomForestClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))

joblib.dump(model, "fatigue_model.joblib")
