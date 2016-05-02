import Misc

class Player(object):
    def __init__(self, room, inv = []):
        self.loc = room
        self.inv = inv

    def printInv(self):
        print("\n==========Inventory==========")
        for item in self.inv:
            print("| " + item.names[0] + " "*(26 - len(item.names[0])) + "|")
        print("=============================")

    def goto(self, room):
        self.loc = room

    def addToInv(self, itemName):
        item = Misc.find(itemName, self.loc.items)
        self.inv.append(item)
        self.loc.items.remove(item)
        if item.takeDesc != "":
            print(item.takeDesc)
