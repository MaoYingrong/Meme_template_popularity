import csv
import json

# File paths (replace these with the actual file paths)
csv_file_path = '/scratch/midway3/yingrong/all_image_names.csv'  
json_file_path = '/scratch/midway3/yingrong/meme_comments.json'  
output_file_path = '/scratch/midway3/yingrong/filtered_comments.json' 


found_data = {}

# Open the CSV file and iterate over the file names
with open(csv_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if there's one
    
    for row in reader:
        file_name = row[1]  # Assuming the file names are in the second column
        file_key = file_name.split('/')[-1].replace('.jpg', '')
        found_data[file_key] = []

with open(json_file_path, 'r') as f:
    data = json.load(f)
    num = 0
    for i in data:
        k = i["link_id"].replace('t3_', '')
        if k in found_data:
            buffer_dic = {i["id"]:i}
            found_data[k].append(buffer_dic)
            num += 1


# Save the found data to a new JSON file
with open(output_file_path, 'w') as f:
    json.dump(found_data, f)

# print(f"Data for matching file names has been saved to {output_file_path}")
print(f"Stored {num} comments in total")