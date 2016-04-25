class Room(object):
    def __init__(self, name = "default room", desc = "a normal looking room", commands = {}):
        self.name = name
        self.desc = desc

        self.commands = commands

    def printDetails(self):
        print('\nRoom: ' + self.name)
        print('Description: ' + self.desc + '\n')    
