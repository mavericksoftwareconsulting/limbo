"""!out"""

import re
from dbController import clockOut

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!out( .*)?", text)
    if not match:
        return

    name = match[0].strip()
    clockIn(msg["user"])
    return "Goodbye", name


on_bot_message = on_message