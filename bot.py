import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

"""
SCRA.PY
Originally written by ScavengerOwl;
Re-written by Silver-Core;
Re-re-written by ScavengerOwl
"""

Scrap = commands.Bot(command_prefix="$")
Scrap.remove_command('help')

@Scrap.event
async def on_ready():
    print(f"{Scrap.user.name} has shone once more!")
    await Scrap.change_presence(game=discord.Game(name="$help"))

@Scrap.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    """ Pings the bot"""
    await ctx.send("***Ouch!***")
    print (f"{Scrap.user.name} has been pinged.")

@Scrap.command()
async def cookie(ctx, user: discord.Member):
    """ Gives a user a cookie"""
    await ctx.send(embed=discord.Embed(
        title="Food!", description=f"{user.name}, have a :cookie:!",
        color=discord.Color.magenta()))

@Scrap.command()
async def PM(ctx, message: str):
    """ Sends a private message"""
    await ctx.author.send(message)

@Scrap.command()
async def info(ctx, user: discord.Member):
    """ Displays user's server information"""
    emb = discord.Embed(title=f"{user.name}'s profile", color=discord.Color.magenta())
    emb.add_field(name="ID:", value=f"{user.id}")
    emb.add_field(name="Status:", value=f"{user.status}")
    emb.add_field(name="Highest Role:", value=f"{user.top_role}")
    emb.add_field(name="Joined at:", value=f"{user.joined_at}")
    emb.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=emb)


@Scrap.command(hidden = True)
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member):
    """ Kicks another user"""
    await ctx.send(embed=discord.Embed(title="KICKED", description=f"{user.name}, GET OUT! :boot:", color=discord.Color.magenta()))
    await Scrap.kick(user)

@Scrap.command()
async def flip(ctx):
    """ Flips a coin"""
    emb = discord.Embed(title="*Coin flipped*", color=discord.Color.blue())
    emb.add_field(name="You got:", value=random.choice(["**Heads**","**Tails**"]))
    await ctx.send(embed=emb)

@Scrap.command()
async def help(ctx):
    """ Shows this Message"""
    emb = discord.Embed(title="Every command should start with the prefix: ***$***", color=discord.Color.magenta())
    await ctx.send(embed=emb)
    desc = "<Command>\t<Description>\n"
    for command in Scrap.all_commands.values():
        if not command.hidden:
            desc += f"<{command.name}>\t<{command.help}>\n"
    await ctx.send(content=f"\n```{desc}```")

Scrap.run(os.getenv("TOKEN"))
