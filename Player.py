class Player(object):
    def __init__(self, room, inv = []):
        self.loc = room
        self.inv = inv

    def printInv(self):
        print("\n==========Inventory==========")
        for item in self.inv:
            print("| " + item.name + " "*(26 - len(item.name)) + "|")
        print("=============================")

    def goto(self, room):
        self.loc = room

    def addToInv(self, item):
        self.inv.append(item)
        if item.takeDesc != "":
            print(item.takeDesc)
