"""!report [<name>]"""

import re
from dbController import runReport
from dbController import runUserReport

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!report( .*)?", text)
    if not match:
        return

    name = match[0].strip()
    if name:
        return runUserReport(name)
    else:
        return runReport()


on_bot_message = on_message