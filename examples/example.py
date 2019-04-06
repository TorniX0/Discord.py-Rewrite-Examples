import discord #importing the library

from discord.ext import commands #importing ext.commands

bot = commands.Bot(command_prefix='?') #defining bot, which is better than discord.Client(). (basically has everything that Client has.)

@bot.event #a event
async def on_ready():
    print('OK >> BOT IS READY!') #prints this when the bot is ready to-be-used.
    print(discord.__version__) #prints out the discord.py version that you have currently installed

@client.command()
async def cookie(ctx): #the definition of the command
    await ctx.message.add_reaction('🍪')  #adding a reaction to the users message
    await ctx.send('You got it!') #sending a message in the channel he ran this command

@client.command()
async def say(ctx, *, text : str): #basically a say command. text is a arg
    await ctx.send(text) #telling the user what he just passed us

bot.run("token") #insert token here
