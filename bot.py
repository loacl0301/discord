import asyncio
import discord

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "ODc2MzkwNTAzNjUyOTQ1OTMw.YRjYQg.S0dXPfBMDrAzXO8hSqXBeO0EEmo"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("봇연습#6890") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("안녕하세요? 챗봇입니다")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("아직 베타 테스트 중이예요~")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.



# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕하세요? 오늘도 좋은하루 보내세요!')

    if message.content == "!임베드":
      embed = discord.Embed(title = "테스트봇의 도움말", description = '''
      예시''', color = 0xffffff) # 여기예요! 0xffffff중 ffffff를 #을 뺀 나머지 것들을 붙여넣기 해주세요!

      await message.channel.send(embed = embed)

    if message.content.startswith('!병신'):
        channel = message.channel
        await channel.send('병신새끼')




client.run(token)
