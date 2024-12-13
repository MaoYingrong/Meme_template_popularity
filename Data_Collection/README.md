Data Collection Process:
1. Download reddit data from [Academic Torrents](https://academictorrents.com/details/9c263fc85366c1ef8f5bb9da0203f4c8c8db75f4)(although it shows 2.64TB, the .torrent file should only be 8.8MB)
2. Download software [Tranmission](https://transmissionbt.com/)
3. Use Transmission to select the subreddit data you want (submission and comments are separate) and download it. The downloaded files usually are jsonl files.
4. Use [images_scraping.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/images_scraping.py) to scrape all available image data.
5. Use [images_names.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/images_names.py) to store all names of images downloaded (image names are posts ID)
6. Use [change_structure.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/change_structure.py) to make the original submission file (list of dictionaries) become a dictionary of dictionaries, in which keys are the posts ID.
7. Use [filter_post.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/filter_post.py) to filter all the posts with images downloaded, based on the image names.   

Other files:
- [filter_comments.py](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/filter_comments.py): based on the filtered posts, get all comments under those posts.
- [sbatch_file.sbatch](https://github.com/MaoYingrong/MEMEs_culture_evolution/blob/main/Data_Collection/sbatch_file.sbatch): use to execute the programs running in Midway HPC
