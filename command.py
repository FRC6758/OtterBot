import asyncio


cmds = []


class Command:
    name = ""
    description = ""
    live = False

    def __init__(self, name, description):
        self.name = name
        self.description = description

    async def exec(self, client, message, args):
        print('(COMMAND) [Execution:Error] No execution handler for command {}'.format(self.name))
