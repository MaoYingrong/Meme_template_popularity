#!/bin/bash

#SBATCH --job-name=connect
#SBATCH --output=connect.out
#SBATCH --error=connect.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=40G
#SBATCH --partition=caslake
#SBATCH --account=macs40123


module load python/anaconda-2022.05 

python connect_comment.py