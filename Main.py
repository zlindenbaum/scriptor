from Game import *
from Player import *
from Room import *
from Item import *

global_commands = {
    "inv": "self.player.printInv()",
    "look": "print(self.player.loc.desc)",
    "print": "print(\"!x!\")",

    "take": """
if self.player.loc.contains("!x!"):
    self.player.addToInv("!x!")
#    del self.player.loc.items["!x!"]
    """,

    "examine": """
if self.player.loc.contains("!x!"):
    print(Misc.find("!x!", self.player.loc.items).desc)
elif "!x!" in Misc.flatten([item.names for item in self.player.inv]):
    print(Misc.find("!x!", self.player.inv).desc)
    print("You are currently holding it")
    """,

    "commands": """
for command, action in self.player.loc.commands.items():
    print(command)
    """,

    "drop": """
if "!x!" in Misc.flatten([item.names for item in self.player.inv]):
    item = Misc.find("!x!", self.player.inv)
    self.player.inv.remove(item)
    self.player.loc.items.append(item)
    """
}

rooms = {
    "r1":
    Room(
        name = "first room",
        desc = "this is the first room",
        # commands = {"next": "self.player.goto(self.rooms[\"r2\"])"},
        connections = {"next": "r2"},
        items = [
            Item(
                names = ["a bar", "bar", "the bar"],
                desc = "a plain white bar; it doesn't strike you as especially extraordinary",
                takeDesc = "you slide the bar into your pocket"
            )
        ]
    ),

    "r2":
    Room(
        name = "second room",
        desc = "this is the second room",
        # commands = {"back": "self.player.goto(self.rooms[\"r1\"])"}
        connections = {"back": "r1"}
    )
}

player = Player(rooms['r1'])

game = Game(rooms, player, global_commands = global_commands)

game.player.inv.append(Item(names = ["thing 1"]))
game.player.inv.append(Item(names = ["thing 2"]))
game.player.inv.append(Item(names = ["thing 3"]))
game.player.inv.append(Item(names = ["thing 4"]))
game.player.inv.append(Item(names = ["a void in your existance"]))

game.gameLoop()
