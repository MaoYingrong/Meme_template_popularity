#!/bin/bash
#SBATCH --job-name=encoding      
#SBATCH --output=encoding.out        
#SBATCH --error=encoding.err        
#SBATCH --partition=ssd-gpu            
#SBATCH --gres=gpu:1                    
#SBATCH --mem=32G                        
#SBATCH --account=ssd
#SBATCH --qos=ssd
    

#SBATCH --mail-user=yingrong@rcc.uchicago.edu 
#SBATCH --mail-type=BEGIN,END,FAIL      

# Load required modules (adjust as per your environment)
module load python/3.8  
module load cuda/11.7                    # Load CUDA module (adjust version if needed)

source ~/myenv/bin/activate

# Run the Python script
python encoding.py             # Replace with the filename of your script