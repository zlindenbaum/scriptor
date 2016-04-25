class Room(object):
    def __init__(self, name = "default room", desc = "a normal looking room", items = {}, commands = {}):
        self.name = name
        self.desc = desc
        self.items = items

        self.commands = commands

    def contains(self, itemKey):
        if itemKey in self.items.keys():
            return True
        else:
            return False

    def printDetails(self):
        print('\nRoom: ' + self.name)
        print('Description: ' + self.desc + '\n')
