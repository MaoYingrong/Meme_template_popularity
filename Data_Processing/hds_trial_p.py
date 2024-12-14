import numpy as np
from datetime import datetime
import json
import csv
import itertools
import time
from collections import defaultdict
import hdbscan 
from sklearn.decomposition import PCA
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "--order", type=int, help="Order of the images.")
args = parser.parse_args()

INPUT_FILE_1 = f"/scratch/midway3/yingrong/features_&_paths/features_{args.order}.npy"
INPUT_FILE_2 = f"/scratch/midway3/yingrong/features_&_paths/paths_{args.order}.npy"
OUTPUT_FILE = f"/scratch/midway3/yingrong/trial/hdbscan_{args.order}.json"

print("Description")
print(f"The data is read from {INPUT_FILE_1}; First use PCA 500 and then uses HDBSCAN to cluster. The results file is {OUTPUT_FILE}/n")



time_0 = datetime.now()

def clustering_hdbscan(features_array, paths_array):
    real_clusters = defaultdict(list)
    pca = PCA(n_components=500)
    reduced_features = pca.fit_transform(features_array)

    time_2 = datetime.now()
    cluterer = hdbscan.HDBSCAN(min_cluster_size=2, metric='euclidean', cluster_selection_method='leaf')
    labels = cluterer.fit_predict(reduced_features)
    print(f"the time used to do hdbscan clustering: {datetime.now()-time_2}")

    for idx, label in enumerate(labels):
        if label != -1:
            real_clusters[label].append(paths_array[idx])

    return real_clusters


def print_and_save(clusters, output_file):
    clusters_list = []
    num_cluster = 0
    num_images = 0
    max_cluster = 0
    for cluster_key, images in clusters.items():
        if len(images) > 1:
        # if len(images) > 2:
            clusters_list.append({f"cluster_{cluster_key}": images})
            num_cluster += 1
            num_images += len(images)
            if len(images) >= max_cluster:
                max_cluster = len(images)
    
    print(f"The total number of clusters is {num_cluster}")
    print(f"The total number of images is {num_images}")
    print(f"The cluster with maximum number of images is {max_cluster}")

    # Save to a JSON file
    with open(output_file, "w") as json_file:
        json.dump(clusters_list, json_file, indent=4)


def main():
    # Path to the folder containing images
    features_array = np.load(INPUT_FILE_1)
    paths_array = np.load(INPUT_FILE_2)

    real_clusters = clustering_hdbscan(features_array, paths_array)
    print_and_save(real_clusters, OUTPUT_FILE)

    print(f"Total time taken: {datetime.now() - time_0}")

if __name__ == "__main__":
    main()