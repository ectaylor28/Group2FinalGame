from game import *

commands_for_go = ["go", "run", "move", "travel", "proceed", "pass"]
commands_for_take = ["take", "get", "add", "steal", "grip", "catch", "grab", "bring", "carry", "bear"]
commands_for_drop = ["drop", "leave", "throw", "remove"]
commands_for_inventory = ["inventory", "inv"]
commands_for_exit = ["exit", "quit", "q", "bye"]
commands_for_task = ["task"]
commands_for_look = ["look"]
commands_for_look_at = ["lookat", "examine"]
commands_for_moves = ["moves"]

commands = [
	commands_for_go,
	commands_for_take,
	commands_for_drop,
	commands_for_inventory,
	commands_for_exit,
	commands_for_look,
	commands_for_look_at,
	commands_for_task,
	commands_for_moves
]

function_dict = {
	"go": execute_go,
	"take": execute_take,
	"drop": execute_drop,
	"inventory": print_inventory_items,
	"exit": exit_game,
	"task": execute_task,
	"look": execute_look,
	"lookat": execute_look_at,
	"moves": execute_moves
}