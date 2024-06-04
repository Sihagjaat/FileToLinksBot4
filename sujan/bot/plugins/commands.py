# (c) @adarsh

from sujan.bot import StreamBot
from sujan.vars import Var
import logging
logger = logging.getLogger(__name__)
from sujan.bot.plugins.stream import MY_PASS
from sujan.utils.human_readable import humanbytes
from sujan.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from sujan.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup
from sujan.vars import bot_name , sujan_channel , sujan_grp

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["ɢᴇᴛ ᴍᴏᴠɪᴇs ғɪʟᴇs ғʀᴇᴇ"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                
                ["ɢᴇᴛ ᴍᴏᴠɪᴇs ғɪʟᴇs ғʀᴇᴇ"]
                        
            ],
            resize_keyboard=True
        )


SRT_TXT = """<b>Hɪ {}!,
I Aᴍ Fɪʟᴇ Tᴏ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ Wɪᴛʜ Cʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.
Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ Aɴᴅ Gᴇᴛ A Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ Aɴᴅ Sᴛʀᴇᴀᴍᴀʙʟᴇ Lɪɴᴋ.!
Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : <a href='https://t.me/Sujan_Bots'>Sᴜᴊᴀɴ</a></b>"""

@StreamBot.on_message(filters.command("start") & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n User Id : {m.from_user.id}\n\n By @Sujan_BotZ"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/5ef57116d62683f872a8c.jpg",
                caption=""""<b>Hᴇʏ Tʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ ! 😊\n\nDᴜᴇ Tᴏ Sᴇʀᴠᴇʀ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Oᴜʀ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ Nᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
             )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/Sujan_Bots'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://graph.org/file/d1aa884d79172a1f5587c.jpg",
    caption= SRT_TXT.format(m.from_user.mention(style="md")),
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 📯", url=sujan_channel)],
            [
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ 🎛️", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ 💡", callback_data="help")
            ]
        ]
    )
)
@StreamBot.on_message(filters.command("help") & filters.private )
async def help_cd(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n User Id : {m.from_user.id}\n\n By @Sujan_BotZ"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/5ef57116d62683f872a8c.jpg",
                caption=""""<b>Hᴇʏ Tʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Mᴇ ! 😊\n\nDᴜᴇ To Sᴇʀᴠᴇʀ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Oᴜʀ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
             )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/Sujan_Bots'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://graph.org/file/d1aa884d79172a1f5587c.jpg",
    caption=f"<b>Wᴇ Dᴏɴ'ᴛ Nᴇᴇᴅ Mᴀɴʏ <a href='https://t.me/Sujan_BotZ'>ᴄᴏᴍᴍᴀɴᴅs</a> Tᴏ Usᴇ Tʜɪs Bᴏᴛ 🤩.\n\nJᴜsᴛ Sᴇɴᴅ Mᴇ Vɪᴅᴇᴏ Fɪʟᴇs Aɴᴅ ɪ Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ & Sᴛʀᴇᴀᴍᴀʙʟᴇ Lɪɴᴋ.\n\nOʀ Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Iɴ Yᴏᴜʀ Cʜᴀɴɴᴇʟ.\n\nJᴜsᴛ Aᴅᴅ Mᴇ Aɴᴅ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ Aɴᴅ Sᴇᴇ Mʏ Mᴀɢɪᴄ 🪄</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 📯", url=sujan_channel)
            ],
            [
                InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),

            ]

        ]
    )
)
            
@StreamBot.on_message(filters.command('ban') & filters.user(Var.OWNER_ID))
async def do_ban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    reason = message.text.split(" ", 2)[2] if len(message.text.split(" ", 2)) > 2 else None
    if not userid:
        return await message.reply('<b>ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ\n\nᴇx : /ban (user/channel_id) (banning reason[Optional]) \nʀᴇᴀʟ ᴇx : <code>/ban 1234567899</code>\nᴡɪᴛʜ ʀᴇᴀsᴏɴ ᴇx:<code>/ban 1234567899 seding adult links to bot</code>\nᴛᴏ ʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ :\n<code>/ban CHANEL_ID</code>\nᴇx : <code>/ban -1001234567899</code></b>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 👀</b>")
    banSts = await db.ban_user(userid)
    if banSts == True:
        await text.edit(
    text=f"<b><code>{userid}</code> ʜᴀs ʙᴇᴇɴ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ\n\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴀɴ ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendAlert_{userid}_{reason if reason else 'no reason provided'}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"noAlert_{userid}"),
            ],
        ]
    ),
)
    else:
        await text.edit(f"<b>Cᴏɴᴛʀᴏʟʟ ʏᴏᴜʀ ᴀɴɢᴇʀ ʙʀᴏ...\n<code>{userid}</code> ɪs ᴀʟʀᴇᴀᴅʏ ʙᴀɴɴᴇᴅ !!</b>")
     return

