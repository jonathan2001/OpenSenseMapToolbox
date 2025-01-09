import os
import pandas as pd
from pathlib import Path

# Define the root directory where the device folders are located
root_dir = "./data"  # Replace with the path to your data directory

# Initialize an empty list to store DataFrames
data_frames = []

# Iterate over all folders in the root directory
for device_folder in os.listdir(root_dir):
    device_path = os.path.join(root_dir, device_folder)
    
    # Check if it is a directory
    if os.path.isdir(device_path):
        csv_path = os.path.join(device_path, "data.csv")
        
        # Check if the data.csv file exists
        if os.path.exists(csv_path):
            # Load the CSV into a DataFrame
            df = pd.read_csv(csv_path)
            
            # Add a column for the device ID
            df["device_id"] = device_folder
            
            # Extract latitude and longitude from the 'geometry' column
            df[["lng", "lat"]] = df["geometry"].str.extract(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)')
            
            # Append the DataFrame to the list
            data_frames.append(df)

# Combine all DataFrames into a single DataFrame
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined DataFrame to a CSV file
output_path = "./combined_data.csv"  # Replace with your desired output path
combined_df.to_csv(output_path, index=False)

print(f"Combined CSV saved to {output_path}")
