# For @LionHelp
"""Check if your userbot is working."""
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
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LionXsupport"


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
        lion = f"**Welcome To Lion **\n\n"
        lion += f"`{CUSTOM_ALIVE}`\n\n"
        lion += (
            f"{lionmoji} **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**: `1.17`\n{lionmoji} **Python**: `3.8.3`\n"
        )
        lion += f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚄𝙱 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**: `{lionver}`\n"
        lion += f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃**: @LionXsupport\n"
        lion += f"{lionmoji} **𝚂𝚄𝙳𝙾** : `{sudo}`\n"
        lion += f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚄𝙿𝚃𝙸𝙼𝙴**: `{uptime}`\n"
        lion += f"{lionmoji} **𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝚂𝚃𝙰𝚃𝚄𝚂**: `𝙰𝙻𝙻 𝙾𝙺 👌!`\n"
        lion += (
            f"{lionmoji} **𝙼𝚈 𝙿𝙴𝚁𝙾 𝙼𝙰𝚂𝚃𝙴𝚁** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        lion += "    [✨ Gɪᴛʜᴜʙ Rᴇᴘᴏsɪᴛᴏʀʏ ✨](https://github.com/Mdnoor786/Lion-X)"
        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALV_PIC, caption=lion, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/9c919ae0a8f31d70a8dfe.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as photo:
        img.save(img, "jpg")
        img.name = "lionuserbot.jpg"
        img.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**𝐘𝐎𝐎!! 𝐋𝐈𝐎𝐍 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{lionmoji} **𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**: `1.17`\n"
            f"{lionmoji} **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**: `1.17`\n"
            f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚄𝙱 𝚅𝙴𝚁𝚂𝙸𝙾𝙽**: `{lionver}`\n"
            f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃**: @LionXsupport\n"
            f"{lionmoji} **𝚂𝚄𝙳𝙾** : `{sudo}`\n"
            f"{lionmoji} **𝙻𝙸𝙾𝙽 𝚄𝙿𝚃𝙸𝙼𝙴**: `{uptime}`\n"
            f"{lionmoji} **𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝚂𝚃𝙰𝚃𝚄𝚂**: `All OK 👌!`\n"
            f"{lionmoji} **𝙼𝚈 𝙿𝙴𝚁𝙾 𝙼𝙰𝚂𝚃𝙴𝚁** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "[✨ gιтнυв яєρσѕιтσяу ✨](https://github.com/Mdnoor786/Lion-X)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=img)
        await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
