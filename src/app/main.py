import discord
from discord.ext import commands
from fetch import fashionFetch
import privateinfo 

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix= '0', intents= intents)


@client.event
async def on_ready():
    print("Bot is ready.")
    print("-------------")

@bot.hybrid_command()
async def fashion(ctx):
    post = await fashionFetch()
    if(post != ""):
        em = discord.Embed(title = post.title)
        em.set_image(url=post.url)
        await ctx.channel.send(embed=em)
        await ctx.channel.send(content="-# *from:* " + post.shortlink, suppress_embeds=True)
    else:
        await ctx.channel.send("THERE IS NO POST FOR THIS WEEK YET!!!")

@bot.hybrid_command()
async def hi(ctx):
    await ctx.channel.send("hi")


@bot.hybrid_command()
async def goodnight(ctx):
    await ctx.channel.send("Goodnight bro, love is real")

# block dms
# Waiting for an answer you'll never recieve is more painful than never recieving one at all.

@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


client.run(privateinfo.info.botcode)
