# Coherence
# A logical Discord chatbot by rhbarber98
# ------

import config

import discord

# Discord API User Token
# Do not edit this line directly. See readme for information on configuring your API token.

TOKEN = config.API_KEY

client = discord.Client()

@client.event
async def on_ready():
    print('Connected to Discord API')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Set Playing/Streaming Status of bot. Uncomment and change 'name' and 'status' to display on bot's profile.
# Only one line should be uncommented at any given time. Having both uncommented will not display the proper status on Discord.

# For "playing" status, uncomment this line:
    await client.change_presence(activity=discord.Game(name="!ping"), status=discord.Status("online"))
# For "streaming" status, uncomment this line:
#    await client.change_presence(activity=discord.Streaming(name="Twitch", url="https://www.twitch.tv"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Edit the 'startswith' and 'send' strings to include your own commands and responses. Copy and paste the code block below to add additional commands.

    if message.content.startswith('!ping'):
        await message.channel.send('Pong! Coherence is operational!')
        await message.delete()

# API Token Function required for connection to Discord API. Do NOT edit the below line.

client.run(TOKEN)

# End of file
