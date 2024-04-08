import discord
import random
import re
from discord.ext import commands

TOKEN = 'your_token'

intents = discord.Intents.all()
intents.messages = True 

bot = commands.Bot(command_prefix='!', intents=intents)

def roll_dice(roll_command):
    match = re.match(r'^(\d+)d(\d+)([+\-]\d+)?$', roll_command)
    if match:
        quantity = int(match.group(1))
        sides = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        rolls = [random.randint(1, sides) for _ in range(quantity)]
        total = sum(rolls) + modifier
        return rolls, total
    else:
        return None, None

@bot.command(name='roll')
async def roll(ctx, roll_command):
    rolls, total = roll_dice(roll_command)
    if rolls is not None and total is not None:
        response = f'Rolagem: {rolls}\nTotal: {total}'
    else:
        response = 'Comando inválido!'
    await ctx.send(response)

@bot.event
async def on_ready():
    print('Bot está pronto!')

bot.run('your_token')
