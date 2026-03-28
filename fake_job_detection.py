# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
# Load dataset
df = pd.read_csv("fake_job_postings.csv")
# Show first 5 rows
print(df.head())
print(df.info())
print(df.isnull().sum())
# Fill missing text values with empty string
df.fillna("", inplace=True)
df["combined_text"] = df["title"] + " " + df["description"] + " " + df["requirements"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

X = vectorizer.fit_transform(df["combined_text"])
y = df["fraudulent"]   # Target column (0 = real, 1 = fake)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression(class_weight='balanced', max_iter=1000)

# Train model
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, classification_report

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Detailed Report
print(classification_report(y_test, y_pred))
def predict_job_post(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    
    if prediction[0] == 1:
        print("⚠ This job posting is FAKE")
    else:
        print("✅ This job posting is REAL")

# Example
predict_job_post("Earn 5000 dollars weekly from home with no experience required")

import pickle
# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save vectorizer
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
print("Model and Vectorizer saved successfully!")