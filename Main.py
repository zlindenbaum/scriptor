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
    self.player.addToInv(self.player.loc.items["!x!"])
    del self.player.loc.items["!x!"]
    """,

    "examine": """
if self.player.loc.contains("!x!"):
    print(self.player.loc.items["!x!"].desc)
elif "!x!" in [item.ID for item in self.player.inv]:
    print(self.player.inv[[item.ID for item in self.player.inv].index("!x!")].desc)
    """,

    "commands": """
for command, action in self.player.loc.commands.items():
    print(command)
    """
}

rooms = {
    "r1":
    Room(
        name = "first room",
        desc = "this is the first room",
        commands = {"next": "self.player.goto(self.rooms[\"r2\"])"},
        items = {
            "bar": Item(
                ID = "bar",
                name = "a bar",
                desc = "a plain white bar; it doesn't strike you as especially extraordinary",
                takeDesc = "you slide the bar into your pocket"
            )
        }
    ),

    "r2":
    Room(
        name = "second room",
        desc = "this is the second room",
        commands = {"back": "self.player.goto(self.rooms[\"r1\"])"}
    )
}

player = Player(rooms['r1'])

game = Game(rooms, player, global_commands = global_commands)

game.player.addToInv(Item(name = "thing 1"))
game.player.addToInv(Item(name = "thing 2"))
game.player.addToInv(Item(name = "thing 3"))
game.player.addToInv(Item(name = "thing 4"))
game.player.addToInv(Item(name = "a void in your existance"))

game.gameLoop()
