class Item(object):
    def __init__(self, ID = "", names = [], desc = "", takeDesc = "", isHidden = False, isTakeable = True):
        self.names = names
        self.desc = desc
        self.takeDesc = takeDesc
        self.isHidden = isHidden
        self.isTakeable = isTakeable
