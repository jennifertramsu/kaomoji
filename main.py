import random
import keep_alive
import os

from kaomoji import kaomoji_list

#creating discord connection
from discord.ext import commands

#bot

bot = commands.Bot(command_prefix='~')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


#commands


@bot.command(name='uwu', help='Responds with a random joy kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['joy'])
    await ctx.send(response)


@bot.command(name='doki', help='Responds with a random love kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['love'])
    await ctx.send(response)


@bot.command(name='yamete',
             help='Responds with a random embarrassment kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['embarrassment'])
    await ctx.send(response)


@bot.command(name='F', help='Responds with a random sympathy kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['sympathy'])
    await ctx.send(response)


@bot.command(name='tsk', help='Responds with a random dissatisfaction kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['dissatisfaction'])
    await ctx.send(response)


@bot.command(name='YAH', help='Responds with a random anger kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['anger'])
    await ctx.send(response)


@bot.command(name='ono', help='Responds with a random sad kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['sad'])
    await ctx.send(response)


@bot.command(name='uhu', help='Responds with a random pain kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['pain'])
    await ctx.send(response)


@bot.command(name='OWO!', help='Responds with a random fear kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['fear'])
    await ctx.send(response)


@bot.command(name='ehh', help='Responds with a random indifference kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['indifference'])
    await ctx.send(response)


@bot.command(name='owo?', help='Responds with a random confusion kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['confusion'])
    await ctx.send(response)


@bot.command(name='ehh?', help='Responds with a random doubt kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['doubt'])
    await ctx.send(response)


@bot.command(name='owo!', help='Responds with a random surprise kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['surprise'])
    await ctx.send(response)


@bot.command(name='hug', help='Responds with a random hugging kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['hugging'])
    await ctx.send(response)


@bot.command(name='wink', help='Responds with a random winking kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['winking'])
    await ctx.send(response)


@bot.command(name='gomen', help='Responds with a random sorry kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['sorry'])
    await ctx.send(response)


@bot.command(name='yawn', help='Responds with a random sleeping kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['sleeping'])
    await ctx.send(response)


@bot.command(name='hehe', help='Responds with a random special kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['special'])
    await ctx.send(response)


@bot.command(name='friend!', help='Responds with a random friend kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['friends'])
    await ctx.send(response)


@bot.command(name='oy', help='Responds with a random enemies kaomoji')
async def kaomoji_random(ctx):
    response = random.choice(kaomoji_list['enemies'])
    await ctx.send(response)


# testing env

@bot.command(name='reminder')
async def remindMe(ctx):
    user = await bot.fetch_user(656620638869651469)
    msg = "GO STUDY"
    await user.send(msg)

TOKEN = os.getenv('TOKEN')
keep_alive.keep_alive()
bot.run(TOKEN)
