"""
✘ Commands Available -
• `{i}update`
    See changelogs if any update is available.
"""

from git import Repo
from telethon.tl.functions.channels import ExportMessageLinkRequest as GetLink

from . import *

POTO = "https://telegra.ph/file/28ed48fae7e23192af2cc.jpg"
LIONOP = Var.PRIVATE_GROUP_ID


@Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"update"))
async def _(e):
    m = await updater()
    branch = (Repo.init()).active_branch
    if m:
        x = await tgbot.send_file(
            LIONOP,
            poto,
            caption="• **Update Available** •",
            force_document=False,
            buttons=Button.inline("Changelogs", data="changes"),
        )
        Link = (await tgbot(GetLink(x.chat_id, x.id))).link
        await eor(
            e,
            f'<strong><a href="{Link}">[ChangeLogs]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )
    else:
        await eor(
            e,
            f'<code>Your BOT is </code><strong>up-to-date</strong><code> with </code><strong><a href="https://github.com/TeamUltroid/Ultroid/tree/{branch}">[{branch}]</a></strong>',
            parse_mode="html",
            link_preview=False,
        )


@Lion.on(events.callbackquery.CallbackQuery(data=re.compile(b"updtavail"))
async def updava(event):
    await event.delete()
    await tgbot.send_file(
        LIONOP,
        poto,
        caption="• **Update Available** •",
        force_document=False,
        buttons=Button.inline("Changelogs", data="changes"),
    )
