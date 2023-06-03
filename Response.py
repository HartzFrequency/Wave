from dotenv import dotenv_values
import Data.MessagesData as Messages

import discord
intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Wave is Started')

    async def on_message(self, message):
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

    async def on_message_edit(self, before, after):
        # Message Edit log
        if before.content != after.content:
            await before.channel.send(
                f'>>> '
                f'{before.author} edit a message. \n'
                f'Before: {before.content}\n'
                f'After: {after.content}'
            )

    async def on_reaction_add(self, reaction, user):
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


env_vars = dotenv_values('.env')
client = MyClient(intents=intents)
client.run(env_vars['BotToken'])
