from telethon import events, Button, custom
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lion import ALIVE_NAME, CMD_HELP
from Lion.__init__ import StartTime
from Lion.LionConfig import Config, Var

from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else "https://telegra.ph/file/bfa06df35913425dbcbc1.jpg"
telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση υsεя"


@Lion.on(admin_cmd(outgoing=True, pattern="alive"))
@Lion.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        fuking_text = "**ʏօօ!! ʏօʊʀ ʟɨօռ ʊֆɛʀɮօȶ ɨֆ ǟʟɨʋɛ**\n\n"
        fuking_text += "**му αℓℓ ѕуѕтєм ιѕ ѕмσσтℓу яυииιg**\n"
        fuking_text += f"**ℓισи νєяѕισи**: 1.0\n"
        fuking_text += "**тнιѕ вσт ιѕ fυℓℓу υρ-тσ-∂αтє**\n"
        fuking_text += "**тєℓєтнσи νєяѕισи**: 1.2\n"
        fuking_text += f"**тникѕ fσя cнεcкιиg мε🤓**\n"
        fuking_button = [[Custom.Button.inline("Mʏ ᴅᴇᴠ✨", "https://github.com/Mdnoor786/Lion-X/graphs/contributors"")]]
        fuking_button += [[Custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀʏ", "https://github.com/Mdnoor786/Lion-X")]]
        await borg.send_file(event.chat_id, ALV_PIC, captions=fuking_text, buttons=fuking_button)
        await alive.delete()
  

    
    CMD_HELP.update({"αℓιvε": "➤ `.alive`\nUse - Check if your bot is working."})
