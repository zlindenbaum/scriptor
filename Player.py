class Player(object):
    def __init__(self, room, inv = []):
        self.loc = room
        self.inv = inv

    def goto(self, room):
        self.loc = room

    def addToInv(self, item):
        self.inv.append(item)
        if item.takeDesc != "":
            print item.takeDesc
