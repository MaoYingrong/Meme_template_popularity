# Content Diversity and Popularity Trends: Investigating Meme Templates as Evolving Communication Genres

**Introduction**
* This study examines the dynamics of internet meme templates as evolving communication genres, focusing on the relationship between content diversity and popularity trends. Using nearly 900,000 user-generated memes from a major subreddit, it investigates how content diversity—measured through textual embeddings and clustering—affects the longevity and temporal dynamics of meme popularity. The research employs advanced computational methods like HDBSCAN clustering, sentence embeddings, ARIMAX models, and Granger causality tests to analyze the temporal interplay between content diversity and popularity. Findings reveal that higher content diversity slows popularity decay, highlighting versatility as a key factor in cultural engagement. However, mixed causality results suggest the influence of other factors, such as contextual relevance and emotional resonance. This work bridges theoretical insights with empirical data, emphasizing memes as dynamic, evolving structures that play a significant role in digital culture.

**Data**:    
  * All posts (2008/12 - 2023/12) from a subreddit called “meme”, which is the earliest and the second largest meme community in Reddit with more than 2.6 million members. Each data point includes the title, meme image, description, posting time, upvote number, upvote ratio, author ID, and comments.
  * Details:
    * Number of original posts: 1,508,474; Number of posts with images downloaded: 896,449.
    * Number of images grouped into template clusters: 195,576. 
   
**Methods**:  
  * Data Collection  
    * Based on the metadata obtained from Academic Torrents, download the corresponding image of each post, delete the empty pages (the post was deleted), select the content with .jpg or .png formats, and select corresponding submissions info and comments info.
  * Data Processing
    * Use a pre-trained neural network (Resnet50) to extract features of all images, then use HDBSCAN clustering methods to group meme images based on whether they’re using the same template.
    * Use a pre-trained OCR model to extract text from meme images.
    * Use a pre-trained sentence embedding ([reddit_single-context_mpnet-base](https://huggingface.co/flax-sentence-embeddings/reddit_single-context_mpnet-base)) model to embed extracted text and post title for each meme. 
  * Data Analysis
    * Relationship between the overall content diversity of meme templates and the decay time of their popularity trends. 
    * ARIMAX analysis. 
    * Granger Causality Test.

