"""





from git import Repo
from telethon.tl.functions.channels import ExportMessageLinkRequest as GetLink

from . import *

LIONPIC = "resources/inline.jpg"
CL = udB.get("INLINE_PIC")
if CL:
    LIONPIC = CL


@ultroid_cmd(pattern="update$")
async def _(e):
    m = await updater()
    branch = (Repo.init()).active_branch
    if m:
        x = await lion.asst.send_file(
            int(udB.get("LOG_CHANNEL")),
            LIONPIC,
            caption="• **Update Available** •",
            force_document=False,
            buttons=Button.inline("Changelogs", data="changes"),
        )
        Link = (await lion(GetLink(x.chat_id, x.id))).link
        await eor(
            e,
            f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
    else:
        await eor(
            e,
            f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/Mdnoor786/Lion-X/tree/{branch}">[{branch}]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )


@callback("updtavail")
@owner
async def updava(event):
    await event.delete()
    await lion.asst.send_file(
        int(udB.get("LOG_CHANNEL")),
        LIONPIC,
        caption="• **Update Available** •",
        force_document=False,
        buttons=Button.inline("Changelogs", data="changes"),
    ) 
"""
