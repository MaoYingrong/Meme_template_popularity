#!/bin/bash

#SBATCH --job-name=hdbscan

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=3G
#SBATCH --partition=caslake
#SBATCH --account=macs40123
#SBATCH --array=0-17             # 17 tasks
#SBATCH --output=hdbscan_%A_%a.out   # Standard output (A: Job ID, a: Array Task ID)
#SBATCH --error=hdbscan_%A_%a.err 

module load python/anaconda-2022.05 

python hds_trial_p.py --order $SLURM_ARRAY_TASK_ID