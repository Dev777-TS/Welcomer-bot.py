import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event 
async def on_member_join(member):
    guild = client.get_guild("SERVER ID HERE")
    channel = guild.get_channel("CHANNEL ID FOR WELCOMING HERE")
    try:
        await member.send(f'Welcome to the{guild.name} sever, {member.name}!  :partying_face:')
    except:
        await channel.send(f'Welcome to the server, {member.mention}! :partying_face:')

client.run("BOT TOKEN HERE")