from command import Command
import asyncio


def userHasRole(user, id):
    for rle in user.roles:
        if rle.id == id:
            return True
    return False


def getRoleFromGuild(guild, id):
    for rle in guild.roles:
        if rle.id == id:
            return rle
    return None

class CommandGiveMe(Command):

    def __init__(self):
        super().__init__('giveme', 'Gives you a role, assuming you\'re a member.')

    async def exec(self, client, message, args):
        if not userHasRole(message.author, '418523867930165248'):
            return
        switcher = {
            "programming": lambda: '418828271174680589',
            "media": lambda: '418828399868641301',
            "mechanical": lambda: '418828557771472917',
            "electrical": lambda: '418828597902573590',
            "pneumatics": lambda: '455926161336303627'
        }
        supported = ''
        for role in switcher.keys():
            supported += ', `{}`'.format(role)
        supported = supported[2:]
        if len(args) != 1:
            await client.send_message(message.channel, 'The currently supported roles are: {}'.format(supported))
            return
        role = switcher.get(args[0].lower(), lambda: '-1')()
        if role == '-1':
            await client.send_message(message.channel, 'Invalid role. The currently supported roles are: {}'.format(supported))
            return
        await client.add_roles(message.author, getRoleFromGuild(message.server, role))
        await client.send_message(message.channel, 'Done!')
