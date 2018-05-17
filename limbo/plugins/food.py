"""!food - decides a random place to go for food"""

import random
import re
from datetime import datetime

# (<Name>, (<Hour>, <Minute>))
foodList = ("Subway", (7, 00)), ("Jimmy Johns", (10, 30)), ("Mr. Burrito", (11, 00)), ("Panda Express", (10, 00)), ("Potbelly", (9, 00)), ("Blaze", (10, 30)), ("Smokin' Oaks", (11, 00)), ("Fuzzy's", (10, 00)), ("Pizza Pit", (11, 00)), ("Dominos", (10, 30)), ("Jeff's", (10, 30)), ("Fighting Burrito", (11, 00)), ("Thai Kitchen", (11, 00))
def decide_food():
	random.seed(datetime.now().microsecond)
	isOpen = False
	while(not isOpen):
		choice = random.choice(foodList)

		if choice[1][0] < datetime.now().hour:
			continue
		elif choice[1][0] > datetime.now().hour:		
			isOpen = True 
			break
		elif choice[1][1] > datetime.now().minute:
			isOpen = True
			break

	return "You should eat at " + choice[0]

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!food( .*)?", text)
    if not match:
        return

    return decide_food()


on_bot_message = on_message