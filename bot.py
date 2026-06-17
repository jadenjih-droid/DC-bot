import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    print('==============================')
    print(f'login sucessful: {bot.user.name}')
    print('bot sucessfuly launched')
    print('==============================')

@bot.command()
async def hello(ctx):
    await ctx.send(f'{ctx.author.name} hello!')

  
