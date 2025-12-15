class script(object):
    START_TXT = """<b>Hey {}, </b>\n\n<b>I Am File To Link Generator Bot With Channel Support.\n\nSend Me Any File And Get A Direct Download Link And Streaming Link.\n\nWarning : Generating Link Of Adult Content Is Strictly Prohibited. If You Will Do, You Will Get Permanent Ban.\n\nBot Is Made By @Sujan_Ch</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.6.00 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    HELP_TXT = """<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴍᴀɴʏ ᴄᴏᴍᴍᴇɴᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ \n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ғɪʟᴇs ᴀɴᴅ I ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ʙᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋ\n\nᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ 💥\n\nғᴏʀ ᴍᴏʀᴇ, ᴜꜱᴇ /help ᴄᴏᴍᴍᴀɴᴅ\nᴍᴏʀᴇ, ᴜꜱᴇ /about ᴄᴏᴍᴍᴀɴᴅ</b>"""
    
    ADMIN_CMD_TXT = """<b>  
# Admin Only Commands 👑  
/ban - Ban a user/channel [FOR ADMINS USE ONLY]  
/unban - Unban a user/channel [FOR ADMINS USE ONLY]  
/broadcast - Send broadcast message [FOR ADMINS USE ONLY]  
/pin_broadcast - Pin broadcast message [FOR ADMINS USE ONLY]  
/restart - Restart the bot [FOR ADMINS USE ONLY]  
/stats - Show bot statistics [FOR ADMINS USE ONLY]  
/blocked - List of blocked users [FOR ADMINS USE ONLY]  
/verified_users - List of verified users [FOR ADMINS USE ONLY]  

# Premium Control 💎  
/add_premium - Grant premium access to a user [ADMINS ONLY]  
/remove_premium - Remove premium access [ADMINS ONLY]
/premium_user - All premium user [ADMINS ONLY]</b>"""

    HELP2_TXT = """<b>Hᴏᴡ ᴛᴏ Uꜱᴇ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Bᴏᴛ

Bᴀꜱɪᴄ Uꜱᴀɢᴇ:
• Sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ғʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ
• Bᴏᴛ ᴡɪʟʟ ɢᴇɴᴇʀᴀᴛᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ʟɪɴᴋꜱ
• Uꜱᴇ ᴛʜᴇꜱᴇ ʟɪɴᴋꜱ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ꜱᴛʀᴇᴀᴍ ᴄᴏɴᴛᴇɴᴛ ᴛʜʀᴏᴜɢʜ ᴏᴜʀ ꜱᴇʀᴠᴇʀꜱ
• Fᴏʀ ꜱᴛʀᴇᴀᴍɪɴɢ, ᴘᴀꜱᴛᴇ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʟɪɴᴋ ɪɴ ᴀɴʏ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ

Kᴇʏ Fᴇᴀᴛᴜʀᴇꜱ:
• Pᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛɪᴏɴ
• Dɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ꜱᴜᴘᴘᴏʀᴛ 
• Vɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍɪɴɢ ᴄᴀᴘᴀʙɪʟɪᴛʏ
• Cʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ (Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ)
• Uɴʟɪᴍɪᴛᴇᴅ ғɪʟᴇ ꜱɪᴢᴇ ꜱᴜᴘᴘᴏʀᴛ

Cʜᴀɴɴᴇʟ Uꜱᴀɢᴇ:
𝟷. Aᴅᴅ ʙᴏᴛ ᴀꜱ ᴀᴅᴍɪɴ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ
𝟸. Bᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴘʀᴏᴄᴇꜱꜱ ғɪʟᴇꜱ
𝟹. Lɪɴᴋꜱ ᴡɪʟʟ ʙᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ᴀʟʟ ᴍᴇᴅɪᴀ

⚠️ Iᴍᴘᴏʀᴛᴀɴᴛ Nᴏᴛᴇꜱ:
• Sʜᴀʀɪɴɢ ɪɴᴀᴘᴘʀᴏᴘʀɪᴀᴛᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪʟʟ ʀᴇꜱᴜʟᴛ ɪɴ ᴘᴇʀᴍᴀɴᴇɴᴛ ʙᴀɴ
• Rᴇᴘᴏʀᴛ ᴀɴʏ ɪꜱꜱᴜᴇꜱ ᴛᴏ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ

🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.

📮 Hᴇʟᴘ & Sᴜᴘᴘᴏʀᴛ:
• Uᴘᴅᴀᴛᴇꜱ: @Sujan_Ch"""

    CAPTION = """🎬 <i><a href='{}'>{}</a></i>"""
    
    LOG_TEXT = """<b>#NewUser {}
    
ID - <code>{}</code>
Nᴀᴍᴇ - {}</b>"""

    ABOUT_TXT = """<b>╔══❰ {} ❱═════❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼🤖Mʏ ɴᴀᴍᴇ : {}
║┣⪼❣️Uᴘᴅᴀᴛᴇ : <a href=https://t.me/Sujan_Ch>Bᴏᴛᴢ</a>
║┣⪼⏲️Bᴏᴛ ᴜᴘᴛɪᴍᴇ :- {}
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 
║┣⪼📚Lɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼🗒️Vᴇʀsɪᴏɴ : {} [sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ </b>"""

    AUTH_TXT = """<i><b>Dᴇᴀʀ {}!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b></i>"""
    
    CAPTION_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 Fɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href={}>{}</a></i>

<b>📦 Fɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b>📝 Nᴏᴛᴇ : Aʟʟ Gᴇɴᴇʀᴀᴛᴇᴅ Lɪɴᴋꜱ Wɪʟʟ Bᴇ ᴇxᴘɪʀᴇ Iɴ 24 Hᴏᴜʀꜱ</b>"""

    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote>\n\n💶 ꜱᴇɴᴅ /plan ᴛᴏ ʙᴜʏ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ</b>"""
    
    VERIFIED_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴠᴇʀɪꜰɪᴇᴅ ꜰᴏʀ ᴛᴏᴅᴀʏ ☺️.
ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ʟɪɴᴋs 💥.

<blockquote>ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</blockquote></b>"""
    
    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_completed"""
    
    CHECK_PLAN_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎖️ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ :</blockquote>

 ❏ 𝟶𝟹𝟿₹    ➠    𝟶𝟷 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟷𝟶₹    ➠    𝟶𝟹 ᴍᴏɴᴛʜ
 ❏ 𝟹𝟼𝟶₹    ➠    𝟷𝟸 ᴍᴏɴᴛʜ

🆔 ᴜᴘɪ ɪᴅ ➩ <code>.......</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]
 
⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏷️ <a href='https://t.me/sujan_chh'>ᴘʀᴇᴍɪᴜᴍ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.
</b>"""
    
    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {}

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ʟɪɴᴋs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                       
❏ ᴜɴʟɪᴍᴛᴇᴅ ғɪʟᴇs ɪɴ ᴀ ᴅᴀʏ                                                   
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""
