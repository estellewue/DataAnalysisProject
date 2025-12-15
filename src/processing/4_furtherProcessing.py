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

# Normalize Age_band_of_driver
# 1. get unique values 2. categorize 3. transform
column_name = "Age_band_of_driver"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

age_group_map = {
    "under 18": "minor",
    "18-30": "young",
    "31-50": "adult",
    "over 51": "senior",
    "unknown": "unknown"
}

data[:, col_index] = np.vectorize(
    lambda x: age_group_map.get(x, "unknown")
)(data[:, col_index])

# Normalize Driving_experience
column_name = "Driving_experience"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

driving_exp_map = {
    "below 1yr": "novice",
    "1-2yr": "junior",
    "2-5yr": "intermediate",
    "5-10yr": "experienced",
    "above 10yr": "veteran",
    "no licence": "unlicensed",
    "unknown": "unknown"
}

data[:, col_index] = np.vectorize(
    lambda x: driving_exp_map.get(x, "unknown")
)(data[:, col_index])

# Service_year_of_vehicle

column_name = "Service_year_of_vehicle"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

vehicle_service_map = {
    "below 1yr": "new",
    "1-2yr": "recent",
    "2-5yrs": "used",
    "5-10yrs": "old",
    "above 10yr": "aged",
    "unknown": "unknown"
}

service_idx = col_idx["Service_year_of_vehicle"]

data[:, service_idx] = np.vectorize(
    lambda x: vehicle_service_map.get(x, "unknown")
)(data[:, service_idx])

# Type_of_vehicle
column_name = "Type_of_vehicle"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

vehicle_type_map = {
    "automobile": "car",
    "stationwagen": "car",
    "taxi": "car",
    "bajaj": "threewheeler",
    "motorcycle": "motorcycle",
    "bicycle": "bicycle",
    "ridden horse": "horse",
    "pick up upto 10q": "pickup",
    "long lorry": "truck",
    "lorry (11?40q)": "truck",
    "lorry (41?100q)": "truck",
    "public (12 seats)": "bus",
    "public (13?45 seats)": "bus",
    "public (> 45 seats)": "bus",
    "special vehicle": "special",
    "turbo": "special",
    "other": "other",
    "unknown": "unknown"
}

vehicle_idx = col_idx["Type_of_vehicle"]

data[:, vehicle_idx] = np.vectorize(
    lambda x: vehicle_type_map.get(x, "other")
)(data[:, vehicle_idx])

# Lanes_or_Medians
column_name = "Lanes_or_Medians"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

lanes_medians_map = {
    "one way": "oneway",
    "undivided two way": "undivided",
    "two-way (divided with broken lines road marking)": "twoway broken lines",
    "two-way (divided with solid lines road marking)": "twoway solid lines",
    "double carriageway (median)": "double carriageway",
    "other": "other",
    "unknown": "unknown"
}

lanes_idx = col_idx["Lanes_or_Medians"]

data[:, lanes_idx] = np.vectorize(
    lambda x: lanes_medians_map.get(x, "unknown")
)(data[:, lanes_idx])

# Age_band_of_casualty
column_name = "Age_band_of_casualty"
col_index = col_idx[column_name]

unique_values = np.unique(data[:, col_index])
print(unique_values)

age_group_map = {
    "under 18": "minor",
    "5": "minor",
    "18-30": "young",
    "31-50": "adult",
    "over 51": "senior",
    "unknown": "unknown"
}

data[:, col_index] = np.vectorize(
    lambda x: age_group_map.get(x, "unknown")
)(data[:, col_index])

np.savetxt(output_path, data, delimiter=",", fmt="%s", header=",".join(headers))
