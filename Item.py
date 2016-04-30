class Item(object):
    def __init__(self, ID = "", name = "", desc = "", takeDesc = "", isHidden = False, isTakeable = True):
        self.ID = ID
        self.name = name
        self.desc = desc
        self.takeDesc = takeDesc
        self.isHidden = isHidden
        self.isTakeable = isTakeable
