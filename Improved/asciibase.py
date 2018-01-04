'''
ASCII Game Engine
by Sam Rooney

Goal:
Make an ASCII game engine. Simple as that.
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
        config.close
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



class Game():
    def __init__(self, config='config.txt'):
        self.config = getConfig(config, debug=False)


class Map():
    def __init__(self):
        pass




#gm_map = Map(True)
