import discord
from discord.ext import commands
from discord.ext import app_commands
from discord.ext import bot
from fetch import fashionFetch
from privateinfo import info

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix= '0', intents= intents)


@client.event
async def on_ready():
    print("Bot is ready.")
    print("-------------")

# decorators related to app commands should be placed below the hybrid_command decorator as per documentation

@commands.hybrid_command(name='fashion', with_app_command=True)
@app_commands.describe(Fashion for the week)
async def fashion(ctx):
    post = await fashionFetch()
    if(post != ""):
        em = discord.Embed(title = post.title)
        em.set_image(url=post.url)
        await ctx.channel.send(embed=em)
        await ctx.channel.send(content="-# *from:* " + post.shortlink, suppress_embeds=True)
    else:
        await ctx.channel.send("THERE IS NO POST FOR THIS WEEK YET!!!")

@commands.hybrid_command(name='hi', with_app_command=True)
@app_commands.describe(hello)
async def hi(ctx):
    await ctx.channel.send("hi")


@commands.hybrid_command(name='goodnight', with_app_command=True)
@app_commands.describe(goodbye)
async def goodnight(ctx):
    await ctx.channel.send("Goodnight bro, love is real")

# block dms
# Waiting for an answer you'll never recieve is more painful than never recieving one at all.

@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


client.run(info.botcode)
