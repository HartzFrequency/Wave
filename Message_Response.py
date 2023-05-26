from dotenv import dotenv_values
import Data.Messages.MessagesMethod as Messages
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
    Hello_messages = ["hello","hola","hi","hey","hey yo","hey there","howdy","yo","bonjour","ciao","namaste"]
    if message.author == client.user:
        return

    if message.content.lower() in Hello_messages:
        await message.channel.send("Hey there! What's up?")    

    
client.run(env_vars['BotToken'])
