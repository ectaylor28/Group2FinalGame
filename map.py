from items import *

room_entrance = {
    "name": "Entrance Hall",

    "description":
    """You stand in an old hallway. A draught blows at your ankles from underneath the front door. The windows have no glass in them and the unwelcoming nature of the room hardly encourages you to explore the house any further.""",

    "exits": {"up": "Landing", "down": "Cellar", "north": "Kitchen", "west": "Sitting", "east": "Dining"},

    "items": [item_musicbox]
}

room_cellar = {
    "name": "Cellar",

    "description":
    """You finally make it down the creaky stairs to the cellar. Some  old-wooden barrels which were used by the family for making homemade wine. After all these years they are still full... of rats and bones.
""",

    "exits":  {"up": "Entrance", "west": "Closet"},

    "items": [item_musket]
}

room_closet = {
    "name": "Storage Closet",

    "description":
    """As you walk in you feel something quickly brush past you. You turn around and see it was a rat. In this room, there aren’t many items, it's filled cobwebs and what look like small insect hives. But you see blood stains on a shelf next to an empty scythe case.
""",

    "exits": {"east": "Cellar"},

    "items": []
}

room_sitting = {
    "name": "Sitting Room",

    "description":
    """The room is almost empty apart from a small wooden chair, slowly rocking back and forth in the corner, in rhythm to the whistling breeze.""",

    "exits": {"east": "Entrance"},

    "items": [item_photo]
}

room_dining = {
    "name": "Dining Room",

    "description":
    """The remnants of a final meal eaten here are still strewn over the old, mahogany table. Crushed glasses and puddles of spilt red wine make the floor a treacherous place. Watch your step.""",

    "exits": {"west": "Entrance"},

    "items": [item_diary]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You look around the dark kitchen. Everything is in disorder, the oven is completely burned out. Ash covers the floor and makes it difficult for you to breathe. But somehow a pot is bubbling on the side, steam curling out of it into the air...
""",

    "exits": {"south": "Entrance", "north": "Vegetable"},

    "items": []
}

room_vegetable = {
    "name": "Vegetable Garden",

    "description":
    """There are many different plants here, all of them dying. But one particular plant stands out, it's thorny and has a skull on the pot.""",

    "exits": {"south": "Kitchen", "north": "Shed"},

    "items": [item_plant]
}

room_shed = {
    "name": "Shed",

    "description":
    """There is no floor here, the ground is just dirt. In the corner you can see a rusty shovel.""",

    "exits": {"south": "Vegetable"},

    "items": [item_coffin]
}

room_landing = {
    "name": "Landing",

    "description":
    "As you step on to the landing you hear the floor creak and feel the floorboards lower as you put your weight on them, it doesn't seem very stable. There is a hole in the floor ahead of you. You look down into it and can vaguely see a foot lying at one end at the bottom of the hole.",

    "exits": {"up": "Attic", "north": "Master", "east": "Spare", "west": "Bathroom", "down": "Entrance"},

    "items": [item_note]
}

room_attic = {
    "name": "Attic",

    "description":
    """You finally make it up the stairs to the attic. Many old goods are in here; most of the books and old clothes are piled in one corner.""",

    "exits": {"down": "Landing"},

    "items": [item_hand]
}

room_master = {
    "name": "Master Bedroom",

    "description":
    """Cobwebs hang in every corner and drape themselves across the bed like a blanket.""",

    "exits": {"south": "Landing"},

    "items": [item_dress]
}

room_spare = {
    "name": "Spare",

    "description":
    """This large, sound proof room was multi-purpose, many things could have been done in here, but it looks like everything that was in here has been removed.""",

    "exits": {"west": "Landing"},

    "items": [item_doll]
}

room_bath = {
    "name": "Bathroom",

    "description":
    """A bloody, cracked mirror is the first thing you see as you enter. The curtains are covered in blood and cut in half while the bath tub is broken. A serious fight must have occurred in here!""",

    "exits": {"east": "Landing"},

    "items": [item_mirror]
}



rooms = {
    "Entrance": room_entrance,
    "Cellar": room_cellar,
    "Closet": room_closet,
    "Sitting": room_sitting,
    "Dining": room_dining,
    "Kitchen": room_kitchen,
    "Vegetable": room_vegetable,
    "Shed": room_shed,
    "Landing": room_landing,
    "Attic": room_attic,
    "Master": room_master,
    "Spare": room_spare,
    "Bathroom": room_bath
}