# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
#😂😂😂😂

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import poci_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice


@poci_cmd(pattern="bokep$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Bokeppypy", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Bokep jangan sange kontol**.")
        
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")

        

CMD_HELP.update(
    {
        "bokep": f"**Plugin : **`bokep`\
        \n\n  •  **Syntax :** `{cmd}bokep`\
        \n  •  **Function : **Untuk Mengirim video bokep untuk kamu yang sange.\
    "
    }
)

