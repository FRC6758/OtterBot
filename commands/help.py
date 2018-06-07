from command import Command
import asyncio
from command import cmds


class CommandHelp(Command):

    def __init__(self):
        super().__init__('help', 'Shows a list of commands')

    async def exec(self, client, message, args):
        cmd_str = "**OtterBot Command List:**\n"
        for cmd in cmds:
            cmd_str += "\n`!{}` - {}".format(cmd.name, cmd.description)
        await client.send_message(message.channel, cmd_str)
