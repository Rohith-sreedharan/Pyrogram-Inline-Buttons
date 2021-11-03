import pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup      

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
