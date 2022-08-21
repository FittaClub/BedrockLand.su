import discord
from discord.ext import commands
import json
from multiprocessing import Process

from app import func

token = 'token'
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print('––––BOT RUN––––')
    with open('json/data.json', 'r') as fh:
        data = json.load(fh)
    with open('json/nicknames.json', 'r') as fh:
        nickname = json.load(fh)
    embed = discord.Embed(title='', description='', color=0xFF8000)
    embed.add_field(name='Новая заявка!', value=data, inline=False)
    channel = bot.get_channel(id)
    if nickname != '':
        msg = await channel.send(f'<@&{id}>', embed=embed)
    else:
        print('Ник пустой')
    with open('json/nicknames.json', 'w') as write:
        json.dump("", write)
    print('––––BOT CLOSE––––')
    Process(target=func).close()
