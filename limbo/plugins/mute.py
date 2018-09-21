"""!mute - set the music volume to 50% for 15 minutes"""

import re
from subprocess import check_output
from time import sleep


def on_message(msg, server):
	text = msg.get("text", "")
    match = re.findall(r"!mute( .*)?", text)

    if not match:
        return "Error."

	check_output(["mpc", "volume", "50"])
	sleep(900) # Time in seconds
	check_output(["mpc", "volume", "100"])
	return "Music returned to normal."


on_bot_message = on_message