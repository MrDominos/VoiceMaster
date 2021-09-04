import discord
from discord.ext import commands
import traceback
import sys, time, os
from sys import platform

if platform == "win32":
    clear = "cls"
elif platform == "linux" or platform == "linux2":
    clear = "clear"
else:
    clear = "cls"



bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot.remove_command("help")

DISCORD_TOKEN = 'ODExMDgyNzYxODk1OTM2MDUy.YCtBrw.zktCgGab44KAmm0IZwLgxSVyy58'

initial_extensions = ['cogs.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="You"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
kunci = input("Masukan Passwordmu: ")
if kunci == "@nj#l#21":
    print("Berhasil login!")
    print("Bot dijalankan dalam 3 detik")
    time.sleep(3)
    os.system(clear)
    bot.run(DISCORD_TOKEN)
