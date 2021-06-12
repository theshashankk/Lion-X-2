#  (c)2020 Lion
#
# You may not use this plugin without proper authorship and consent from @LionSupport
#
from telethon.tl import functions

from Lion import ALIVE_NAME, CMD_HELP
from Lion.utils import admin_cmd

TELENAME = ALIVE_NAME if ALIVE_NAME else "Lion"

# set your mood


@Lion.on(admin_cmd(pattern="mood ((.|\n)*)"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = f"「{names}」 {ALIVE_NAME}"
    last_name = ""
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("Mood set xD")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


# reset back


@Lion.on(admin_cmd(pattern="resetmood"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    first_name = f"{ALIVE_NAME}"
    last_name = ""
    try:
        await borg(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("Mood reset xD")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


CMD_HELP.update(
    {
        "mood": ".mood <text>\nUse - Sets name to [text] ALIVE_NAME\
        .resetmood - revert changes"
    }
)
