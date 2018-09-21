"""!food - decides a random place to go for food"""

import random
import re
from datetime import datetime, time

is_open = lambda x: x[1] < datetime.now().time()

foodList = ("Subway", time(7, 00)), ("Jimmy Johns", time(10, 30)), ("Mr. Burrito", time(11, 00)), ("Panda Express", time(10, 00)), ("Potbelly", time(9, 00)), ("Blaze", time(10, 30)), ("Smokin' Oaks", time(11, 00)), ("Fuzzy's Tacos", time(11, 00)), ("Pizza Pit", time(11, 00)), ("Fighting Burrito", time(11, 00)), ("Thai Kitchen", time(11, 00)), ("Freddy's", time(10, 30))

# (<Name>, (<Hour>, <Minute>))
def decide_food():
	random.seed(datetime.now().microsecond)
	hour = datetime.now().hour
	minute = datetime.now().minute
	temp = list(filter(is_open, foodList))

	return "You should eat at {0}".format(random.choice(temp)[0])

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!food( .*)?", text)
    if not match:
        return

    return decide_food()

on_bot_message = on_message
