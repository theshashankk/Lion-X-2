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
    else "𝚈𝙾𝙾!! 𝚈𝙾𝚄𝚁 𝙻𝙸𝙾𝙽 𝚄𝙱 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴"
)
lionmoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✘**"
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

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"

BOT_USERNAME = VAR.TG_BOT_USER_NAME_BF_HER if TG_BOT_USER_NAME_BF_HER else none
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LionXsupport"

SHASANKXD = VAR.ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/9c919ae0a8f31d70a8dfe.jpg"

theshashank = "**үσσ!! ℓιση υsεявσт ιs αℓιvε**\n\n"
theshashank += f"**𝐌𝐘 𝐏𝐄𝐑𝐎 𝐌𝐀𝐒𝐓𝐄𝐑**          : {DEFAULTUSER}\n"
theshashank += f"𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 : [here](t.me/LionXsupport)\n"  
theshashank += f"𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : [here](LionXupdates)\n\n"
theshashank += f"`𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽`       : 1.0\n"
theshashank += "`𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽`           : 3.9.0\n\n"
theshashank += "`𝐘𝐎𝐔𝐑 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓👾`          : {BOT_USERNAME} \n"
theshashank += "𝙈𝙔 𝘿𝙀𝙑 👇👇\n"
theshashank += "[✘ 𝐒𝐇𝐀𝐒𝐇𝐀𝐍𝐊 ✘](t.me/shashankxD\n"
theshashank += "[✘ 𝐌𝐃 𝐍𝐎𝐎𝐑 ✘](t.me/SimpleBoy786)"



@Lion.on(admin_cmd(outgoing=True, pattern="alive"))
@Lion.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def theshashank(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, SHASHANKXD, caption=theshashank)
    await alive.delete()
