class Item(object):
    def __init__(self, name = "", desc = "", takeDesc = "", isHidden = False, isTakeable = True):
        self.name = name
        self.desc = desc
        self.takeDesc = takeDesc
        self.isHidden = isHidden
        self.isTakeable = isTakeable
