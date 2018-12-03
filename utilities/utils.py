import discord

class TextUtilities:

    def guildColor(self, data):
        if data is not None:
            output = data.me.color
        else:
            output = discord.Colour.blue()
        return output