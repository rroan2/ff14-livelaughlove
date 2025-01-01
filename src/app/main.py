import discord
from discord.ext import commands
from fetch import fashionFetch
from privateinfo import info

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix= '0', intents= intents)


@client.event
async def on_ready():
    print("Bot is ready.")
    print("-------------")

@client.command()
async def fashion(ctx):
    post = await fashionFetch()
    if(post != None):
        em = discord.Embed(title = post.title)
        em.set_image(url=post.url)
        await ctx.channel.send(embed=em)
        await ctx.channel.send(content="-# *from:* " + post.shortlink, suppress_embeds=True)
    else:
        await ctx.channel.send("THERE IS NO POST FOR THIS WEEK YET")

@client.command()
async def hi(ctx):
    await ctx.channel.send("hi")


@client.command()
async def goodnight(ctx):
    await ctx.channel.send("Goodnight bro, love is real")


client.run(info.botcode)
