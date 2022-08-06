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
        await message.add_reaction("<:cute:979917869204787271>")


client.run(TOKEN)
