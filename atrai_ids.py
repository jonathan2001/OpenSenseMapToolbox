import requests
import json

# List of grouptags to query
grouptags = ["atrai", "ATRAI"]  # Add as many tags as needed
output_file = "sensebox_ids.txt"

# Set to store unique IDs
unique_ids = set()

# Iterate over each grouptag
for tag in grouptags:
    url = f"https://api.opensensemap.org/boxes?grouptag={tag}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract IDs from the returned data
        for box in data:
            if "_id" in box:
                unique_ids.add(box["_id"])

        print(f"Fetched {len(data)} boxes for grouptag '{tag}'")
    except requests.RequestException as e:
        print(f"Error fetching data for grouptag '{tag}': {e}")

# Write unique IDs to the output file
with open(output_file, "w") as file:
    for unique_id in unique_ids:
        file.write(f"{unique_id}\n")

print(f"Saved {len(unique_ids)} unique senseBox IDs to '{output_file}'")