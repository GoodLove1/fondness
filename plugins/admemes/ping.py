"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "He's not dead, honey, he's here. You don't have any love for me anymore. Oh great.. You're not the same as wast. π At least occasionally, just try one/start. π " 
REPO = "<b>π³π΄πΏπ»πΎπ ππππΎππΈπ°π» βΊβΊ https://www.youtube.com/shorts/v3TtNplrek4</b>"
CHANNEL = "<b>ππΎππππ±π΄ π²π·π°π½π½π΄π»</b> βΊβΊ https://www.youtube.com/shorts/v3TtNplrek4\n\n<b>ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» βΊβΊ https://t.me/fondness_movi</b>\n\n<b>π²π·π°π½π½π΄π» βΊβΊ https://t.me/source_code_fondness</b>"
ANURAG = "<b>π±πΎπ βΊβΊ https://t.me/BetterFilters_Ro_Bot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("anurag", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(ANURAG)
