import discord
from discord.ext import commands
from discord.ui import Button, View

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

@bot.command()
async def ping(ctx):
    latency=round(bot.latency*1000)
    await ctx.send(f'{latency}ms')

@bot.command()
async def info(ctx):

    embed=discord.Embed(
        title=f"{ctx.author.name} Your info",
        description="making discord bot",
        color=0x00ff00 
    )

    embed.add_field(name="creation date",value=ctx.author.created_at.strftime("%yyear%mmonth%dday"),inline=False)

    embed.set_thumbnail(url=ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url)

    await ctx.send(embed=embed)


    #Fruit gambling game which requires currency and a selling mechanic
    

























bot.run('MTUxNjkyNzkzNDgzMTY1NzE1Mg.GyaDAK.S_p_aHoUavMvuJyQlCsVjCuO_dJWkC06rSg9T0')