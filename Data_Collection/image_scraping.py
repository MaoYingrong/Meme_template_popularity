import json
import aiohttp
import asyncio
from datetime import datetime

with open('/meme_submission.json') as f:
    large_data = json.load(f)

count = 0
n = 0
start_time = datetime.now()

# Headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Directory to save images
output_dir = "/Images"

# Function to download a single image
async def download_image(session, item):
    global count, n
    n += 1
    print(n)

    try:
        if item["url"].endswith(".png") or item["url"].endswith(".jpg"):
            async with session.get(item["url"], headers=headers, timeout=5000) as response:
                if response.status == 200:
                    image_name = f"{output_dir}/{item['id']}.jpg"
                    with open(image_name, 'wb') as f:
                        f.write(await response.read())
                    count += 1
                else:
                    print(f"Failed to download image {item['id']}. Status code: {response.status}")
                    print(f"URL: {item['url']}")
    except Exception as e:
        print(f"Failed to download image. Exception: {e}")

# Function to handle multiple image downloads concurrently
async def download_images(large_data):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for item in large_data:
            tasks.append(download_image(session, item))
        await asyncio.gather(*tasks)

# Running the download process
async def main():
    await download_images(large_data)

if __name__ == '__main__':
    asyncio.run(main())

end_time = datetime.now()
print(f"Downloaded {count} images")
print(f"Time taken: {end_time - start_time} seconds")
