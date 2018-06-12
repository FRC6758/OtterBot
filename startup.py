import discord
import asyncio
import time
from command import cmds
from commands.ping import CommandPing
from commands.help import CommandHelp
from commands.otterpic import CommandOtterPic
from commands.subotterpic import CommandSubOtterPic
from commands.giveme import CommandGiveMe

config = {}

print('(LOADER) Reading configuration...')
with open('config.ini') as f:
    lines = f.readlines()
    for line in lines:
        parts = line.split('=')
        if len(parts) != 2:
            print('(LOADER) [Configuration:Error] Malformed configuration line: {}'.format(line))
            continue
        varname = parts[0]
        varvalue = parts[1]
        config[varname] = varvalue.rstrip('\n')
        print('(LOADER) [Configuration] Set configuration value of {}'.format(varname))


print('(LOADER) Initializing commands...')
client = discord.Client()
cmds.append(CommandHelp())
cmds.append(CommandPing())
cmds.append(CommandOtterPic())
cmds.append(CommandSubOtterPic())
cmds.append(CommandGiveMe())
print('(LOADER) Initialized {} commands'.format(len(cmds)))

@client.event
async def on_ready():
    game = discord.Game()
    game.name = "https://team6758.com"
    await client.change_presence(game=game)
    print('(DISCORD) [READY] {} ({})'.format(client.user.name, client.user.id))


def ctime():
    return int(round(time.time() * 1000))

@client.event
async def on_message(message):
    handler_bf = ctime()
    msg = message.content
    if not msg.startswith('!'):
        return
    if message.server is None:
        return
    args = msg.split()
    cmd = args[0]
    cmd = cmd[1:]
    args.pop(0)
    match = next((x for x in cmds if x.name.lower() == cmd.lower()), None)
    if match is None:
        print('(COMMAND) [Handler:Warning] No match for command {}'.format(cmd))
        return
    print('(COMMAND) [Handler] Beginning execution of command {}'.format(cmd))
    handler_af = ctime()
    await match.exec(client, message, args)
    exec_time = ctime()-handler_af
    handler_time = handler_af-handler_bf
    print('(COMMAND) [Handler] Successfully executed command {}. [Execution Time: {}ms; Handler Time: {}ms]'
          .format(cmd, exec_time, handler_time))

print(config)

client.run(config['BOT_TOKEN'])
