
from Robot import Robot
from Dino import Dinosaur


class Group:

    def __init__(self, char_list):
        self.char_list = char_list


class Fleet(Group):
    pass


class Herd(Group):
    pass


Voltron = Robot('Bob', '100', 'Sledgehammer', '50')
Megazord = Robot('Rob', '90', 'Fork', '45')
Optimus = Robot('Tob', '80', 'Cheese Grater', '55')

Tyran = Dinosaur('Tyran', '500', '300')
Veloce = Dinosaur('Veloce', '450', '300')
Megalo = Dinosaur('Megalo', '680', '260')

RoboFleet = Fleet([Voltron, Megazord, Optimus])
DinoHerd = Herd([Tyran, Veloce, Megalo])



