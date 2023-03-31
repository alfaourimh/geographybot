import discord
import wikipedia
import random
client = discord.Client()

with open('countries.csv') as f:
    words = f.read().split()
    SearchResults = random.choice(words) + " country"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$search"):
        await message.channel.send(wikipedia.page(SearchResults))
        await message.channel.send(wikipedia.summary(SearchResults[:2000]))
            
client.run('TOKEN')