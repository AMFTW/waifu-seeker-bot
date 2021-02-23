"""
The logic for the bot.
"""
import os

import discord
import requests

import utils

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')
MAX_URLS_TO_SEARCH = 2000
URL = 'https://www.google.com/search?q=hot+anime+waifu+&tbm=isch&ved=2ahUKEwiytvHXv4DvAhXrK7cAHSZXBUoQ2-cCegQIABAA&oq=hot+anime+waifu+&gs_lcp=CgNpbWcQA1CZM1iZM2DWNGgAcAB4AIABVIgBVJIBATGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=xTY1YPK_E-vX3LUPpq6V0AQ&bih=763&biw=1536'

waifu = discord.Client()


@waifu.event
async def on_message(msg: discord.message) -> None:
    """
    When the bot is mentioned, send a random image url along with a message
    pinging the person who mentioned the bot on discord.

    :param msg: An autofilled parameter which is the message the bot
    was mentioned with.
    """
    if msg.author == waifu.user:
        return
    if waifu.user.mentioned_in(msg):
        await msg.channel.send(
            f'Here you go, you horny child!, {msg.author.mention}'
        )
        await msg.channel.send(
            utils.get_rand_img_url(requests.get(URL).text, MAX_URLS_TO_SEARCH)
        )


waifu.run(DISCORD_TOKEN)
