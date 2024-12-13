import os
import csv

# List of subfolders
subfolders = [
    "images_0_199",
    "images_200_399",
    "images_400_599",
    "images_600_799",
    "images_800_999",
    "images_1000_1199",
    "images_1200_end"
]

# Set the base directory (modify this to match your path)
base_dir = "/scratch/midway3/yingrong"

# Output file path for the single CSV file
output_csv = "/scratch/midway3/yingrong/all_image_names.csv"

total_files = 0

# Open the CSV file for writing
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Subfolder", "File Name"])  # CSV header

    # Loop through each subfolder and collect file names
    for subfolder in subfolders:
        folder_path = os.path.join(base_dir, subfolder)
        
        # List all files in the subfolder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                total_files += 1
                full_path = os.path.join(root, file)
                writer.writerow([subfolder, full_path])  # Write subfolder and file name

        print(f"Collected file names from {subfolder}")

print(f"All file names stored in {output_csv}")
print(f"Total number of files: {total_files}")