# special thanks to Sur_vivor
# Re-written for Lion by @its_xditya

import time
from datetime import datetime

from Lion import CMD_HELP
from Lion.__init__ import StartTime
from Lion.plugins import OWNER_ID, LION


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


# @command(pattern="^.ping$")


@Lion.on(admin_cmd(pattern="ping$"))
@Lion.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    x = await eor(event, "⛝ ＰＯＮＧ! ⛝")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await x.edit(
        f"⪼ **ριηg** : `{ms}`\n⪼ **υρтιмε** : `{uptime}`\n⪼ **мү мαsтεя** : [{LION_NAME}](tg://user?id={OWNER_ID})"
    )


CMD_HELP.update({"ping": ".ping\nUse - See the ping stats and uptime of userbot."})
"""
