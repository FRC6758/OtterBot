from command import Command
import asyncio
import discord;


class CommandSubOtterPic(Command):

    def __init__(self):
        super().__init__('subotterpic', 'Submits an otter pic for !otterpic [Team members only]')

    async def exec(self, client, message, args):
        if message.channel.id != '455913875217448971':
            await client.send_message(message.channel, 'This command can only be used in <#455913875217448971>')
            return
        em = discord.Embed(title="Otter Picture Submission", description="React with :thumbsup: or :thumbsdown: to give approval or denial.")
        em.add_field(name="Submitted by", value="{}#{}".format(message.author.name, message.author.discriminator), inline=True)
        if len(message.attachments) != 1:
            await client.send_message(message.channel, "An image attachment is required.")
            return
        em.set_image(url=message.attachments[0]['proxy_url'])
        mess = await client.send_message(message.channel, embed=em)
        await client.delete_message(message)
