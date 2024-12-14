#!/bin/bash
#SBATCH --job-name=easyocr6      
#SBATCH --output=easyocr_6.out        
#SBATCH --error=easyocr_6.err        
#SBATCH --partition=jevans-gpu            
#SBATCH --gres=gpu:1                    
#SBATCH --mem=16G                        
#SBATCH --account=pi-jevans
    

#SBATCH --mail-user=yingrong@rcc.uchicago.edu 
#SBATCH --mail-type=BEGIN,END,FAIL      

# Load required modules (adjust as per your environment)
module load python/3.8                   # Load Python module (adjust version)
module load cuda/11.7                    # Load CUDA module (adjust version if needed)

# Activate your Python environment if applicable
source ~/myenv/bin/activate             # Replace `my_env` with your environment name

# Run the Python script
python extract_text.py             # Replace with the filename of your script