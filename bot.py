import os
import re
import json

import discord

from discord import message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

config = json.load(open('config.json',))

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(f'{message.content} got written on server')
    for key, value in config['wiki_links_map'].items():
        if key in message.content:
            print('Wrong Wiki link used')
            text_after = re.sub(re.escape(key), value, message.content)
            await message.add_reaction(config["replacment_reaction"])
            await message.reply("Hi, it seems like you didn't use the wiki. Did you mean: " + text_after + " ?")
            return

    if client.user.mentioned_in(message):
        for key, value in config['wiki_introduction_links'].items():
            if key.lower() in message.content.lower():
                print('Wiki link requested')
                await message.add_reaction(config["help_reaction"])
                await message.reply("Hi!\n" + 
                    "Hmmm... It seems like you are searching for IOTA " + key + " documentation.\n" +
                    "Here you go: " + value + ".\n" +
                    "Happy BUIDLING!")

client.run(TOKEN)