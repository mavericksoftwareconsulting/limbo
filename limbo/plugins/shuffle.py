"""!shuffle - this command is currently not allowed."""
import re
from subprocess import check_output

# To use, remove the top return statement and uncomment the two lines below.
def on_message(msg, server):
	text = msg.get("text", "")
	match = re.findall(r"!shuffle( .*)?", text)

    if not match:
    	return "Error."

	return "This command is currently not allowed."
	# check_output(["mpc", "shuffle"])
	# return "Playing AMS-Default, shuffled."


on_bot_message = on_message