from command import Command
import asyncio


class CommandPing(Command):

    def __init__(self):
        super().__init__('ping', 'Sends PONG!')

    async def exec(self, client, message, args):
        await client.send_message(message.channel, 'Pong!')
