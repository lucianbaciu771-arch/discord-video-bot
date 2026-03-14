import discord
import os
import random
from discord.ext import tasks
from datetime import time

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1475585161876738272

VIDEO_FOLDER = "videos"
POSTED_FILE = "posted_videos.txt"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


def get_posted():
    if not os.path.exists(POSTED_FILE):
        return []
    with open(POSTED_FILE, "r") as f:
        return f.read().splitlines()


def save_posted(video):
    with open(POSTED_FILE, "a") as f:
        f.write(video + "\n")


async def post_videos():

    channel = client.get_channel(CHANNEL_ID)

    videos = os.listdir(VIDEO_FOLDER)
    posted = get_posted()

    available = [v for v in videos if v not in posted]

    if len(available) < 6:
        print("Not enough new videos")
        return

    selected = random.sample(available, 6)

    for video in selected:

        await channel.send(file=discord.File(f"{VIDEO_FOLDER}/{video}"))

        save_posted(video)

        await discord.utils.sleep_until(discord.utils.utcnow())


@tasks.loop(time=time(hour=20, minute=0))
async def daily_videos():
    await post_videos()


@client.event
async def on_ready():
    print(f"Bot online: {client.user}")
    daily_videos.start()


client.run(TOKEN)