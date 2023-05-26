import Data.Messages.MessagesMethod as Messages
import discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

Hello_messages = ["hello","hola","hi","hey","hey yo","hey there","howdy","yo","bonjour","ciao","namaste"]

@client.event
async def on_ready():
    print('Frequency is Started')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() in Hello_messages:
        await message.channel.send("Hey there! What's up?")    

    
client.run('MTEwODg1NjM2NjE5OTc1NDc4Mg.GyRpZV.N5LXkfvxyEoTQEakuwOZJQxNUYQoWleEe3lpfo')
