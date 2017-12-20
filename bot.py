import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

"""
SCRA.PY
Originally written by ScavengerOwl;
Re-written by Silver-Core;
Re-re-written by ScavengerOwl.
"""

Scrap = commands.Bot(command_prefix="$")
Scrap.remove_command('help')

@Scrap.event
async def on_ready():
    print(f"{Scrap.user.name} has shone once more!")
    await Scrap.change_presence(game=discord.Game(name="$help"))

@Scrap.command()
@commands.has_role("Master")
async def ping(ctx):
    """ Pings the bot. """
    await ctx.send("***Ouch!***")
    print (f"{Scrap.user.name} has been pinged.")

@Scrap.command()
async def cookie(ctx, user: discord.Member):
    """ Gives a user a cookie. """
    await ctx.send(embed=discord.Embed(title="Food!", description=f"{user.name}, have a :cookie:!", color=discord.Color.dark_gold()))

@Scrap.command()
async def PM(ctx, message: str):
    """ PM's a User. """
    try:
        await Scrap.send(ctx.author, message)

    except (discord.Forbidden, discord.HTTPException) as e:
        await ctx.send(f"{ctx.author.mention}, You do not have PMs open.")

@Scrap.command()
async def info(ctx, user: discord.Member):
    """ Displays user's server information """
    emb = discord.Embed(title=f"{user.name}'s profile", color=discord.Color.red())
    emb.add_field(name="ID:", value=f"{user.id}")
    emb.add_field(name="Status:", value=f"{user.status}")
    emb.add_field(name="Highest Role:", value=f"{user.top_role}")
    emb.add_field(name="Joined at:", value=f"{user.joined_at}")
    emb.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=emb)


@Scrap.command()
@commands.has_role("Master")
async def kick(ctx, user: discord.Member):
    """ Kicks another user (WORK IN PROGRESS) """
    await ctx.send(embed=discord.Embed(title="KICKED", description=f"{user.name}, GET OUT! :boot:", color=discord.Color.green()))
    await Scrap.kick(user)

@Scrap.command()
async def flip(ctx):
    emb = discord.Embed(title="*Coin flipped*", color=discord.Color.blue())
    emb.add_field(name="You got:", value=random.choice(["**Heads**","**Tails**"]))
    await ctx.send(embed=emb)

@Scrap.command()
async def help(ctx):
    """ Shows this message. """
    msg = await ctx.send(embed=Embed(title='Help is coming.', color=discord.Color.dark_magenta()))
    e = Embed(title='Hello there!', color=discord.Color.magenta(), description='Every command should start with the prefix ***$***')
    for command_obj in self.bot.all_commands.values():
        if not command_obj.hidden:
            e.add_field(name=f'{command_obj.name.title()}', value=f'{command_obj.help}', inline=False)
        await msg.edit(embed=e)


Scrap.run(os.getenv("TOKEN"))
