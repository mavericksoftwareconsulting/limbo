"""!playing - get the song that is currently playing"""

import re
from subprocess import check_output

def on_message(msg, server):
	text = msg.get("text", "")
    match = re.findall(r"!playing( .*)?", text)

    if not match:
        return "Error."
	
	temp = check_output(["mpc", "current"])
	return str(temp).rstrip()

on_bot_message = on_message