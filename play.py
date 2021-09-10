from os import system
from sys import argv
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='',self_bot=True)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    channel = await bot.get_channel(int(argv[2])).connect()
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    channel.play(discord.FFmpegPCMAudio("Chin_Cheng_Hanji_Meme_(EARRAPE).mp3",**FFMPEG_OPTS), after=lambda e: print('done', e))
bot.run(argv[1], bot=False)