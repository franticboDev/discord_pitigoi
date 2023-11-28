import discord
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="ping", description="Pings me.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong 🏓! Api latency: {0}s'.format(round(bot.latency, 1)), ephemeral=True)

@bot.tree.command(name="say", description="I will send a message.")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message("sent message", ephemeral=True)
    await interaction.channel.send(f"{thing_to_say}")

bot.run(token)