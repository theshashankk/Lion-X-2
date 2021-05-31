# Ported from other Telegram UserBots for Lion//Made for Lion
# Kangers, don't remove this line
# @its_xditya

"""Available Commands:
.info
"""

import asyncio

from Lion import CMD_HELP


@Lion.on(admin_cmd(pattern="info"))
@Lion.on(sudo_cmd(pattern="info", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Visit this page to know more about Lion.":
    await eor(event, "Thanks")
    animation_chars = ["**Lion**", "[More Info](https://telegra.ph/Lion-07-08)"]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await eor(event, animation_chars[i % 18])


CMD_HELP.update({"about": "➟ .info\nUse - Get to know about your bot."})
