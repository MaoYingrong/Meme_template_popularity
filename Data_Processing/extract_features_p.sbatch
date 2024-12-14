#!/bin/bash

#SBATCH --job-name=extract_features

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=5G
#SBATCH --partition=caslake
#SBATCH --account=macs40123
#SBATCH --array=0-16             # 17 tasks
#SBATCH --output=logs/extract_features_%A_%a.out   # Standard output (A: Job ID, a: Array Task ID)
#SBATCH --error=logs/extract_features_%A_%a.err 

module load python/anaconda-2022.05 

python extract_features_p.py --order $SLURM_ARRAY_TASK_ID