import numpy as np


path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251130.csv"
output_path = "dataset-20251214.csv"

selected_headers= ['Time', 'Day_of_week', 'Age_band_of_driver', 'Vehicle_driver_relation', 'Driving_experience',
                    'Type_of_vehicle', 'Owner_of_vehicle', 'Area_accident_occured', 'Lanes_or_Medians',
                    'Road_allignment', 'Types_of_Junction', 'Road_surface_type', 'Road_surface_conditions',
                    'Light_conditions', 'Weather_conditions', 'Cause_of_accident']


# >0 - >7 out of 15 features are missing
MISSING_THRESHOLD_RATIOS = np.array([0, 0.1, 0.15, 0.2, 0.3, 0.35, 0.4, 0.5])

# Explicit missing marker
MISSING = "MISSING"

# Load the first row (headers) separately
with open(path, "r") as f:
    headers = f.readline().strip().split(",")

# Skip the first row (headers) using skiprows=1
data = np.genfromtxt(path, delimiter=",", dtype=str, skip_header=1)

print("Rows loaded:", data.shape[0])
print("Columns:", data.shape[1])

# Column index lookup
col_idx = {h: i for i, h in enumerate(headers)}

# Replace "NULL" and empty strings with np.nan
data[data == "NULL"] = MISSING
data[data == ""] = MISSING

# Count missing values per row
selected_matrix = np.vstack(
    [data[:, col_idx[h]] for h in selected_headers]
).T

for ratio in MISSING_THRESHOLD_RATIOS:
    threshold = int(len(selected_headers) * ratio)

    # Count missing per row
    missing_mask = selected_matrix == MISSING
    missing_per_row = np.sum(missing_mask, axis=1)

    bad_rows = missing_per_row > threshold
    filtered_data = data[~bad_rows]

    remaining_rows = filtered_data.shape[0]
    removed_rows = data.shape[0] - remaining_rows
    remaining_missing = np.sum(filtered_data == MISSING)
    
    print(f"Threshold ratio: {ratio:>4}")
    print(f"  Missing allowed per row: {threshold}")
    print(f"  Rows removed: {removed_rows}")
    print(f"  Rows remaining: {remaining_rows}")
    print(f"  Missing values remaining: {remaining_missing}\n")

