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
# get the config file, and all related data contained within



class Game():
    def __init__(self, config='config.txt'):
        self.config = getConfig(config, debug=False)
        try:
            self.map = Map(self.config) #make the map based on the config file
            self.player = Player(self.config) #make player based on config
        except:
            raise ValueError('Incompatible config file.')
        #
    #make map and player objects, grab config

    def setup(self):
        self.map.genMap()
        self.player.location = [random.randint(0, self.map.dimensions[0]-1), random.randint(0, self.map.dimensions[1]-1)]
        while self.map.map[self.player.location[1]][self.player.location[0]] != ' ':
            self.player.location = [random.randint(0, self.map.dimensions[0]-1), random.randint(0, self.map.dimensions[1]-1)]
    #generate map, player location, etc.

    def movePlayer(self, xdiff, ydiff):
        #checks that path is clear, then moves player
        pl = self.player.location
        pl[0] += xdiff
        pl[1] += ydiff
        try:
            char = self.map.map[pl[1]][pl[0]]
        except:
            if not self.map.infinite:
                char = '#'
            else:
                raise Exception('Infinite map generation not yet complete')
        if char not in '0#':
            self.player.move(xdiff, ydiff)
        char = self.getCharBelowPlayer()
        if char == 'Q':
            self.player.inventory['sonar']+=self.player.sonarper
        elif char == 'F':
            self.player.inventory['food']+=1
        elif char =='A':
            self.player.stats['attackpower']+=1
        elif char =='$':
            self.player.inventory['coins']+=1
    #check that player path is clear, then moves the player accordingly

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
        self.sonarper = int(config['amountSonarPer'])
        self.inventory = {'sonar': 0,
                          'food': 0,
                          'coins': int(config['startingcoins'])}
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
        try:
            for ls_int in range(ymin, ymax, 1):
                outstr=' '
                try:
                    for char_int in range(xmin, xmax, 1):
                        outstr += self.map[ls_int][char_int] + ' '
                except:
                    outstr += '#'
                    continue
                output.append(outstr)
        except:
            outstr += '#'
        return output
    #get range of values in map, e.g. if you want a specific area

    def prettyMapRange(self, xmin, ymin, xmax, ymax):
        maprange = self.getMapRange(xmin, ymin, xmax, ymax)
        output = []
        outstr = self.corner
        for i in range(len(maprange[0])):
            outstr += self.topside
        output.append(outstr + self.corner)

        for ls in maprange:
            outstr = self.side
            for char in ls:
                outstr += char
            output.append(outstr + self.side)

        outstr = self.corner
        for i in range(len(maprange[0])):
            outstr += self.topside
        output.append(outstr + self.corner)

        return output
#
#


#scripting, aka unit tests
if __name__ == '__main__':
    gm = Game()
    gm.setup()
    for ls in gm.map.getMapRange(5, 5, 21, 21):
        print(ls)
