#    Lion - UserBot
#    Copyright (C) 2020 Lion

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Based of AFK by @SpEcHIDe
# Media Afk, Time, by @xditya
"""
AFK Plugin for Lion
Syntax: .afk REASON

import asyncio
import os
from datetime import datetime

from telegraph import Telegraph, upload_file
from telethon import Button, events
from telethon.tl import functions, types

from Lion import CMD_HELP
from Lion.LionConfig import Config, Var

# --=============================================--#
global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start  # pylint:disable=E0602
global afk_end  # pylint:disable=E0602
# --=============================================--#
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}
BOTLOG = True
CUSTOM_AFK = Var.CUSTOM_AFK if Var.CUSTOM_AFK else "I am currently unavailable!"
botname = Var.TG_BOT_USER_NAME_BF_HER
if botname.startswith("@"):
    MYBOT = botname
else:
    MYBOT = f"@{botname}"
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]
# --=============================================--#


@Lion.on(
    events.NewMessage(incoming=True, func=lambda e: bool(e.mentioned or e.is_private))
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = afk_end - afk_start
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason is not None and lion == "True":
            message_to_reply = "**AFK**\n{}\n\n**Last active** `{}` **ago.**\n\n**Reason** : {}".format(
                CUSTOM_AFK, endtime, reason
            )
        elif lion == "False":
            message_to_reply = "**AFK**\n{}\n\n**Last active** `{}` **ago.**\n\n**Reason** - {}".format(
                CUSTOM_AFK, endtime, reason
            )
        else:
            message_to_reply = "**AFK**\n{}\n\n**Last active** {} **ago.**".format(
                CUSTOM_AFK, endtime
            )
        if event.chat_id not in Config.UB_BLACK_LIST_CHAT:
            msg = await event.reply(message_to_reply)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        last_afk_message[event.chat_id] = msg
        chat = await event.get_chat()
        if Var.PRIVATE_GROUP_ID:
            await asyncio.sleep(5)
            if not event.is_private:
                mssgtosend = f"#AFK \nYou were tagged in `{chat.title}`"
                try:
                    await tgbot.send_message(
                        Var.PRIVATE_GROUP_ID,
                        mssgtosend,
                        buttons=[
                            Button.url(
                                "Go to Message",
                                url=f"https://t.me/c/{chat.id}/{event.message.id}",
                            )
                        ],
                    )
                except BaseException:
                    await Lion.send_message(
                        Var.PRIVATE_GROUP_ID,
                        f"Please add {MYBOT} here for afk tags to work.",
                    )


@Lion.on(admin_cmd(pattern=r"afk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    global reason
    global lion
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    tele = "False"
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if not USER_AFK:
        if event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            media = await Lion.download_media(reply_message, "AFK_media")
            try:
                url = upload_file(media)
                os.remove(media)
            except BaseException:
                pass
            input_str = event.pattern_match.group(1)
            if url:
                if input_str is not None:
                    tele = "True"
                    reason = f"`{input_str}`[‎‏‏‎ ‎](https://telegra.ph/{url[0]})"
                else:
                    tele = "False"
                    reason = f"[‎‏‏‎ ‎](https://telegra.ph/{url[0]})"
            else:
                if input_str is not None:
                    reason = f"`{input_str}`"
        else:
            input_str = event.pattern_match.group(1)
            reason = f"`{input_str}`"
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.now()
        USER_AFK = f"on: {reason}"
        if reason:
            await event.edit(
                f"`Your status has been set to AFK.`\n**Reason** - {reason}"
            )
            await asyncio.sleep(5)
            await event.delete()
        else:
            await event.edit("`Your status has been set to AFK.`")
            await asyncio.sleep(5)
            await event.delete()
        if BOTLOG:
            if reason:
                await event.client.send_message(
                    Var.PRIVATE_GROUP_ID,
                    f"#AFK \nAFK - Active\nReason - {reason}",
                )
            else:
                await event.client.send_message(
                    Var.PRIVATE_GROUP_ID,
                    f"#AFK \nAFK - Active\nReason - None Specified.",
                )


@Lion.on(events.NewMessage(outgoing=True))
async def set_not_afk(event):
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = afk_end - afk_start
        time = int(total_afk_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        else:
            if h > 0:
                endtime += f"{h}h {m}m {s}s"
            else:
                endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if "afk" not in current_message and "on" in USER_AFK:
        shite = await event.client.send_message(
            event.chat_id,
            f"`I'm back!\nWas afk for {endtime}`",
        )
        USER_AFK = {}
        afk_time = None
        await asyncio.sleep(5)
        await shite.delete()
        if BOTLOG:
            await event.client.send_message(
                Var.PRIVATE_GROUP_ID, f"#AFK \n`AFK - Disabled\nAFK for {endtime}`"
            )


CMD_HELP.update(
    {
        "afk": "➟ `.afk` <optional reason>\nUse - Sets your status to AwayFromKeyboard. The bot will reply when you are tagged in groups. Will be auto turned off when you message again!"
    }
)
"""
import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types

