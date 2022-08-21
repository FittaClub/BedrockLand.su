import discord
from discord.ext import commands
from discord import utils
import json
from mcrcon import MCRcon
import re


botTOKEN = "token"
bot = commands.Bot(command_prefix="/")


ip: str
password: str
port: int


@bot.event  
async def on_raw_reaction_add(payload):
	print("———Проверка реакций———")
	channel = bot.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	guild = bot.get_guild(payload.guild_id)
	reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
	if payload.member.id == bot.user.id:
		return
	if reaction.emoji == "✅": 
	 	message = reaction.message.id
	 	msg = await channel.fetch_message(message)
	 	embedFromMessage = msg.embeds[0]
	 	embed = str(discord.Embed.to_dict(embedFromMessage))
	 	nickname = msg.content
	 	mcr = MCRcon(ip, password, port)
	 	mcr.connect()
	 	
	 	if re.search(r'\bJava\b', embed):
	 		mcr.command("whitelist add " + str(nickname))
	 		mcr.disconnect()
	 		await channel.send("заявка успешно принята✅!")
	 		await channel.send(str(nickname) + " успешно добавлен(а) в whitelist✅!")
	 	
	 	if re.search(r'\bBedrock\b', embed):
	 		mcr.command("whitelist add " + str(nickname))
	 		mcr.disconnect()
	 		await channel.send("заявка успешно принята✅!")
	 		await channel.send(str(nickname) + " успешно добавлен(а) в whitelist✅!")
	 		
bot.run(botTOKEN)
