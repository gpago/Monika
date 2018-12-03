import discord
from discord.ext import commands
import aiohttp
from utilities import checks
from io import StringIO
from pybooru import Danbooru
import rule34
import json
import asyncio
from utilities import libBoorus

global checks
checks = checks.Checks()
global booruslib
booruslib = libBoorus.Boorus()


# TODO Separate commands for SFW and NSFW or internal tag??

class Realbooru:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.command()
    @checks.in_nsfw()
    async def realbooru(self, ctx):
        """Posts an image directly from Realbooru."""
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        else:
            color = discord.Colour.blue()
        embed = discord.Embed(color=color, title="Denied!", description="Trying to look at 3D girls, eh? I don't think so {}!".format(ctx.message.author.name))
        embed.set_image(url="https://danbooru.donmai.us/data/sample/__monika_doki_doki_literature_club_drawn_by_tjf_513274409__sample-b4a1bb2da0447bb56a13acab82e088b5.jpg")
        await ctx.send(embed=embed)


class Gelbooru:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.command()
    @checks.in_nsfw()
    async def gelbooru(self, ctx):
        """Posts an image directly from Gelbooru."""
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        else:
            color = discord.Colour.blue()
        embed = discord.Embed(color=color, title="Oh nuu! This function is not implemented yet.", description="Writing python code..aaand 46 exceptions??!!")
        embed.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/303/902/885.jpg")
        await ctx.send(embed=embed)


class Rule34:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.command()
    @checks.in_nsfw()
    async def rule34(self, ctx):
        """Posts an image directly from Rule34."""
        r34 = rule34.Rule34(asyncio.get_event_loop())
        data = await r34.getImageURLS(tags='*', randomPID=1)
        url = data[0]
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        else:
            color = discord.Colour.blue()
        embed = discord.Embed(color=color, title="Image from Rule34!", description="Here's your image, {}~".format(ctx.message.author.name))
        embed.set_image(url=url)
        embed.set_footer(text="Powered by Rule34.")
        await ctx.send(embed=embed)

    @commands.command()
    @checks.command()
    async def rule34(self, ctx):
        """Posts an image directly from Rule34."""
        r34 = rule34.Rule34(asyncio.get_event_loop())
        data = await r34.getImageURLS(tags='*', randomPID=1)
        url = data[0]
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        else:
            color = discord.Colour.blue()
        embed = discord.Embed(color=color, title="Image from Rule34!", description="Here's your image, {}~".format(ctx.message.author.name))
        embed.set_image(url=url)
        embed.set_footer(text="Powered by Rule34.")
        await ctx.send(embed=embed)


class Danbooru:

    def __init__(self, bot):
        self.bot = bot

    def fixDanbooruJSON(self, temp):
        temp = temp.replace("{\'", "{\"")
        temp = temp.replace("\': ", "\": ")
        temp = temp.replace("\": \'", "\": \"")
        temp = temp.replace("\', \'", "\", \"")
        temp = temp.replace(", \'", ", \"")
        temp = temp.replace("\'}", "\"}")
        temp = temp.replace("True", "\"True\"")
        temp = temp.replace("False", "\"False\"")
        temp = temp.replace("None", "\"None\"")
        temp = temp.replace("[", "")
        temp = temp.replace("]", "")
        return temp

    # @commands.command()
    # @checks.command()
    # async def safedanbooru(self, ctx):
    #     """Same as danbooru, but looks for safe images."""
    #     client = Danbooru('danbooru', username=self.bot.config['danbooruuser'], api_key=self.bot.config['danboorukey'])
    #     image_found = False
    #     while not image_found:
    #         temp = self.fixDanbooruJSON(str(client.post_list(random=True, limit=1, tags="rating:s -status:deleted")))
    #         data = json.loads(temp)
    #         if 'file_url' in data:
    #             image_found = True
    #     url = data['file_url']
    #     if ctx.message.guild is not None:
    #         color = ctx.message.guild.me.color
    #     else:
    #         color = discord.Colour.blue()
    #     embed = discord.Embed(color=color, title="Image from Project Danbooru!", description="Here's your 'safe' image, {}~".format(ctx.message.author.name))
    #     embed.set_image(url=url)
    #     embed.set_footer(text="Powered by Project Danbooru.")
    #     await ctx.send(embed=embed)

    @commands.command()
    @checks.command()
    @checks.in_nsfw()
    async def danbooru(self, ctx):
        """Posts an image directly from Danbooru."""
        client = Danbooru('danbooru', username=self.bot.config['boorus']['Danbooru']['user'], api_key=self.bot.config['boorus']['Danbooru']['key'])
        temp = str(client.post_list(random=True, limit=1))
        temp = temp.replace("\'", "\"")
        temp = temp.replace("True", "\"True\"")
        temp = temp.replace("False", "\"False\"")
        temp = temp.replace("None", "\"None\"")
        temp = temp.replace("[", "")
        temp = temp.replace("]", "")
        data = json.loads(temp)
        url = data['file_url']
        if ctx.message.guild is not None:
            color = ctx.message.guild.me.color
        else:
            color = discord.Colour.blue()
        embed = discord.Embed(color=color, title="Image from Danbooru!", description="Here's your image, {}~".format(ctx.message.author.name))
        embed.set_image(url=url)
        embed.set_footer(text="Powered by Danbooru.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Danbooru(bot))
    bot.add_cog(Realbooru(bot))
    bot.add_cog(Rule34(bot))
    bot.add_cog(Gelbooru(bot))