from Lion import CMD_HELP
from Lion.utils import admin_cmd

global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global last_afk_message  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
afk_start = {}

# Originally by @NOOB_GUY_OP
# I think its first for DARKCOBRA


@Lion.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        shite = await borg.send_message(
            event.chat_id,
            "__ɪᴍ ʙᴀᴄᴋ ᴀʟɪᴠᴇ!__\n**Nᴏ ʟᴏɴɢᴇʀ ᴀғᴋ.**\n `Wᴀs Aғᴋ Fᴏʀ:``"
            + total_afk_time
            + "`",
            file=pic,
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE 👀\nSᴇᴛ ᴀғᴋ ᴍᴏᴅᴇ ғᴀʟsᴇ\n"
                + "__Bᴀᴄᴋ ᴀʟɪᴠᴇ!__\n**Nᴏ ʟᴏɴɢᴇʀ ᴀғᴋ.**\n `Wᴀs ᴀғᴋ ғᴏʀ:``"
                + total_afk_time
                + "`",
                file=pic,
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602 # Originally by @NOOB_GUY_OP
                # I think its first for DARKCOBRA
                event.chat_id,
                "Pʟᴇᴀsᴇ sᴇᴛ `PRIVATE_GROUP_BOT_API_ID` "
                + "Fᴏʀ ᴛʜᴇ ᴘʀᴏᴘᴇʀ ғᴜɴᴄᴛɪᴏɴɪɴɢ ᴏғ ᴀғᴋ "
                + "Bᴏss sᴇᴛ ɪᴛ.\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await shite.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "mafk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None  # Originally by @NOOB_GUY_OP
        # I think its first for DARKCOBRA
        message_to_reply = (
            f"__Mʏ ʙᴏss ɪs ᴀғᴋ ɴᴏᴡ ғʀᴏᴍ sɪɴᴄᴇ__ `{total_afk_time}`\nWʜᴇʀᴇ ɪs ʜᴇ: I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴍᴏɪ ғʀɪᴇɴᴅ..Hᴇ ɪs ᴛᴏ ʙᴜᴢʏ ᴘᴇʀsᴏɴ.."
            + f"\n\n__I ᴄᴀɴ'ᴛ ɢɪʙ ɢᴜᴀʀᴀɴᴛᴇᴇ ʏᴏᴜ ᴛʜᴀᴛ ᴡʜᴇɴ ʜᴇ ᴡɪʟʟ ᴄᴏᴍ..__\n**ʀɛǟֆօռ**: {reason}"
            if reason
            else f"**Hᴇʏʏ!**\n__Mʏ ᴍᴀsᴛᴇʀ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ. Sɪɴᴄᴇ ᴡʜᴇɴ, ʏᴏᴜ ᴀsᴋ? Fᴏʀ {total_afk_time} ɪ ᴛʜɪɴᴋ.__\n\nᴡʜᴇɴ ʜᴇ ᴡɪʟʟ ᴄᴏᴍᴇ ʙᴀᴄᴋ? Sᴏᴏɴ __Wʜᴇɴᴇᴠᴇʀ I ғᴇᴇʟ ʟɪᴋᴇ ᴄᴏᴍɪɴɢ ʙᴀᴄᴋ__**(o(^▽^)o)**  "
        )
        msg = await event.reply(message_to_reply, file=pic)
        await asyncio.sleep(5)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"afk (.*) (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    global pic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()  # Originally by @NOOB_GUY_OP
    # I think its first for DARKCOBRA
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    pic = event.pattern_match.group(2)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )  # Originally by @NOOB_GUY_OP
        # I think its first for DARKCOBRA
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason} {pic}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id,
                f"**I Sʜᴀʟʟ ɢᴏɪɴɢ ᴀғᴋ!** __ᴄᴢ ~ {reason}__",
                file=pic,
            )
        else:
            await borg.send_message(event.chat_id, f"**I ᴀᴍ ɢᴏɪɴɢ ᴀғᴋ!**", file=pic)
        await asyncio.sleep(5)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#MAFKTRUE \nSet MAFK mode to True, and Reason is {reason}",
                file=pic,
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CMD_HELP.update(
    {
        "mafk": "__**PLUGIN NAME :** Afk__\
\n\n📌** CMD ➥** `.mafk` [Optional Reason]\
"
    }
)
