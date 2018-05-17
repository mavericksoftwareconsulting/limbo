"""!in"""

import re
from dbController import clockIn


def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!in( .*)?", text)
    if not match:
        return
    clockIn(msg["user"])
    return "Welcome", name


on_bot_message = on_message
