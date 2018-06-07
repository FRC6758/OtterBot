from command import Command
import asyncio
import os
import random


class CommandOtterPic(Command):

    def __init__(self):
        super().__init__('otterpic', 'Sends an amazing otter picture')

    async def exec(self, client, message, args):
        pics = os.listdir("res/otterpics")
        pic = random.choice(pics)
        await client.send_typing(message.channel)
        await client.send_file(message.channel, "res/otterpics/{}".format(pic), content=":heart_eyes:")
