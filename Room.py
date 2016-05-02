import Misc

class Room(object):
    def __init__(self, name = "default room", desc = "a normal looking room", items = [], commands = {}, connections = {}):
        self.name = name
        self.desc = desc
        self.items = items
        self.connections = connections
        self.commands = commands

    def contains(self, itemName):
        if itemName in Misc.flatten([item.names for item in self.items]):
            return True
        else:
            return False

    def printDetails(self):
        print('\nRoom: ' + self.name)
        print('Description: ' + self.desc + '\n')
