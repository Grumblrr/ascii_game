'''
ASCII Game Engine
by Sam Rooney

Goal:
Make an ASCII game engine. Simple as that.

Features:
Configuration files, you can change how your game plays!
'''

import random, sys, os


def getConfig(configfile='config.txt', debug=False):
    name = os.path.basename(__file__)
    try:
        config = open(__file__[:0-len(name)]+configfile, 'r')
    except:
        defaults = open(__file__[:0-len(name)]+"defaultconfig.txt", 'r')
        config = open(__file__[:0-len(name)]+configfile, 'w')
        config.write(defaults.read())
        defaults.close()
        del defaults
        config.close
        del config
        config = open(__file__[:0-len(name)]+configfile, 'r')

    configdict = {}

    for ln in config:
        ln = ln.strip()
        if ln == '' or ln[0] == '#':

            if debug:
                print('skipping line: ' + ln)

            continue
        else:
            data = ln.split(': ')

            if debug:
                print('Not skipping. Data: ' + str(data))

            configdict[data[0]] = data[1]

    if debug:
        print('\n')
        for key in configdict.keys():
            print(key + ': ' + configdict[key])
        print('\n')

    return configdict

#




class Game():
    def __init__(self, config='config.txt'):
        self.config = getConfig(config, debug=False)
        self.map = Map(self.config) #make the map based on the config file
        self.player = Player(self.config) #make player based on config

#



class Player():
    def __init__(self, config):
        self.location = [0, 0]
        self.viewdist = int(config['viewdist'])
        self.sonardist = int(config['sonardist'])

    def move(self, xdiff, ydiff):
        self.location[0] += xdiff
        self.location[1] += ydiff

#



class Map():
    def __init__(self, config):
        self.corner = config['corner']
        self.side = config['side']
        self.topside = config['topside']

        if config['infinite'] = 'False':
            self.dimensions = [int(config['mapx']), int(config['mapy'])]
            self.infinite = False
            self.map = [] #map is list

        else:
            self.infinite = True
            self.dimensions = None
            self.buildingfile = config['buildingfile'] #where buildings are stored
            self.map = {} #map is dict

        self.outside = config['walls'] #walls for outside the map
        self.rocks = config['rocks'] #rocks you find laying around

#


#scripting, aka unit tests
if __name__ == '__main__':
    gm = Game()
