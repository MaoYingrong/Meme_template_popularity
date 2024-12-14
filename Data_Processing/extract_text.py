import torch
print(torch.cuda.is_available()) 

import easyocr
import os
from datetime import datetime
import json

new_dic = {}
base_path = "/scratch/midway3/yingrong/MEME_data/meme_data/image_meme/"

time_0 = datetime.now()
def run_easyocr(image_path):
    # Initialize EasyOCR reader with GPU
    reader = easyocr.Reader(['en'], gpu=True)  # Add other languages if needed
    results = reader.readtext(image_path)

    # Extract text
    extracted_text = " ".join([result[1] for result in results])
    return extracted_text


file = "/home/yingrong/meme_project/time_series/templated_meme.json"
with open(file, "r") as json_file:
    data = json.load(json_file)

# Create an empty list to store all paths
all_paths = []

# Iterate through each cluster and extract paths
for cluster in data:
    for key, paths in cluster.items():
        if len(paths) > 100:
            all_paths.extend(paths)

print(f"The length of all_paths is {len(all_paths)}")

current_list = all_paths[60000:70000]

for target_path in current_list:
    folder_name, file_name = os.path.split(target_path)
    parent_folder_name = os.path.basename(folder_name)
    file_path = base_path + parent_folder_name + "/" + file_name
    
    key = file_name.replace(".jpg","")
    text = run_easyocr(file_path)
    new_dic[key] = text



output_path = "extracted_text_6.json"

with open(output_path, "w") as json_file:
    json.dump(new_dic, json_file, indent=4)

print(f"The time used to run is {datetime.now() - time_0}")
# for k, v in new_dic.items():
#     print(k)
#     print(v)