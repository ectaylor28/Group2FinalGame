from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

# Game goals
goalr = rooms.copy()
del goalr["Reception"]
goal_room = goalr.popitem()
goali = items.copy()
goal_item = goali.popitem()

# Start game at the reception
current_room = rooms["Reception"]
