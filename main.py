import discord, os, audioop, logic as l, random as r, commandapi as ca
from dotenv import load_dotenv
from logic import *
from discord.ext import commands

load_dotenv ()
token = os.getenv("dt")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name = "psw")
async def password(ctx, lenght=25):
    a = l.contra(lenght)
    await ctx.send(f"🔒Su contraseña sera generada {a}")

@bot.command(name = "coin")
async def luck(ctx):
    await ctx.send(l.coin())

@bot.command(name = "meme")
async def chiste(ctx):
    a = l.meme()
    await ctx.send(file = a)
    
@bot.command(name = "momo")
async def chiste(ctx):
    a = l.momo()
    await ctx.send(file = a)

@bot.command(name = "pato")
async def patos(ctx):
    a = ca.get_duck_image_url()
    await ctx.send(a)

bot.run(token)