import csv
import json

# File paths (replace these with the actual file paths)
csv_file_path = '/scratch/midway3/yingrong/all_image_names.csv'  
json_file_path = '/scratch/midway3/yingrong/new_submission.json'  
output_file_path = '/scratch/midway3/yingrong/filtered_submission.json' 

with open(json_file_path, 'r') as f:
    data = json.load(f) 

found_data = {}
n = 0
# Open the CSV file and iterate over the file names
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if there's one
    
    for row in reader:
        n += 1
        file_name = row[1]  # Assuming the file names are in the second column
        file_key = file_name.split('/')[-1].replace('.jpg', '')

        if file_key in data:
            found_data[file_key] = data[file_key]  # Add the corresponding dictionary to found_data
        else:
            print(f"Key {file_key} not found in JSON data")

# Save the found data to a new JSON file
with open(output_file_path, 'w') as f:
    json.dump(found_data, f)

# print(f"Data for matching file names has been saved to {output_file_path}")
print(f"Stored {n} comments in total")