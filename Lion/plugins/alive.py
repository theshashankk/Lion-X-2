
from telethon import events, Button, custom
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lion import ALIVE_NAME, CMD_HELP, lionver
from Lion.__init__ import StartTime
from Lion.LionConfig import Config, Var

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
        fuking_text += "**му αℓℓ ѕуѕтєм ιѕ ѕмσσтℓу яυииιg**\n\n"
        fuking_text += f"**ℓισи νєяѕισи**: 1.0\n\n"
        fuking_text += "**тнιѕ вσт ιѕ fυℓℓу υρ-тσ-∂αтє**\n\n"
        fuking_text += "**тєℓєтнσи νєяѕισи**: 1.2\n\n"
        fuking_text += f"**тникѕ fσя cнεcкιиg мε🤓**\n\n"
        fuking_text +="**𝐌𝐘 𝐃𝐄𝐕**\n\n"
        fuking_text += "**[Sʜᴀsʜᴀɴᴋ xD](t.me/ShashankxD)\n\n"
        fuking_text += "**[Mᴅ Nᴏᴏʀ](t.me/SimpleBoy786)\n\n"
        fuking_text += "**[Gɪᴛʜᴜʙ Rᴇᴘᴏsɪᴛᴏʀʏ](https://github.com/mdnoor786/LionX)\n\n"
        fuking_button = [[Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/mdnoor786/LionX")]]
        await borg.send_file(alive.chat_id, ALV_PIC, caption=fuking_text, buttons=fuking_button, link_preview=False)          #Dont replace repo with real one tilk userbot not complete
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        
CMD_HELP.update({"αℓιvε": "➤ `.alive`\nUse - Check if your bot is working."})
