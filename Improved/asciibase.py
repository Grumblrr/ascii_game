'''
ASCII Game Engine
by Sam Rooney

Goal:
Make an ASCII game engine. Simple as that.
'''

import random

class Map():
    def __init__(self):
        try:
            config = open('config.txt', 'r')
        except:
            config = open('defaultconfig.txt', 'r')
        configdict = {}
        for ln in range(len(config)):
            if not ln or ln[0] == '#':
                continue
            else:
                data = ln.split(': ')
                configdict[data[0]] = data[1]
        print(configdict)

gm_map = Map()
