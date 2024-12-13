import json

# Load the JSON file (replace 'your_file.json' with the path to your JSON file)
with open('/scratch/midway3/yingrong/meme_submission.json', 'r') as f:
    data = json.load(f)

# Create a new dictionary where each entry's key is the 'id'
id_dict = {item['id']: item for item in data}

# Save the new dictionary into a new JSON file (optional)
with open('/scratch/midway3/yingrong/new_submission.json', 'w') as f:
    json.dump(id_dict, f, indent=4)

print("Rebuilt dictionary saved to 'rebuilt_data.json'")