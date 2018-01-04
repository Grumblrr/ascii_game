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
# get the config file, and all related data contained within




class Game():
    def __init__(self, config='config.txt'):
        self.config = getConfig(config, debug=False)
        self.map = Map(self.config) #make the map based on the config file
        self.player = Player(self.config) #make player based on config
    #

    def setup(self):
        self.map.genMap()
    #

    def movePlayer(self, xdiff, ydiff):
        #checks that path is clear, then moves player
        pass
    #

    def printEntireMap(self):
        for ls in self.map.map:
            string = ''
            for char in ls:
                string += char + ' '
            print(string)
    #

    def getCharBelowPlayer(self):
        try:
            return self.map.map[self.player.location[1]][self.player.location[0]]
        except:
            return ''
    #
#
#



class Player():
    def __init__(self, config):
        self.location = [0, 0]
        self.viewdist = int(config['viewdist'])
        self.sonardist = int(config['sonardist'])
        self.inventory = {'sonar': 0,
                          'food': 0}
        self.stats = {'attackpower': 1,
                      'health': 10}
    #

    def move(self, xdiff, ydiff):
        self.location[0] += xdiff
        self.location[1] += ydiff

#
#



class Map():
    def __init__(self, config):
        self.corner = config['corner']
        self.side = config['side']
        self.topside = config['topside']

        if config['infinite'] == 'False':
            self.dimensions = [int(config['mapx']), int(config['mapy'])]
            self.infinite = False
            self.map = [] #map is list

        else:
            self.infinite = True
            self.dimensions = None
            self.buildingfile = config['buildingfile'] #where buildings are stored
            self.map = {} #map is dict

        self.outside = config['walls'] #walls for outside the map
        self.charset = config['charset'] #rocks you find laying around
        for i in range(len(self.charset)*3):
            self.charset += ' '
    #get pretty map characters, map data, and the charset.

    def genMap(self):
        if not self.infinite:
            for i in range(self.dimensions[1]):
                self.map.append([random.choice(self.charset) for i in range(self.dimensions[0])])
                #long line
            self.map[random.randint(0, self.dimensions[1]-1)][random.randint(0, self.dimensions[0]-1)] = '@'
            #make the door. Even longer line!
    #generate the map, currently only works for non-infinite-world

    def findDoor(self):
        for row in self.map:
            try:
                return [row.index('@'), self.map.index(row)]
            except:
                continue
        return None
    #find the door on the map, used in debug. Returns None if there is no door.

    def getMapRange(self, xmin, ymin, xmax, ymax):
        output = []
        for ls_int in range(ymin, ymax, 1):
            outstr=''
            for char_int in range(xmin, xmax, 1):
                outstr += self.map[ls_int][char_int] + ' '
            output.append(outstr)
        return output
    #get range of values in map, e.g. if you want a specific area
#
#


#scripting, aka unit tests
if __name__ == '__main__':
    gm = Game()
    gm.setup()
