import pandas as pd
import joblib

model = joblib.load("accident_severity_key_features.joblib")

new_data = pd.read_csv("new_accident_data.csv")
predictions = model.predict(new_data)

new_data["Predicted_Accident_severity"] = predictions
new_data.to_csv("predictions.csv", index=False)

print("Predictions saved to predictions.csv")
