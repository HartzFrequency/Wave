from dotenv import dotenv_values
import Data.Messages.MessagesData as Messages

import discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
env_vars = dotenv_values('.env')


@client.event
async def on_ready():
    print('Wave is Started')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if message.content.lower() in Messages.Hello_messages:
        Reply=Messages.HelloReply()
        await message.channel.send(Reply)    

    
client.run(env_vars['BotToken'])
