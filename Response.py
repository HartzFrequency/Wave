# Import required modules
from dotenv import dotenv_values
import Data.MessagesData as Messages
import discord
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR)

# Set up discord intents
intents = discord.Intents.default()
intents.message_content = True

# Create a custom Discord client class
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        # Called when the bot is ready and connected to the server
        print('Wave is Started')

    async def on_message(self, message):
        try:
            # Ignore messages sent by the bot itself
            if message.author == self.user:
                return

            # Check if the received message is a hello message
            if message.content.lower() in Messages.Hello_messages:
                Reply = Messages.HelloReply()
                await message.channel.send(Reply)

            # Help Command
            if message.content.lower() == '!help':
                help_message = "I am Wave Bot. Here are some available commands:\n" \
                               "`!hello` - Say hello to the bot\n" \
                               "`!help` - Show this help message"
                await message.channel.send(help_message)

            # Add a reaction if the message content is "wave"
            if message.content.lower() == 'wave':
                await message.add_reaction('👋')

            # Reaction On cool
            if message.content.lower() == 'cool':
                await message.add_reaction('\U0001F60E')

            # Reply Of Middle Finger in chats
            if message.content == '\U0001F595':
                await message.add_reaction('\U0001F92C')

        except Exception as e:
            logging.exception("Error processing message:", exc_info=e)

    async def on_message_edit(self, before, after):
        try:
            # Message Edit log
            if before.content != after.content:
                await before.channel.send(
                    f'>>> '
                    f'{before.author} edit a message. \n'
                    f'Before: {before.content}\n'
                    f'After: {after.content}'
                )

        except Exception as e:
            logging.exception("Error processing message edit:", exc_info=e)

    async def on_reaction_add(self, reaction, user):
        try:
            if reaction.emoji == '\U0001F595':
                await reaction.message.channel.send(f'Fuck You {user}')

            # Reaction logs
            # Preventing to give self reaction logs
            if user == self.user:
                pass
            else:
                await reaction.message.channel.send(
                    f'>>> '
                    f'{user} reacted with {reaction.emoji}'
                )

        except Exception as e:
            logging.exception("Error processing reaction add:", exc_info=e)


# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Create an instance of the custom client class and run the bot
client = MyClient(intents=intents)
try:
    client.run(env_vars['BotToken'])
except Exception as e:
    logging.exception("Error running the bot:", exc_info=e)
