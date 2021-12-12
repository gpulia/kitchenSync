import discord
import requests

client = discord.Client()

tokenFile = open('secret.secret','r')
token = tokenFile.readline()

@client.event
async def on_message(msg):
    if msg.content.startswith('$$$$'):
        name = msg.content[4::]
        apiCall = 'https://na.whatismymmr.com/api/v1/summoner?name=' + name
        response = requests.get(apiCall)
        if(response.status_code == 200):
            data = response.json()
            Ammr = data['ARAM']['avg']
            Apct = data['ARAM']['percentile']
            Arank = data['ARAM']['closestRank']
            builtMsg = f'{name}\'s ARAM MMR: {Ammr}\n{Apct}th percentile, about {Arank}'
            await msg.channel.send(builtMsg)
        else:
            await msg.channel.send('RIP LMAO.')
##test push
client.run(token)