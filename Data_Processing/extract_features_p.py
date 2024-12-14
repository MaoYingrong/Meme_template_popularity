from PIL import Image, UnidentifiedImageError
import numpy as np
import csv
import torch
from torchvision import transforms
import itertools
import os
from datetime import datetime
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "--order", type=int, help="Order of the images.")
args = parser.parse_args()

batch_size = 50000
start_index = args.order * batch_size
end_index = start_index + batch_size


time_0 = datetime.now()
# Load model
MODEL_PATH = 'resnet50.pth'
model = torch.load(MODEL_PATH)
model.eval()

# Preprocessing transforms
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_image(image_path):
    """Load and preprocess an image."""
    try:
        img = Image.open(image_path).convert('RGB')
        img_tensor = preprocess(img).unsqueeze(0)
        return img_tensor
    except:
        print(f"Error loading image: {image_path}")
        return None

def extract_features(image_path):
    """Extract features for an image."""
    img_tensor = load_image(image_path)
    if img_tensor is None:
        return None
    with torch.no_grad():
        feature = model(img_tensor).squeeze()
    return feature.cpu().numpy()

def main():
    input_file = "/scratch/midway3/yingrong/all_image_names.csv"
    feature_output_file = f"/scratch/midway3/yingrong/features_&_paths/features_{args.order}.npy"
    path_output_file = f"/scratch/midway3/yingrong/features_&_paths/paths_{args.order}.npy"

    # Load image paths
    image_paths = []
    with open(input_file, "r") as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in itertools.islice(reader, start_index, end_index):
            _, full_path = row
            image_paths.append(full_path)

    # Extract features for all images
    features, paths = [], []
    for path in image_paths:
        feature = extract_features(path)
        if feature is not None:
            features.append(feature)
            paths.append(path)

    # Save features and paths
    np.save(feature_output_file, np.array(features))
    np.save(path_output_file, np.array(paths))

    print(f"Features successfully written to {feature_output_file}")
    print(f"Paths successfully written to {path_output_file}")

    print(f"The time used to run is {datetime.now() - time_0}")

if __name__ == "__main__":
    main()