from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='!')
bot.videos = ['https://www.youtube.com/watch?v=XmoKM4RunZQ', 'https://www.youtube.com/watch?v=qTmjKpl2Jk0', 'https://www.youtube.com/watch?v=hY7m5jjJ9mM']
bot.happylist = []

@bot.command()
async def hello(ctx):
    await ctx.send("hello " + ctx.author.display_name)

@bot.command()
async def cat(ctx):
    await ctx.send(random.choice(bot.videos))

@bot.command()
async def happy(ctx, *, item):
    await ctx.send("Awesome!")
    bot.happylist.append(item)
    print(bot.happylist)

@bot.command()
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happylist))

@bot.command()
async def calc(ctx, x: float, fn: str, y: float):
    if fn == '+':
        await ctx.send(x + y)
    elif fn == '-':
        await ctx.send(x - y)
    elif fn == '*':
        await ctx.send(x * y)
    elif fn == '/':
        await ctx.send(x / y)
    else:
        await ctx.send("We only support 4 function operations")


password = os.environ['password']
bot.run(password)