from items import *
from map import rooms

inventory = [item_knife, item_whiskey]
movement_limit = 10

# Game goals
goalr = rooms.copy()
del goalr["Entrance"]
goal_room = goalr.popitem()
goali = items.copy()
goal_item = goali.popitem()

# Start game at the entrance hall
current_room = rooms["Entrance"]
