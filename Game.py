class Game(object):
    def __init__(self, rooms, player):

        self.rooms = rooms

        self.player = player

    def gameLoop(self):
        self.lastCommand = ""
        while True:
            print('\nRoom: ' + self.player.loc.name)
            print('Description: ' + self.player.loc.desc + '\n')

            self.lastCommand = input()

            if self.lastCommand == "!exit!":
                print("Game Ended")
                break

            if self.lastCommand in self.player.loc.commands.keys():
                eval(self.player.loc.commands[self.lastCommand])
            else:
                print("Sorry, I don't understand what you mean")
