"""!shuffle - this command is currently not allowed."""

import re
from subprocess import check_output
from time import sleep

# To use, remove the top return statement and uncomment the two lines below.
def on_message(msg, server):
	text = msg.get("text", "")
    match = re.findall(r"!next( .*)?", text)

    if not match:
        return "Error."

	return "This command is currently not allowed."
	# check_output(["mpc", "next"])
	# return "Skipped to next song: " + str(check_output(["mpc", "current"])).rstrip()


on_bot_message = on_message