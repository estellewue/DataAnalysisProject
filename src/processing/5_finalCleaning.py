import numpy as np
import matplotlib.pyplot as plt


path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251215.csv"
output_path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/data/processed/dataset-20251215_2.csv"
figure_path = "/Users/marcelwillkommen/Coding/DataForAI/DataAnalysisProject/DataAnalysisProject/reports/figures/UpdatedRowsMissingFeatures.pdf"

selected_headers= ['Time', 'Day_of_week', 'Age_band_of_driver', 'Vehicle_driver_relation', 'Driving_experience',
                    'Type_of_vehicle', 'Owner_of_vehicle', 'Area_accident_occured', 'Lanes_or_Medians',
                    'Road_allignment', 'Types_of_Junction', 'Road_surface_type', 'Road_surface_conditions',
                    'Light_conditions', 'Weather_conditions', 'Cause_of_accident']

with open(path, "r") as f:
    headers = f.readline().strip().split(",")

headers[0] = headers[0][2:]

data = np.genfromtxt(path, delimiter=",", dtype=str, skip_header=1)

# Column index lookup
col_idx = {h: i for i, h in enumerate(headers)}

# >0 - >7 out of 15 features are missing
MISSING_THRESHOLD_RATIOS = np.array([0, 0.1, 0.15, 0.2, 0.3, 0.35, 0.4, 0.45])

# Explicit missing marker
MISSING = "unknown"

# Count missing values per row
selected_matrix = np.vstack(
    [data[:, col_idx[h]] for h in selected_headers]
).T

y = np.array([])

for ratio in MISSING_THRESHOLD_RATIOS:
    threshold = int(len(selected_headers) * ratio)

    # Count missing per row
    missing_mask = selected_matrix == MISSING
    missing_per_row = np.sum(missing_mask, axis=1)

    bad_rows = missing_per_row > threshold
    filtered_data = data[~bad_rows]

    remaining_rows = filtered_data.shape[0]
    removed_rows = data.shape[0] - remaining_rows
    
    y = np.append(y, removed_rows)

plt.plot(MISSING_THRESHOLD_RATIOS, y, marker='o', linestyle='-', color='blue', label='Values')

plt.xlabel('Threshold Ratios')
plt.ylabel('Rows')
plt.xticks(MISSING_THRESHOLD_RATIOS)  # show all x values
plt.grid(True)

plt.savefig(figure_path)
plt.show()

best_ratio = 0.2

threshold = int(len(selected_headers) * best_ratio)  
missing_mask = selected_matrix == MISSING
missing_per_row = np.sum(missing_mask, axis=1)

bad_rows = missing_per_row > threshold
filtered_data = data[~bad_rows]

remaining_rows = filtered_data.shape[0]
print(f"Rows remaining: {remaining_rows}")

removed_rows = data.shape[0] - remaining_rows
print(f"Rows removed: {removed_rows}")

# Create new csv
np.savetxt(output_path, filtered_data, delimiter=",", fmt="%s", header=",".join(headers))