from pyrogram import Client

api_id =  1597219
api_hash = "252f4132f58c15c9c5ccfccdba79c974"

app = Client("jggd_g-host", api_id=api_id, api_hash=api_hash)

@app.on_message()
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

app.run()
