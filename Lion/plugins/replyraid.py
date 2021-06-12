import asyncio
import random

from . import catmemes

que = {}


@Lion.on(admin_cmd(incoming=True))
@Lion.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    counter = int(random.choice(catmemes.NUMBER))
    if counter == 0:
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(
                entity=event.chat_id,
                message="""{}""".format(random.choice(catmemes.RRAID)),
                reply_to=event.message.id,
            )
    if counter == 1:
        caption = random.choice(catmemes.RRAID)
        async with event.client.action(event.chat_id, "typing"):
            await event.client.send_message(event.chat_id, caption)


@Lion.on(admin_cmd(pattern="replyraid(?: |$)(.*)"))
@Lion.on(sudo_cmd(pattern="replyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@Lion.on(admin_cmd(pattern="dreplyraid(?: |$)(.*)"))
@Lion.on(sudo_cmd(pattern="dreplyraid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")


CMD_HELP.update(
    {
        "spam": "**Plugin : **`replyraid`\
        \n\n**  •  Syntax : **`.replyraid <username>`\
        \n**  •  Function : **__ Replies the user globally on every chat with random abuses. __\
        \n\n**  •  Syntax : **`.dreplyraid <username>`\
        \n**  •  Function : **__ Deactivates the reply raid. __\
        \n\n\n**Note : Spam at your own risk !!**"
    }
)
