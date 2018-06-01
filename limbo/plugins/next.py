import re
import subprocess
from time import sleep


def on_message(msg, server):
	subprocess.check_output("mpc next")
	return "Skipped to next song" + subprocess.check_output("mpc current")


on_bot_message = on_message