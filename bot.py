import discord
import os
import random
import gdown
from discord.ext import tasks
from datetime import time

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1475585161876738272

DRIVE_FOLDER = "https://drive.google.com/drive/folders/1Xry7zBispB-ZbNS2lx88bqMh-oCcuxdr?usp=sharing"

DOWNLOAD_FOLDER = "videos"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


async def download_videos():

    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    gdown.download_folder(DRIVE_FOLDER, output=DOWNLOAD_FOLDER, quiet=True)


async def post_videos():

    channel = client.get_channel(CHANNEL_ID)

    videos = os.listdir(DOWNLOAD_FOLDER)

    selected = random.sample(videos, 6)

    for video in selected:

        await channel.send(file=discord.File(f"{DOWNLOAD_FOLDER}/{video}"))


@tasks.loop(time=time(hour=20, minute=0))
async def daily_post():

    await download_videos()
    await post_videos()


@client.event
async def on_ready():

    print("Bot online")
    daily_post.start()


client.run(TOKEN)
