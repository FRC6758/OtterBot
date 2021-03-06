from command import Command
import asyncio
import discord


class CommandSubOtterPic(Command):

    def __init__(self):
        super().__init__('subotterpic', 'Submits an otter pic for !otterpic [Team members only]')

    async def exec(self, client, message, args):
        if message.channel.id != '455913875217448971':
            await client.send_message(message.channel, 'This command can only be used in <#455913875217448971>')
            return
        em = discord.Embed(title="Otter Picture Submission")
        em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        if len(message.attachments) != 1:
            await client.send_message(message.channel, "An image attachment is required.")
            return
        em.set_image(url=message.attachments[0]['proxy_url'])
        await client.send_typing(message.channel)
        mess = await client.send_message(message.channel, embed=em)
        await client.add_reaction(mess, '👍')
        await client.add_reaction(mess, '👎')
        await client.delete_message(message)
