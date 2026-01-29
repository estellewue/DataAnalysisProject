import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import joblib

# =========================
# Load data
# =========================
df = pd.read_csv("/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251215_2.csv")

TARGET = "Accident_severity"

selected_headers = [
    'Time',
    'Day_of_week',
    'Age_band_of_driver',
    'Vehicle_driver_relation',
    'Driving_experience',
    'Type_of_vehicle',
    'Owner_of_vehicle',
    'Area_accident_occured',
    'Lanes_or_Medians',
    'Road_allignment',
    'Types_of_Junction',
    'Road_surface_type',
    'Road_surface_conditions',
    'Light_conditions',
    'Weather_conditions',
    'Cause_of_accident'
]

X = df[selected_headers]
y = df[TARGET]

# =========================
# Train/Test split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# Preprocessing (categorical only)
# =========================
categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", categorical_pipeline, selected_headers)
    ]
)

# =========================
# Model
# =========================
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

pipeline = Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("model", model)
])

# =========================
# Train
# =========================
pipeline.fit(X_train, y_train)

# =========================
# Evaluate
# =========================
y_pred = pipeline.predict(X_test)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# =========================
# Save model
# =========================
joblib.dump(pipeline, "accident_severity_key_features.joblib")
print("\nModel saved as accident_severity_key_features.joblib")
