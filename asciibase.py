'''
ASCII game engine
By Sam Rooney

Goal:
Make a game engine that can use ASCII to make a multi-level map, generate items
for the map, and otherwise generate an ASCII-based roguelike landscape. Should
also contain a basic player/npc framework as well as an item class.
'''

#imports
import random, pygame, sys

#variables

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
    #pretty self-explanatory

    def move(self, direction):
        #direction is string, must be 'n', 's', 'e', 'w', 'nw', 'ne' etc
        #im kinda proud of this sneaky buggering around of mine
        #if the direction is invalid, nothing happens
        if direction in ['n', 'ne', 'nw']:
            self.location[1] += 1
        if direction in ['s', 'se', 'sw']:
            self.location[1] -= 1
        if direction in ['e', 'ne', 'se']:
            self.location[0] -= 1
        if direction in ['w', 'nw', 'sw']:
            self.location[0] += 1
    #direction is string, e.g. 'n', 's', 'ne', etc
    #if direction is invalid nothing happens


class Item():
    #basic item class, esp. for basic items. Contains 'id' variable, should be
    #a unique index from 'ids' list.
    def __init__(self, name, idsindex=None):
        self.id = idsindex
        self.name = name #special name if there is any


class Game():
    def __init__():
        #width and height are attributes
        screensize = self.width, self.height = 1080, 720
        self.screen = pygame.display.set_mode(screensize)
        
