import discord
import datetime


client = discord.Client()

@client.event
async def on_ready():
    print("------------")
    print("로그인")
    print("봇 제작자:호떡#9460")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    game = discord.Game("호떡이가 제작중인 봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/help"):
       embed = discord.Embed(color=0x00ff00)
       embed.add_field(name="[help]", value="/help를 치시면 사진의 정보를 알수있습니다.", inline=False)
       embed.add_field(name="[help]", value="/출근,/퇴근을 치시면 출근 퇴근이 가능합니다.", inline=False)
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/724230191550955582/781375414689857576/55a42c2df85c4eb7.png")  #메세지 오른쪽 작은 이미지
       await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/정보"):
       date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
       embed = discord.Embed(color=0x00ff00)
       embed.add_field(name="[이름]", value=message.author.name, inline=False)
       embed.add_field(name="[서버닉네임]", value=message.author.display_name, inline=False)
       embed.add_field(name="[가입일]", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
       embed.add_field(name="[아이디]", value=message.author.id, inline=False)
       embed.set_thumbnail(url=message.author.avatar_url)
       await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/출근"):
       embed = discord.Embed(color=0x00ff00)
       embed.add_field(name="[출근]", value=message.author.name + "님께서 출근하셨습니다.", inline=False)
       embed.add_field(name="[아이디]", value=message.author.id, inline=False)
       embed.set_thumbnail(url=message.author.avatar_url)
       await message.channel.send(message.channel, embed=embed)

    if message.content.startswith("/퇴근"):
       embed = discord.Embed(color=0x00ff00)
       embed.add_field(name="[퇴근]", value=message.author.name + "님께서 퇴근하셨습니다.", inline=False)
       embed.add_field(name="[아이디]", value=message.author.id, inline=False)
       embed.set_thumbnail(url=message.author.avatar_url)
       await message.channel.send(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run('access_token')
