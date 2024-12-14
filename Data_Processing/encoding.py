import pandas as pd
import numpy as np
from datetime import datetime
import torch
from sentence_transformers import SentenceTransformer


print(torch.cuda.is_available()) 
print(torch.cuda.device_count())  


time_0 = datetime.now()
# Load model and move it to GPU
model = SentenceTransformer('flax-sentence-embeddings/reddit_single-context_mpnet-base', device='cuda')

with open("meme_table_title&extracted.csv", "r") as file:
    meme_df = pd.read_csv(file)

# Prepare your combined_text as a list
texts = meme_df["combined_text"].tolist()
# Encode in batches
embeddings = model.encode(texts, batch_size=32, show_progress_bar=True)
meme_df["embedding"] = embeddings.tolist()

print(meme_df.head())
print(f"time used: {datetime.now()-time_0}")

# store it into a new csv file
meme_df.to_csv("redditST_title&extracted_encoded.csv", index=False)