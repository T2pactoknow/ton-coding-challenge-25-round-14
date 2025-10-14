from pyrogram import Client, filters

app = Client("userbot", api_id=123456, api_hash="abcd1234")

@app.on_message(filters.command("ping", prefixes="/") & filters.me)
async def ping(_, msg):
    await msg.reply_text("pong")

app.run()
