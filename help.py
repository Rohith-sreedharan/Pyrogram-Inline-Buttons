from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from plugins.core.buttons import help_text, help_markup

@Client.on_message(filters=filters.command("help"))
async def help_message(client:Client, message:Message)->None:
    try:
        await client.get_chat_member("bots_universe", message.from_user.id)
    except:
        await message.reply_text(
            "Join our [channel](t.me/bots_universe) to get my service. We are doing this completely for free!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("@Bots_Universe", url="t.me/bots_universe")]])
        )
        return

    await message.reply_text(
        help_text,
        reply_markup=help_markup
    )
    return
