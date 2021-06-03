from telethon import events, Button, custom
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lion import ALIVE_NAME, CMD_HELP
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
    
fuking_bot = (
    Var.TG_BOT_USER_NAME_BF_HER
    if Var.TG_BOT_USER_NAME_BF_HER
    else "ℓισи υѕєявσт"
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
        fuking_text += f"**{fukingbot} νєяѕισи**: 1.0\n"
        fuking_text += "**тнιѕ вσт ιѕ fυℓℓу υρ-тσ-∂αтє**\n"
        fuking_text += "**тєℓєтнσи νєяѕισи**: 1.2\n"
        fuking_text += f"**уσυя αѕѕιѕтαия**: {fuking_bot}\n"
        fuking_button = [[Custom.Button.inline("Mʏ ᴅᴇᴠ", data="developer")]]
        fuking_button += [[Custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀʏ", data="gay")]]
        await borg.send_file(event.chat_id, ALV_PIC, captions=fuking_text, buttons=fuking_button)
        await alive.delete()
  
  @Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"developer")))
  async def callback_query_handler(event):
    gay = "𝐌𝐘 𝐃𝐄𝐕\n"
    gay += "[Sʜᴀsʜᴀɴᴋ xD](https://github.com/theshashankk)\n"
    gay += "[Mᴅ ɴᴏᴏʀ](https://github.com/mdnoor786)\n"
    await borg.send_message(event.chat_id, captions=gay)
  
  @Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"gay")))
  async def callback_query_handler(event):
    gay_text = "нєяє ιѕ ℓισи υѕєявσт gιтнυв яєρσѕιтσяу αи∂ нєяσкυ ℓιик\n\n"
    gay_text += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 Sʜᴀsʜᴀɴᴋ [DEV] AND Mᴅ ɴᴏᴏʀ [DEV]\n"
    gay_text += "🚑ѕυρρσят gяσυρ🚑", "t.me/LionXsupport")]]
    gay_button = [[Button.url("Hᴇʀᴏᴋᴜ", "https://heroku.com/deploy?template=https://github.com/mdnoor786/lion-X"), Button.url("Hᴇʀᴏᴋᴜ", "https://heroku.com/deploy?template=https://github.com/mdnoor786/lion-X")]]
    await borg.send_file(event.chat_id, ALV_PIC, captions=gay_text, buttons=gay_button)
    
@Lion.on(admin_cmd(outgoing=True, pattern="repo"))
async def repo(event):
  await borg.send_message(event.chat, "Rᴇᴘᴏsɪᴛᴏʀʏ ᴏғ ʟɪᴏɴ ᴜsᴇʀʙᴏᴛ", buttons=[[Button.url("✨Rᴇᴘᴏsɪᴛᴏʀʏ✨", "https://github.com/mdnoor786/LionX-UB")]])
    
    CMD_HELP.update({"αℓιvε": "➤ `.alive`\nUse - Check if your bot is working."})
