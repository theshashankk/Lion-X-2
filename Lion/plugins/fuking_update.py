from telethon import events
from os import remove, execle, path, makedirs, getenv, environ, execl
from shutil import rmtree
import asyncio
import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from Lion import CMD_HELP, bot
from Lion.utils import admin_cmd, sudo_cmd

UPSTREAM_REPO_URL = "https://github.com/Mdnoor786/Lion-X"
HEROKU_API_KEY = Var.HEROKU_API_KEY
HEROKU_APP_NAME = Var.HEROKU_APP_NAME

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'Xsetup.txt')

async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} by <{c.author}>\n'
    return ch_log

async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)

@Lion.on(admin_cmd(pattern="update ?(.*)", outgoing=True))
async def upstream(ups):
    "For .update command, check if the bot is up to date, update if specified"
    conf = ups.pattern_match.group(1)
    await ups.edit("Wᴀɪᴛ ʟᴇᴍᴍᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ....")
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "Oᴏᴘss.. Uᴘᴅᴀᴛᴇʀ ᴄᴀɴɴᴏᴛ ᴄᴏɴᴛɪɴᴜᴇ ᴅᴜᴇ ᴛᴏ"
        txt += "Sᴏᴍᴇ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit(f'{txt}\nᴅɪʀᴇᴄᴛᴏʀʏ {error} ɪs ɴᴏᴛ ғᴏᴜɴᴅ')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit(f'{txt}\nEᴀʀʟʏ ғᴀɪʟᴜʀᴇ! {error}')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != "now":
            await ups.edit(f"**Hᴇʏʏ ᴍʏ ᴘᴇʀᴏ ᴍsᴛᴇʀ!!!**👀👀\n__Tᴏ ɢᴇᴛ ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴜᴘᴅᴀᴛᴇ ᴏғ__ \n©ᴛᴇᴀᴍʟɪᴏɴᴜʙ\n\n Dᴏ |`.update now`| ")
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit(
            f'**[UPDATER]:**` ʟᴏᴏᴋꜱ ʟɪᴋᴇ ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ʏᴏᴜʀ ᴏᴡɴ ᴄᴜꜱᴛᴏᴍ ʙʀᴀɴᴄʜ ({ac_br}). '
            'ʟᴏᴏᴋꜱ ʟɪᴋᴇ ʏᴏᴜ ᴀʀᴇ ᴜꜱɪɴɢ ʏᴏᴜʀ ᴏᴡɴ ᴄᴜꜱᴛᴏᴍ ʙʀᴀɴᴄʜ '
            'ᴡʜɪᴄʜ ʙʀᴀɴᴄʜ ɪꜱ ᴛᴏ ʙᴇ ᴍᴇʀɢᴇᴅ. '
            'Pʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴏᴜᴛ ᴛʜᴇ ᴏғғɪᴄɪᴀʟ ʙʀᴀɴᴄʜ`')
        repo.__del__()
        return
    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')
    if not changelog and not force_update:
        await ups.edit(
            f'\n**{ac_br} ʏᴏᴏ!! ᴜ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴄᴢ.. ᴜʀ ʙᴏᴛ ɪs ᴜᴘ-ᴛᴏ-ᴅᴀᴛᴇ..**\n')
        repo.__del__()
        return
    if conf != "now" and not force_update:
        changelog_str = f'**Wᴇ ғᴏᴜɴᴅ ɴᴇᴡ ᴜᴘᴅᴀᴛᴇ ɪɴ [{ac_br}]:\n\nCHANGELOG:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await ups.edit("`Cʜᴀɴɢᴇʟᴏɢ ɪs ᴛᴏᴏ ʙɪɢ, ᴛᴏ ᴠɪᴇᴡ ᴛʜᴇ ғɪʟᴇ.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await ups.client.send_file(
                ups.chat_id,
                "output.txt",
                reply_to=ups.id,
            )
            remove("output.txt")
        else:
            await ups.edit(changelog_str)
        await ups.respond("Dᴏ `.update now` Tᴏ ᴜᴘᴅᴀᴛᴇ")
        return
    if force_update:
        await ups.edit('Fᴏʀᴄᴇ-sʏɴᴄɪɴɢ ᴛᴏ ʟᴀᴛᴇsᴛ sᴛᴀʙʟᴇ ʟɪᴏɴ ᴜʙ ᴄᴏᴅᴇ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴍᴀsᴛᴇʀ ʟᴇᴍᴇᴇ ᴜᴘᴅᴀᴛᴇ...😅😅')
    else:
        await ups.edit('`Uᴘᴅᴀᴛɪɴɢ ʏᴏᴜʀ ʟɪᴏɴ ᴜʙ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ....Yᴏᴜ ᴀʀᴇ ʙᴇsᴛ ᴍᴀsᴛᴇʀ🤗😇')
    if HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await ups.edit('Pʟᴇᴀsᴇ sᴇᴛ ᴛʜᴇ `HEROKU_APP_NAME` ᴠᴀʀɪᴀʙʟᴇ ᴛᴏ ʙᴇ ᴀʙʟᴇ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʟɪᴏɴ ᴜsᴇʀʙᴏᴛ.')
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                f'{txt}\n`ɪɴᴠᴀʟɪᴅ ʜᴇʀᴏᴋᴜ ᴄʀᴇᴅᴇɴᴛɪᴀʟ ғᴏʀ ᴜᴘᴅᴀᴛɪɴɢ ʟɪᴏɴ ᴜʙ ᴅʏɴᴏ.`'
            )
            repo.__del__()
            return
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
             await ups.edit("`✘ ᴜᴘᴅᴀᴛɪɴɢ ʏᴏᴜʀ ʟɪᴏɴ ᴜʙ ✘\n\nᴘʟᴇᴀsᴇ ᴡᴀɪᴛ 2-3 ᴍɪɴ ᴛʜᴀɴ ᴛʀʏ .alive\n\n**𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 ©𝚃𝙴𝙰𝙼𝙻𝙸𝙾𝙽𝚄𝙱**")
                remote.push(refspec="HEAD:refs/heads/main", force=True)
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        reqs_upgrade = await update_requirements()
        await ups.edit('`Sᴇᴄᴄᴇssғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ!\n'
                       'Gɪᴍᴍᴇ ᴀ sᴇᴄᴏɴᴅ ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ...`')
        # Spin a new instance of bot
        args = [sys.executable, "-m", "Lion"]
        execle(sys.executable, *args, environ)
        return
    

CMD_HELP.update({
    'updater':
    ".update\
\nUsage: Checks if the main userbot repository has any updates and shows a changelog if so.\
\n\n.update now\
\nUsage: Updates your userbot, if there are any updates in the main userbot repository."
})
