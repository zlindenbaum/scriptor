import Misc
import pyparsing as pp
import types

class Room(object):
    def __init__(self, ID, name = "default room", desc = "a normal looking room", items = [], commands = {}, connections = {}):
        self.ID = ID
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

        condition = pp.Suppress(pp.Literal("<")) + (pp.Literal("with") ^ pp.Literal("without")) + pp.Word(pp.alphanums) + pp.Suppress(pp.Literal(">"))
        conditionalText = pp.SkipTo(pp.Literal("|"))
        conditionBlock = pp.Group(pp.Suppress(pp.Literal("|")) + condition + conditionalText + pp.Suppress(pp.Literal("|")))
        # descBlock = pp.Optional(pp.OneOrMore(pp.SkipTo("|") + conditionBlock)) + pp.SkipTo(pp.stringEnd)
        # descBlock = pp.ZeroOrMore(conditionBlock | pp.SkipTo(pp.Literal("|")) | pp.SkipTo(pp.stringEnd))
        descBlock = pp.ZeroOrMore(conditionBlock | pp.Word(pp.printables))

        pDesc = descBlock.parseString(self.desc)
        print("Description:", end=" ")

        for item in pDesc:
            if type(item) is str:
                print(item, end=" ")
            else:
                if item[0] == "with":
                    if not item[1] in [item.ID for item in self.items]:
                        print(item[2], end = " ")
                if item[0] == "without":
                    if item[1] in [item.ID for item in self.items]:
                        print(item[2], end = " ")
                # print(item[2], end = " ")
        print()

        # print(pDesc)

        # print('Description: ' + self.desc + '\n')
