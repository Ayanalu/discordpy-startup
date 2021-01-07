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
    if reaction.count == 2:
        if reaction.emoji == "\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(1, 100)
            prev(1, dice, reaction)
        if reaction.emoji == "\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(1, 10)
            prev(1, dice, reaction)
        if reaction.emoji == "\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(3, 6)
            prev(3, dice, reaction)
        if reaction.emoji == "\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(1, 6)
            prev(1, dice, reaction)
        if reaction.emoji == "\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(1, 4)
            prev(1, dice, reaction)        
        if reaction.emoji == "\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}":
            dice = diceroll(2, 3)
            prev(2, dice, reaction)
            
            
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    msg = await ctx.send('にゃーん')
    
@bot.command()
# async def dice(ctx, *, question):
async def dice(ctx):
    msg = await ctx.send(f'0：1D100\n1：1D10\n2：3D6\n3：1D6\n4：1D4\n5：2D3')
    await msg.add_reaction("\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT SIX}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT SEVEN}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT EIGHT}\N{COMBINING ENCLOSING KEYCAP}")
    await msg.add_reaction("\N{DIGIT NINE}\N{COMBINING ENCLOSING KEYCAP}")


@bot.command()
async def roll(ctx, dice : str):
    rolls, limit = map(int, dice.split('d'))
    dice = diceroll(rolls, limit)
    await reaction.message.channel.send(f'**{dice[1]}**')
    del dice[1]
    await reaction.message.channel.send(f'内訳：{dice}')    

    
def diceroll(rolls : int, limit : int):
    total = 0
    num_list = []
    for i in range(0, rolls):
        num = random.randint(1, limit)
        num_list.append(num)
    total = sum(num_list)
    num_list.append(total)
    return num_list

def prev(limit, dice, reaction):
    await reaction.message.channel.send(f'**{dice[limit]}**')
    del dice[limit]
    await reaction.message.channel.send(f'内訳：{dice}')
                  
bot.run(token)
