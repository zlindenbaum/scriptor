class Player(object):
    def __init__(self, room, inv = []):
        self.loc = room
        self.inv = inv

    def goto(self, room):
        self.loc = room
