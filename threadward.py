import discord
import json

import cmd_handler

# load configuration file
with open('config.json') as config_file:
    CONFIG = json.load(config_file)

TOKEN = CONFIG['TOKEN']
PREFIX = CONFIG['PREFIX']
COMMANDS = CONFIG['COMMANDS']

# start client session
client = discord.Client()

@client.event
async def on_message(message):
    # prevent bot from replying to other bots, including itself
    if message.author.bot:
        return

    # extract command from message
    if message.content.startswith(PREFIX):
        command = message.content.split(' ')[0][len(PREFIX):]

    elif client.user.mentioned_in(message):
        command = 'help'

    else:
        return

    msg = cmd_handler.handle(command, COMMANDS)

    # only reply if user provides valid command
    if msg:
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)