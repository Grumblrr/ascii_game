'''
ASCII game engine
By Sam Rooney

Goal:
Make a game engine that can use ASCII to make a multi-level map, generate items
for the map, and otherwise generate an ASCII-based roguelike landscape. Should
also contain a basic player/npc framework.
'''

#imports
import random

#classes
class Player():
    def __init__(self, ap=1, hp=10, carryweight=10, startlocation=[0, 0]):
        self.ap = ap
        self.hp = hp
        self.carryweight = carryweight
        self.inventory = []
        self.clothing = []
        self.holding = []
        self.location = startlocation 

    def move(self, direction):
        #direction is string, must be 'n', 's', 'e', 'w', 'nw', 'ne' etc
        if direction == 'n':
            direction[1] += 1
        elif direction == 's':
            direction[1] -= 1
        elif direction == 'e':
            direction[0] -= 1
        elif direction == 'w':
            direction[0] += 1
        else:
            raise ValueError('Invalid direction')
