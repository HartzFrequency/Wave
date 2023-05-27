from dotenv import dotenv_values
import discord
from discord import Intents

import Data.Messages.MessagesData as Messages

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Configure Discord client with intents
intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Wave is Started')


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the received message is a hello message
    if message.content.lower() in Messages.Hello_messages:
        Reply = Messages.HelloReply()
        await message.channel.send(Reply)

    # React to a specific message

    # Add a reaction if the message content is "wave"
    if message.content.lower() == 'wave':
        await message.add_reaction('👋')

    # Additional features

    # Help Command
    if message.content.lower() == '!help':
        help_message = "I am Wave Bot. Here are some available commands:\n" \
                       "`!hello` - Say hello to the bot\n" \
                       "`!help` - Show this help message"
        await message.channel.send(help_message)


client.run(env_vars['BotToken'])
