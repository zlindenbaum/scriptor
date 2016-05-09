import Misc
import Parser

class Room(object):
    def __init__(self, ID, name = "default room", desc = "a normal looking room",
                 items = [], commands = {}, connections = {}):
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


        pDesc = Parser.desc_block.parseString(self.desc)
        # print(pDesc)
        print("Description:", end=" ")

        for item in pDesc:
            if type(item) is str:
                print(item, end=" ")
            else:
                if item["if_condition"]["verb"] == "has":
                    if not item["if_condition"]["object"] in [item.ID for item in self.items]:
                        print(item["if_condition"]["condition_text"], end = " ")
                    else:
                        print(item["else_condition"]["condition_text"])
                # if item[0] == "without":
                #     if item[1] in [item.ID for item in self.items]:
                #         print(item[2], end = " ")
                # print(item[2], end = " ")
        print()

        # print(pDesc)

        # print('Description: ' + self.desc + '\n')
