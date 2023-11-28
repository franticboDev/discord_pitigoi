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

logs_channel = 1178981842217598997

@bot.tree.command(name="kick", description="Kicks the bad guys.")
@commands.has_role(1178981222433705994)
@app_commands.describe(user = "User you want to kick.", reason = "What did he wrong?")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
    try:
        await user.kick(reason=reason)
        the_logs_channel = bot.get_channel(logs_channel)
        await the_logs_channel.send(f"{user.mention} was kicked by {interaction.user.mention} for {reason}")
        await interaction.response.send_message(f"Kicked {user.mention}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Could not kick the user.", ephemeral=True)

@bot.tree.command(name="ban", description="Hammer.")
@commands.has_role(1178981222433705994)
@app_commands.describe(user = "User you want to ban.", reason = "What did he wrong?")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str):
    try:
        await user.ban(reason=reason)
        the_logs_channel = bot.get_channel(logs_channel)
        await the_logs_channel.send(f"{user.mention} was banned by {interaction.user.mention} for {reason}")
        await interaction.response.send_message(f"Banned {user.mention}", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Could not ban the user.", ephemeral=True)

@bot.tree.command(name="clear_all", description="Clears all the messages in chat.")
@commands.has_role(1178981222433705994)
async def clear_all(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(f"Done.", ephemeral=True)
        await interaction.channel.purge()
        await interaction.channel.send("Cleaned all messages.")
    except:
        pass

bot.run(token)