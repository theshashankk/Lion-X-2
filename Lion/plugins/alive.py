import asyncio
import time

from telethon import version
from userbot.utils import admin_cmd, sudo_cmd
from Lion import Config, Var
from Lion import StartTime

# ======CONSTANTS=========#
CUSTOM_ALIVE = Var.CUSTOM_ALIVE if Var.CUSTOM_ALIVE else "ʏօօ!! ʟɨօռ ʊֆɛʀɮօȶ ɨֆ ǟʟɨʋɛ!"
ALIVE_NAME = Var.ALIVE_NAME if Var.ALIVE_NAME else "ℓιση x υsεя"
# =========================#
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση x υsεя"

# Thanks to Sipak bro and Aryan..
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
# mod For Coffin With Credit
global fuk
fuk = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/33f7e8dc3bb38cbe25991.jpg"
file2 = "https://telegra.ph/file/25e8b6ac76b208a9b87aa.jpg"
file3 = "https://telegra.ph/file/d65773b873c889b7ebcbe.jpg"
file4 = "https://telegra.ph/file/a1f313f984cd6937f7986.jpg"
""" =======================CONSTANTS====================== """


@Lion.on(admin_cmd(pattern=r"alive"))
@Lion.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def hmm(yes):
    await yes.get_chat()
    global fuk
    fuk = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - StartTime))
    pm_caption = "** ʟɨօռ Ӽ ʊֆɛʀɮօȶ ɨֆ օռʟɨռɛ **\n\n"
    pm_caption += "**Mʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
    pm_caption += "✗ Aʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
    pm_caption += f"✗ **𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉** ☞ {version.__version__}\n"
    pm_caption += "✗ **𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝘾𝙃𝘼𝙉𝙉𝙀𝙇** ☞ [ᴊᴏɪɴ](https://t.me/TeamLionUB)\n"
    pm_caption += "✗ **𝙇𝙄𝘾𝙀𝙉𝙎𝙀**  ☞ [𝚃𝙴𝙰𝙼 𝙻𝙸𝙾𝙽 𝚄𝙱](https://github.com/TeamLion-X)\n"
    pm_caption += (
        "✗ **𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔** ☞ [𝙻𝙸𝙾𝙽 𝚄𝙱](https://github.com/teamlion-X/Lion-X)\n\n"
    )
    pm_caption += f"✗ **𝙇𝙄𝙊𝙉 𝙐𝙋𝙏𝙄𝙈𝙀** ☞ {uptime}\n\n"
    pm_caption += f"✗ **𝙈𝙔 𝙋𝙀𝙍𝙊 𝙈𝘼𝙎𝙏𝙀𝙍** ☞ [{DEFAULTUSER}](tg://user?id={fuk})\n"
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
