class script(object):
    START_TXT = """<b>𝖸𝗈 {}, 𝖭𝗂𝖼𝖾 𝖳𝗈 𝖬𝖾𝖾𝗍 𝖸𝗈𝗎</b>
I'm Powerful Auto-Filter Bot You Can Use Me As A Auto-filter in Your Group .... 

Its Easy To Use Me Just Add Me To Your Group As Admin Thats All i will Provide Movies There.

More Help Check Help Button Below
"""

    HELP_TXT = """<b>How To Use Me?</b>
    
○ Search Using Inline Mode
    This Methord Works On Any Chat, Just Type @piroxfilesrobot And Then Leave A Space And Search Any Movie You Want.
    
○ Or Just Send Correct Movie Name Without Spelling Mistakes I Will Send Movies To You.

<a href='https://t.me/piro_tuts/13'>Watch Using Tutorial..</a>"""

    ABOUT_TXT = """<b>○ 𝖬𝗒 𝖭𝖺𝗆𝖾: {}
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/piroxbots'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥 
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : VPS
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖥𝗋𝖾𝖾 𝖳𝗂𝖾𝗋</a>"""

    SOURCE_TXT = """<b>NOTE:</b>
𝖲𝗉𝖾𝖼𝗂𝖺𝗅 𝖳𝗁𝖺𝗇𝗄𝗌 𝗍𝗈 𝖤𝗏𝖺𝖬𝖺𝗋𝗂𝖺 𝖣𝖾𝗏𝗌 𝖥𝗈𝗋 𝖳𝗁𝖾 𝖡𝖺𝗌𝖾 𝖢𝗈𝖽𝖾𝗌

<b>𝖱𝖾𝖿𝖾𝗋𝖾𝗇𝖼𝖾 𝖱𝖾𝗉𝗈</b>

~ Source: https://github.com/ritheshrkrm/PiroAutoFilterBot""" #please don't change repo link give credit :)

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
⚡️ Free Storage: <code>{}</code>
🚀 Uptime: <code>{}</code>

<b>😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @piroxbots</b>"""


    LOG_TEXT_G = """#NewGroup
𝖦𝗋𝗈𝗎𝗉 = {}(<code>{}</code>)
𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 = <code>{}</code>
𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 - {}"""

    LOG_TEXT_P = """#NewUser
𝖨𝖽 - <code>{}</code>
𝖭𝖺𝗆𝖾 - {}"""

    ALRT_TXT = """Hello {},
This is Not Your Request
Request Yourself Please...!!!"""

    OLD_ALRT_TXT = """Hey {},
You Are Using One Of Old Message, 
Request Again...!!!"""

    CUDNT_FND = """<b>
𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍
𝖣𝗂𝖽 𝗒𝗈𝗎 𝗆𝖾𝖺𝗇 𝖺𝗇𝗒 𝗈𝗇𝖾 𝗈𝖿 𝗍𝗁𝖾𝗌𝖾?</b>"""

    I_CUDNT = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @raixchat</i></b>"""

    I_CUD_NT = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @raixchat</i></b>"""

    MVE_NT_FND = """❌ <b>𝖨 𝖼𝗈𝗎𝗅𝖽𝗇'𝗍 𝖿𝗂𝗇𝖽 𝖺𝗇𝗒𝗍𝗁𝗂𝗇𝗀 𝗋𝖾𝗅𝖺𝗍𝖾𝖽 𝗍𝗈 𝗍𝗁𝖺𝗍</b>\n\n‼ <b><i>𝖱𝖾𝗉𝗈𝗋𝗍 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 ▶ @raixchat</i></b>"""

    TOP_ALRT_MSG = """𝖢𝗁𝖾𝖼𝗄𝗂𝗇𝗀 𝖿𝗈𝗋 𝗊𝗎𝖾𝗋𝗒 𝗂𝗇 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾..."""

    MELCOW_ENG = """<b>Hey {}, Welcome to {}</b> 

• 𝖭𝗈 𝖯𝗋𝗈𝗆𝗈, 𝖭𝗈 𝖯𝗈𝗋𝗇, 𝖭𝗈 𝖮𝗍𝗁𝖾𝗋 𝖠𝖻𝗎𝗌𝖾𝗌
• 𝖠𝗌𝗄 𝖸𝗈𝗎𝗋 𝖬𝗈𝗏𝗂𝖾𝗌 𝖶𝗂𝗍𝗁 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀
• 𝖲𝗉𝖺𝗆𝗆𝖾𝗋𝗌 𝖲𝗍𝖺𝗒 𝖠𝗐𝖺𝗒
• 𝖥𝖾𝖾𝗅 𝖥𝗋𝖾𝖾 𝖳𝗈 𝖱𝖾𝗉𝗈𝗋𝗍 𝖠𝗇𝗒 𝖤𝗋𝗋𝗈𝗋𝗌 𝖳𝗈 𝖠𝖽𝗆𝗂𝗇𝗌 𝗎𝗌𝗂𝗇𝗀 @admin

<u>𝗥𝗲𝗾𝘂𝗲𝘀𝘁𝘀 𝗙𝗼𝗿𝗺𝗮𝘁𝘀</u>

• 𝖲𝗈𝗅𝗈 2017
• 𝖣𝗁𝗈𝗈𝗆 3 𝖧𝗂𝗇𝖽𝗂
• 𝖪𝗎𝗋𝗎𝗉 𝖪𝖺𝗇
• 𝖣𝖺𝗋𝗄 𝗌01
• 𝖲𝗁𝖾 𝖧𝗎𝗅𝗄 720𝗉
• 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝗌03 1080𝗉

‼️𝗗𝗼𝗻𝘁 𝗮𝗱𝗱 𝘄𝗼𝗿𝗱𝘀 & 𝘀𝘆𝗺𝗯𝗼𝗹𝘀 𝗹𝗶𝗸𝗲 , . -  send link movie series 𝗲𝘁𝗰‼️"""

    NORSLTS = """
lol"""

    RESTART_TXT = """
<b>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 !</b>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏2.7.3 [ 𝖲𝗍𝖺𝖻𝗅𝖾 ]</code></b>"""

    RESTART_GC_TXT = """
<b><u>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 ✅</u></b>"""

    LOGO = """
PIRO BOTS"""
