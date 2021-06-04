"""from Lion import bot
from Lion import ID
import heroku3
from telethon import events
from Lion import StartTime
import time
import datetime
from . import *
from telethon import events, Button, custom
import re, os
from Lion import PHOTO, Lion, BOT, VERSION
from Lion import bot
@Lion.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  OP = f"нєуу !! тнιѕ ιѕ уσυя αѕѕιѕтαит ву тєαм ℓισи\n\n"
  OP += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  OP += f"**ᴀssɪsᴛᴀɴᴛ Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
  OP += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  OP += "**ᴛʜɪs ʙᴏᴛ ɪs ᴜᴘ-ᴛᴏ-ᴅᴀᴛᴇ...**\n\n"
  OP += "**Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `1.21.1`\n\n"
  OP += "~~ **Pʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.2`!!"
  OP_b = [[Button.url("Pᴇʀᴏ ᴍᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  OP_b += [[custom.Button.inline("ʀᴇᴘᴏsɪᴛᴏʀʏ »»", data="ripo")]]
  await Lion.send_file(event.chat_id, PHOTO, caption=OP,  buttons=OP_b)




@Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"repo")))
async def callback_query_handler(event):
# inline by LEGENDX22 and PROBOY22 🔥
  pero_b = [[Button.url("Rᴇᴘᴏsɪᴛᴏʀʏ", "https://github.com/TeamLion-X/Lion-X")]]
  pero_b +=[[Button.url("ʜᴇʀᴏᴋᴜ", "https://heroku.com/deploy?template=https://github.com/Mdnoor786/Lion-X")]]
  pero = "**Sᴏᴏɴ ᴛᴜᴛᴏʀɪᴀʟ**\n"
  pero_b +=[[Button.url("Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com/@LionUB/stringsession#main.py")]]
  pero_b +=[[Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "my.telegram.org/auth")]]
  pero_b +=[[Button.url("🚑 Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ 🚑", "https://t.me/TeamLionUB"), Button.url("🚑 Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ 🚑", "https://t.me/LionXsupport")]]
  pero_b +=[[custom.Button.inline("«« ʙᴀᴄᴋ", data="cback")]]
  await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=pero_b, captions=pero)


@Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"cback")))
async def callback_query_handler(event):
  OP = f"нєуу !! тнιѕ ιѕ уσυя αѕѕנѕтαит ву тєαм ℓισи\n\n"
  OP += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
  OP += f"**ᴀssɪsᴛᴀɴᴛ Vᴇʀsɪᴏɴ** : `1.0`\n\n"
  OP += f"**Usᴇʀ** : @{bot.me.username}\n\n"
  OP += "**ᴛʜɪs ʙᴏᴛ ɪs ᴜᴘ-ᴛᴏ-ᴅᴀᴛᴇ...**\n\n"
  OP += "**Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `1.21.1`\n\n"
  OP += "~~ **Pʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.2`!!"
  OP_b = [[Button.url("Pᴇʀᴏ ᴍᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X")]]
  OP_b += [[custom.Button.inline("ʀᴇᴘᴏsɪᴛᴏʀʏ »»", data="ripo")]]
  await event.edit(text=OP, buttons=OP_b)


@Lion.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
  await xbot.send_message(event.chat, "**ʜᴇʀᴇ ɪs ʟɪᴏɴ X ᴜsᴇʀʙᴏᴛ ʀᴇᴘᴏ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @LionXsupport", buttons=[[Button.url("🗡️ Rᴇᴘᴏ 🗡️", "https://github.com/TeamLion-X/Lion-X"), Button.url("🗡️ Dᴇᴘʟᴏʏ 🗡️", "https://heroku.com/deploy?template=https://github.com/Mdnoor786/Lion-X")]])


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

@Lion.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
     return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>ＰＯＮＧ !!</i></b>\n"
        "<b>✪ тιмє тαкєи:</b> <code>{}</code>\n"
        "<b>✪ αѕѕιѕтαит υρтנмє:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
"""
