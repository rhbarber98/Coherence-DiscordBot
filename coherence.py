# Coherence
# ------
# A Discord chatbot by rhbarber98

import discord

# Discord API User Token

TOKEN = 'Insert your bot token from the Discord Developers Portal here'

client = discord.Client()

@client.event
async def on_ready():
    print('Connected to Discord API')
    prunt('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Set Game/Streaming Status of bot. Uncomment and change name and active status to display on bot's profile.

#    await client.change_presence(activity=discord.Game(name="?ping"), status=discord.Status("online"))
#    await client.change_presence(activity=discord.Streaming(name="JetMech", url="https://www.twitch.tv/jetmech"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Edit the 'startswith' and 'send' strings to include your own commands and responses. Copy and paste the code block below to add more commands.

    if message.content.startswith('?ping'):
        await message.channel.send('Pong! Bot is operational.')
        await message.delete()

# API Token Variable. Do NOT edit the below line.

client.run(TOKEN)

# End of file
