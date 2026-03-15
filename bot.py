import discord
import os
import random
import gdown
from discord.ext import tasks
from datetime import time

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1475585161876738272

DRIVE_FOLDERS = [
"https://drive.google.com/drive/folders/1qMw9LNtHU5-kwIink9tykVw8EaGrFgNg?usp=sharing",
"https://drive.google.com/drive/folders/1WDimEvfvBNh7qRIZpV8ZLwWyxbwCE8Qt?usp=sharing",
"https://drive.google.com/drive/folders/19omJ7QsNsn3PXnxLIlQylYWfEGRcWb4p?usp=sharing",
"https://drive.google.com/drive/folders/1GT8x6uqHwtE4Z1AEvtxLHDVwptDbYr9P?usp=sharing",
"https://drive.google.com/drive/folders/1hG1IJyU1bnTKQYZyCklA38b857VhYlt_?usp=sharing"
]

DOWNLOAD_FOLDER = "videos"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def download_videos():

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    for folder in DRIVE_FOLDERS:
        gdown.download_folder(
    folder,
    output=DOWNLOAD_FOLDER,
    quiet=True,
    use_cookies=False
)


async def post_videos():

    channel = client.get_channel(CHANNEL_ID)

    videos = [v for v in os.listdir(DOWNLOAD_FOLDER) if v.endswith((".mp4",".mov"))]

    selected = random.sample(videos, min(6, len(videos)))

    for video in selected:

        await channel.send(file=discord.File(f"{DOWNLOAD_FOLDER}/{video}"))


@tasks.loop(seconds=60)
async def daily_post():

    await download_videos(import shutil

if os.path.exists(DOWNLOAD_FOLDER):
    shutil.rmtree(DOWNLOAD_FOLDER)

os.makedirs(DOWNLOAD_FOLDER))
    await post_videos()


@client.event
async def on_ready():

    print("Bot online")
    daily_post.start()


client.run(TOKEN)