@StreamBot.on_message(filters.command('unban') & filters.user(Var.OWNER_ID))
async def do_unban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    if not userid:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀɴ ɪᴅ\nᴇx : <code>/unban 1234567899<code>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 🥱</b>")
    unban_chk = await db.is_unbanned(userid)
    if  unban_chk == True:
        await text.edit(text=f'<b><code>{userid}</code> ɪs ᴜɴʙᴀɴɴᴇᴅ\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴛʜᴇ ʜᴀᴘᴘʏ ɴᴇᴡs ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>',
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendUnbanAlert_{userid}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"NoUnbanAlert_{userid}"),
            ],
        ]
    ),
)

    elif unban_chk==False:
        await text.edit('<b>ᴜsᴇʀ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ ʏᴇᴛ.</b>')
    else :
        await text.edit(f"<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ.\nʀᴇᴀsᴏɴ : {unban_chk}</b>")
                
@StreamBot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "close_data":
        await query.message.delete()


    if data == "start":
        await query.message.edit_caption(
        caption= SRT_TXT.format(query.from_user.mention(style="md")),
        reply_markup=InlineKeyboardMarkup(
                [
            [InlineKeyboardButton("Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 📯", url=sujan_channel)],
            [
                 InlineKeyboardButton("Aʙᴏᴜᴛ 🎛️", callback_data="about"),
                 InlineKeyboardButton("Hᴇʟᴘ 💡", callback_data="help")
            ]
        ]
            )
        )

    elif data == "about":
        await query.message.edit_caption(
            caption=f"<b>Mʏ Nᴀᴍᴇ :<a href='https://t.me/TG_FileToLinkXbot'>{bot_name}</a>\nOᴡɴᴇʀ : <a href='https://t.me/Sujan_Bots'>ꜱᴜᴊᴀɴ</a>\nHᴏsᴛᴇᴅ ᴏɴ : Hᴇʀᴏᴋᴜ\nᴅᴀᴛᴀʙᴀsᴇ : Mᴏɴɢᴏ ᴅʙ\nLᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
        caption=f"<b>Nᴏ Nᴇᴇᴅ Mᴀɴʏ ᴄᴏᴍᴍᴀɴᴅs Tᴏ Usᴇ Tʜɪs Bᴏᴛ 🤩.\n\nJᴜsᴛ Sᴇɴᴅ Mᴇ Vɪᴅᴇᴏ Fɪʟᴇs Aɴᴅ ɪ Wɪʟʟ Gɪᴠᴇ Yᴏᴜ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ & Sᴛʀᴇᴀᴍᴀʙʟᴇ Lɪɴᴋ.\n\nOʀ Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Iɴ Yᴏᴜʀ Cʜᴀɴɴᴇʟ.\n\nJᴜsᴛ Aᴅᴅ Mᴇ Aɴᴅ Mᴀᴋᴇ Mᴇ Aᴅᴍɪɴ Aɴᴅ Sᴇᴇ Mʏ Mᴀɢɪᴄ 🪄</b>",
            reply_markup=InlineKeyboardMarkup(
[[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]            )
        )

    elif data == "aboutDev":
        # please don't steal credit
        await query.message.edit_caption(
            caption=f"<b>Hɪ Dᴇᴀʀ...\nɪ'ᴍ <a href='https://t.me/Sujan_Bots'>ꜱᴜᴊᴀɴ</a>\nɪ Aᴍ Tʜᴇ Aᴅᴍɪɴ Oғ Tʜɪs Bᴏᴛ..Aɴᴅ ɪ Mᴀᴅᴇ Tʜᴇ Bᴏᴛ Bʏ Hᴇʟᴘ Oғ <a href='https://github.com/adarsh-goel'>Aᴅᴀʀsʜ Bʀᴏ</a>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]            )
        )
