import discord
import json
import os
import re

from discord import message
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

config = json.load(open('config.json',))

async def print_help(message):
    keywords = ", ".join(config['wiki_introduction_links'])
    print(keywords)
    await message.reply(
        "Hi, I'm the IOTA-Wiki bot.\n" +
        "I was mainly created to gently remind you to use the IOTA Wiki <https://wiki.iota.org>.\n" +
        "I can help you with the following:\n" +
        "**Introduction Links:** I will suggest links to the introduction page of a certain documentation.\n" +
        "Just mention me in your message and use one of the following keywords:\n`" +
        keywords + "`\n\n" +
        "Insider: You can also use the related emojis ;)\n" + 
        "\n" +
        "**Wiki Search:** Let me search the wiki for you.\n" +
        "Just mention me with the keywords `search` or `search for`\n" +
        "and I will provide you with a link to the search results."
    )


async def print_not_found_message(message):
    argsList = message.content.split(' ')[1::]
    arg = ' '.join(argsList)
    print(arg)
    await message.reply(
        f"Unable to find documentation for `{arg}`\n" 
    )

async def  print_query_result(message, query):
    await message.reply(
        "Hi,\n" +
        "It seems you are searching for `" + query + "`.\n" +
        "Let me help you out my friend. Here your result:\n" +
        "<https://wiki.iota.org/search?q=" + quote(query) + ">\n"
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
        query = re.search("(?<=search for ).*", message.content.lower()) or re.search("(?<=search ).*", message.content.lower())
        if query:
            print('Wiki search requested')
            await print_query_result(message, query[0])
            return

        introduction_found = False
        for key, value in config['wiki_introduction_links'].items():
            if key.lower() in message.content.lower():
                print('Wiki link requested')
                await message.add_reaction(config["help_reaction"])
                await message.reply("Hi!\n" + 
                    "It seems like you are searching for IOTA " + key + " documentation.\n" +
                    "Here you go: " + value + ".\n" +
                    "Happy BUIDLING!")
                introduction_found = True
        if introduction_found:
            return

        if (len(message.content.split(' ')) <= 1) or ("hi" or "help" in message.content.lower()):
            await print_help(message)
        else: 
            await print_not_found_message(message)

client.run(TOKEN)
