import random
import keep_alive
import os

from kaomoji import kaomoji_list

#creating discord connection
from discord.ext import commands

#bot

bot = commands.Bot(command_prefix = '~')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#commands

@bot.command(name = "teehee", help = 'Responds with a random kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(random.choice(kaomoji_list))
    await ctx.send(response)
    
@bot.command(name = 'uwu', help = 'Responds with a random joy kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_joy)
    await ctx.send(response)
    
@bot.command(name = 'doki', help = 'Responds with a random love kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_love)
    await ctx.send(response)
    
@bot.command(name = 'yamete', help = 'Responds with a random embarrassment kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_embarrassment)
    await ctx.send(response)
    
@bot.command(name = 'F', help = 'Responds with a random sympathy kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sympathy)
    await ctx.send(response)
    
@bot.command(name = 'tsk', help = 'Responds with a random dissatisfaction kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_dissatisfaction)
    await ctx.send(response)
    
@bot.command(name = 'YAH', help = 'Responds with a random anger kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_anger)
    await ctx.send(response)
    
@bot.command(name = 'ono', help = 'Responds with a random sad kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sad)
    await ctx.send(response)
    
@bot.command(name = 'uhu', help = 'Responds with a random pain kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_pain)
    await ctx.send(response)

@bot.command(name = 'OWO!', help = 'Responds with a random fear kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_fear)
    await ctx.send(response)
    
@bot.command(name = 'ehh', help = 'Responds with a random indifference kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_indifference)
    await ctx.send(response)
    
@bot.command(name = 'owo?', help = 'Responds with a random confusion kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_confusion)
    await ctx.send(response)
    
@bot.command(name = 'ehh?', help = 'Responds with a random doubt kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_doubt)
    await ctx.send(response)
    
@bot.command(name = 'owo!', help = 'Responds with a random surprise kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_surprise)
    await ctx.send(response)
    
@bot.command(name = 'hug', help = 'Responds with a random hugging kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_hugging)
    await ctx.send(response)
    
@bot.command(name = 'wink', help = 'Responds with a random winking kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_winking)
    await ctx.send(response)
    
@bot.command(name = 'gomen', help = 'Responds with a random sorry kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sorry)
    await ctx.send(response)
    
@bot.command(name = 'yawn', help = 'Responds with a random sleeping kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sleeping)
    await ctx.send(response)
    
@bot.command(name = 'hehe', help = 'Responds with a random special kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_special)
    await ctx.send(response)
    
@bot.command(name = 'friend!', help = 'Responds with a random friend kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_friends)
    await ctx.send(response)

@bot.command(name = 'oy', help = 'Responds with a random enemies kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_enemies)
    await ctx.send(response)

TOKEN=os.getenv('TOKEN')
keep_alive.keep_alive()
bot.run(TOKEN)