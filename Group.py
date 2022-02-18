
class Group:

    def __init__(self, char_list):
        self.char_list = char_list


class Fleet(Group):
    pass


class Herd(Group):
    pass



RoboFleet = Fleet([Voltron, Megazord, Optimus])
DinoHerd = Herd([Tyran, Veloce, Megalo])



