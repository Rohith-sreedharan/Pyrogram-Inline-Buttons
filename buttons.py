import pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup      

def cb(l:list = ["text", "data", "url", "login_url", "switch_inline_query, switch_inline_query_current_chat"]):
    text = l[0] if len(l) >= 1 else "No Text"
    data = l[1] if len(l) >= 2 else "nope"
    url = l[2] if len(l) >= 3 else None
    login_url = l[3] if len(l) >= 4 else None
    switch_inline_query = l[4] if len(l) >= 5 else None
    switch_inline_query_current_chat = l[5] if len(l) >= 6 else None

    return InlineKeyboardButton(text, data, url, login_url, switch_inline_query, switch_inline_query_current_chat)

def create_markup(_list: list=[[]]):
    result = []
    for row in _list:
        result.append([])
        for item in row:
            btn = cb(item)
            result[-1].append(btn)
    
    return InlineKeyboardMarkup(result)


r_home_btn = ["🏠 Home", "home"]
r_help_btn = ["🙂 Help", "help"]
r_ourc_btn = ["💝 Our Channel", None, "https://telegram.me/bots_universe"]
r_rohith = ["@Rohithaditya", None, "t.me/Rohithaditya"]

main_markup = create_markup([
    [r_help_btn],
    [r_ourc_btn],
    [r_home_btn]
])

help_text = """\
Edit tesxt
```
"""
help_markup = create_markup([
    [r_home_btn]
])
