from Game import *
from Player import *
from Room import *

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

game = Game(rooms, player)
game.gameLoop()
