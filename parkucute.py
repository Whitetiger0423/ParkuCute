import asyncio
import discord
import random
import re
import os, json
import datetime
from discord.ext import commands
import functools
import itertools
import math
from async_timeout import timeout


client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online, activity=discord.Game("파커쿠엽")
    )
    print("다음으로 로그인합니다 : ")
    print(client.user.name)


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if id == 593773552885301252:
        await message.add_reaction("<:cute_parku_1:1026076784481030145>")
        await message.add_reaction("<:cute_parku_2:1026076887883206717>")
        await message.add_reaction("<:cute_parku_3:1026076931629776956>")
        await message.add_reaction("<:cute_parku_4:1026077009316691989>")
        await message.add_reaction("<:cute_parku_5:1026077010990223370>")
        await message.add_reaction("<:cute_parku_6:1026077012630196297>")
        await message.add_reaction("<:cute_parku_7:1026077014865752154>")
        await message.add_reaction("<:cute_parku_8:1026077016585404437>")
        await message.add_reaction("<:cute_parku_9:1026077020356100106>")
        await message.add_reaction("❌")


@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1:
        return None
    if user.id != 593773552885301252:
        if str(reaction.emoji) == "❌":
            await reaction.message.clear_reactions()
    if user.id == 593773552885301252:
        if str(reaction.emoji) == "❌":
            user = await client.fetch_user("593773552885301252")
            await user.send(
                "https://tenor.com/view/lord-of-the-rings-you-shall-not-pass-not-pass-gandal-the-grey-gandalf-gif-7706023"
            )


client.run(TOKEN)
