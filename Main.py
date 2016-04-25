from Game import *
from Player import *
from Room import *
from Item import *

rooms = {
    "r1":
    Room(
        name = "first room",
        desc = "this is the first room",
        commands = {"next": "self.player.goto(self.rooms[\"r2\"])",
                    "inv": "self.player.printInv()"}
    ),

    "r2":
    Room(
        name = "second room",
        desc = "this is the second room",
        commands = {"back": "self.player.goto(self.rooms[\"r1\"])"}
    )
}

player = Player(rooms['r1'])

game = Game(rooms, player)
game.player.addToInv(Item(name = "thing 1"))
game.player.addToInv(Item(name = "thing 2"))
game.player.addToInv(Item(name = "thing 3"))
game.player.addToInv(Item(name = "thing 4"))
game.player.addToInv(Item(name = "a void in your existance"))
game.gameLoop()
