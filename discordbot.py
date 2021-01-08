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
    if reaction.count != 1:
        if reaction.emoji == "<:1D100:797018895226634250>":
            dice = diceroll(1, 100)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[1]}**')
            del dice[1]
            await reaction.message.channel.send(f'```内訳：1D100 {dice}```')
        if reaction.emoji == "<:1D10:797018894903934997>":
            dice = diceroll(1, 10)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[1]}**')
            del dice[1]
            await reaction.message.channel.send(f'```内訳：1D10 {dice}```')
        if reaction.emoji == "<:3D6:797018895419965490>":
            dice = diceroll(3, 6)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[3]}**')
            del dice[3]
            await reaction.message.channel.send(f'```内訳：3D6 {dice}```')
        if reaction.emoji == "<:1D6:797018895382216724>":
            dice = diceroll(1, 6)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[1]}**')
            del dice[1]
            await reaction.message.channel.send(f'```内訳：1D6 {dice}```')
        if reaction.emoji == "<:1D4:797018895206711297>":
            dice = diceroll(1, 4)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[1]}**')
            del dice[1]
            await reaction.message.channel.send(f'```内訳：1D4 {dice}```')  
        if reaction.emoji == "<:2D3:797018895215099945>":
            dice = diceroll(2, 3)
            await reaction.message.channel.send(f'{user.mention} ➨ **{dice[2]}**')
            del dice[2]
            await reaction.message.channel.send(f'```内訳：2D3 {dice}```')
            
            
@bot.command()
async def ping(ctx):
    """test"""
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    """猫"""
    msg = await ctx.send('にゃーん')
    
@bot.command()
# async def dice(ctx, *, question):
async def dice(ctx):
    """ダイスを振る(簡易)"""
    msg = await ctx.send(f'>>> 0：1D100\n1：1D10\n2：3D6\n3：1D6\n4：1D4\n5：2D3')
    await msg.add_reaction("<:1D100:797018895226634250>")
    await msg.add_reaction("<:1D10:797018894903934997>")
    await msg.add_reaction("<:3D6:797018895419965490>")
    await msg.add_reaction("<:1D6:797018895382216724>")
    await msg.add_reaction("<:1D4:797018895206711297>")
    await msg.add_reaction("<:2D3:797018895215099945>")
#     await msg.add_reaction("\N{DIGIT ZERO}\N{COMBINING ENCLOSING KEYCAP}")
#     await msg.add_reaction("\N{DIGIT ONE}\N{COMBINING ENCLOSING KEYCAP}")
#     await msg.add_reaction("\N{DIGIT TWO}\N{COMBINING ENCLOSING KEYCAP}")
#     await msg.add_reaction("\N{DIGIT THREE}\N{COMBINING ENCLOSING KEYCAP}")
#     await msg.add_reaction("\N{DIGIT FOUR}\N{COMBINING ENCLOSING KEYCAP}")
#     await msg.add_reaction("\N{DIGIT FIVE}\N{COMBINING ENCLOSING KEYCAP}")


@bot.command()
async def roll(ctx, dice : str):
    """NdNでダイスを振る"""
    rolls, limit = map(int, dice.split('d'))
    dice = diceroll(rolls, limit)
    await ctx.send(f'{ctx.author.mention} ➨ **{dice[rolls]}**')
    del dice[rolls]
    await ctx.send(f'```内訳：{rolls}D{limit} {dice}```')    

    
def diceroll(rolls : int, limit : int):
    total = 0
    num_list = []
    for i in range(0, rolls):
        num = random.randint(1, limit)
        num_list.append(num)
    total = sum(num_list)
    num_list.append(total)
    return num_list
                 
bot.run(token)
