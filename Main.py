from Game import *
from Player import *
from Room import *
from Item import *

global_commands = {
    "inv": "self.player.printInv()",
    "look": "print(self.player.loc.desc)"
}

rooms = {
    "r1":
    Room(
        name = "first room",
        desc = "this is the first room",
        commands = {"next": "self.player.goto(self.rooms[\"r2\"])"}
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
