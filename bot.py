import discord
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("대리는 DM | 딜트봇")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="in")
    await channel.send(f'로블록스 대리점에 오신걸 환영합니다! {member.mention}')
    print("한명이 서버에 들어옴!")

    role = get(member.guild.roles, name='USER')
    await member.add_roles(role)
    print("한명이 역활을 받음!")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="out")
    await channel.send(f'로블록스 대리점을 들려주셔서 감사합니다! {member.mention}')
    print("한명이 서버를 나감!")

    
access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
