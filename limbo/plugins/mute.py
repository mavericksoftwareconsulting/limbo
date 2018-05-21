import re
import subprocess
from time import sleep


def on_message(msg, server):
	subprocess.check_output("mpc volume 50")
	sleep(1800) # Time in seconds
	subprocess.check_output("mpc volume 100")
	return "Music returned to normal"


on_bot_message = on_message