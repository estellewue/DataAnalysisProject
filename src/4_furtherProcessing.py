import numpy as np
import matplotlib.pyplot as plt


path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251214.csv"
output_path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251215.csv"
figure_path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/reports/figures/.pdf"

selected_headers= ['Time', 'Day_of_week', 'Age_band_of_driver', 'Vehicle_driver_relation', 'Driving_experience',
                    'Type_of_vehicle', 'Owner_of_vehicle', 'Area_accident_occured', 'Lanes_or_Medians',
                    'Road_allignment', 'Types_of_Junction', 'Road_surface_type', 'Road_surface_conditions',
                    'Light_conditions', 'Weather_conditions', 'Cause_of_accident']

with open(path, "r") as f:
    headers = f.readline().strip().split(",")

data = np.genfromtxt(path, delimiter=",", dtype=str, skip_header=1)

# Column index lookup
col_idx = {h: i for i, h in enumerate(headers)}

# Normalize categorical data
for h in headers:
    idx = col_idx[h]
    data[:, idx] = np.char.lower(
        np.char.strip(data[:, idx])
    )

# Transform time to hour only to make it easier to analyse
time_idx = col_idx['Time']

def extract_hour(t):
    try:
        return int(t.split(":")[0])
    except:
        return "MISSING"

hours = np.array([extract_hour(t) for t in data[:, time_idx]])
data[:, time_idx] = hours.astype(str)

data[data == "MISSING"] = "unknown"
data[data == "missing"] = "unknown"

# Normalize Age_band_of_driver and Driving_experience
# 1. get unique values 2. categorize 3. transform


np.savetxt(output_path, data, delimiter=",", fmt="%s", header=",".join(headers))
