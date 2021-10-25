import os
import re
import json

import discord

from discord import message
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

config = json.load(open('config.json',))

async def print_help(message):
    keywords = ", ".join(config['wiki_introduction_links'])
    print(keywords)
    await message.reply(
        "Hi, I'm the IOTA-Wiki bot.\n" +
        "I was mainly created to remind you to use the god damn wiki. Just use the wiki and I'm your friend, ok?\n" +
        "But i can also give you a link to the introduction page of a certain documentation\n" +
        "Just mention me in your message and use one of the following keywords:\n" +
        keywords + "\n\n" +
        "Insider: You can also use the related emojis ;)"
    )


async def print_not_found_message(message):
    argsList = message.content.split(' ')[1::]
    arg = ' '.join(argsList)
    print(arg)
    await message.reply(
        f"Unable to find documentation for `{arg}`\n" 
    )


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(f'{message.content} got written on server')
    for key, value in config['wiki_links_map'].items():
        if key.lower() in message.content.lower():
            print('Wrong Wiki link used')
            text_after = re.sub(re.escape(key), value, message.content)
            await message.add_reaction(config["replacment_reaction"])
            await message.reply("Hi, it seems like you didn't use the wiki. Did you mean: " + text_after + " ?")
            return

    if client.user.mentioned_in(message):
        needed_help = False
        for key, value in config['wiki_introduction_links'].items():
            if key.lower() in message.content.lower():
                print('Wiki link requested')
                await message.add_reaction(config["help_reaction"])
                await message.reply("Hi!\n" + 
                    "It seems like you are searching for IOTA " + key + " documentation.\n" +
                    "Here you go: " + value + ".\n" +
                    "Happy BUIDLING!")
                needed_help = True


        if not needed_help and (("hi" in message.content.lower()) or ("help" in message.content.lower())):
            await print_help(message)
        else: 
            await print_not_found_message(message)

client.run(TOKEN)
