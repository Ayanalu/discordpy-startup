from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# Error時のイベント
@bot.event
async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)
    await ctx.send(f"{ctx.message.author.name}さん 何を言っているの？")
    
@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji.id)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    msg = await ctx.send('にゃーん')
    
@bot.command()
async def vote(ctx, *, question):
    msg = await ctx.send(f'アンケート： {question}\n下の✔か☓で答えてください。')
    await msg.add_reaction("✅")

    
@bot.command()
async def roll(ctx, dice : str):
    rolls, limit = map(int, dice.split('d'))
    
    total = 0
    num_list = []
    for i in range(0, rolls):
        num = random.randint(1, limit)
        num_list.append(num)
    total = sum(num_list)
    await ctx.send(f'{num_list}\n→ {total}')
                  
bot.run(token)
