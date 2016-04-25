class Game(object):
    def __init__(self, rooms, player, global_commands = {}):

        self.rooms = rooms
        self.global_commands = global_commands
        self.player = player

    def gameLoop(self):
        self.lastCommand = ""
        while True:
            self.player.loc.printDetails()

            self.lastCommand = input()

            if self.lastCommand == "!exit!":
                print("Game Ended")
                break

            if self.lastCommand in self.player.loc.commands.keys():
                eval(self.player.loc.commands[self.lastCommand])
            elif self.lastCommand in self.global_commands.keys():
                eval(self.global_commands[self.lastCommand])
            elif self.lastCommand.split(' ', 1)[0] in self.global_commands.keys():
                exec(self.global_commands[self.lastCommand.split(' ', 1)[0]].replace("!x!", self.lastCommand.split(' ', 1)[1]))

            else:
                print("Sorry, I don't understand what you mean")
