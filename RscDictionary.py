import PyDictionary
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	#On start up notifies server admin that bot initialized successfully.
	print('Bot ' + bot.user.name + " is running on ID " + bot.user.id)

@bot.command(pass_context=True)
async def define(ctx):
    from PyDictionary import PyDictionary
    dictionary = PyDictionary()
    splitWord = (ctx.message.content.split(" ")[1])
    #await bot.say(str(dictionary.meaning(splitWord)))
    definedWord=dictionary.meaning(splitWord)
    embed = discord.Embed(title="Definition of " + splitWord, description="Here's what I could find.", color=0x00ffff)
    for k, v in definedWord.items():
        for e in v:
            embed.add_field(name=k, value=e, inline=True)
    await bot.say(embed=embed)



bot.run("INSERT_BOT_TOKEN_HERE")

