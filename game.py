'''
Text-Based roguelike Game
Sam Rooney
'''

#Time to make some list of lists

#imports
import random


#functions



#classes


class Unit():
    def __init__(self, char, location, attackpower=1, health=1, leap=1, turncount=1):
        self.char = char
        self.location=location
        self.ap = attackpower #damage done per blow
        self.hp = health #total health
        self.leap= leap #amount of tiles this can move per turn
        self.turncount = turncount #constant to reset self.counter to
        self.counter = self.turncount #counter till next time this unit takes a turn

    def __str__(self):
        return self.char

class Game():
    def __init__(self, rc=18, fc=3, sc=2, ac=1, spacemult = 4): #likelihood for certain chars stored in self.mpc
        self.mpc = [' ' for i in range((rc+fc+sc+ac)* 4)]
        for i in range(rc+fc+sc+ac):
            if i+1 <= rc:
                self.mpc[i] = '0'
            elif i+1 <= rc+fc:
                self.mpc[i] = 'F'
            elif i+1 <= rc+fc+sc:
                self.mpc[i] = 'Q'
            else:
                self.mpc[i] = 'A'
        self.mapls = []
    #does some interesting things with lists, makes empty map list

    def genMap(self, xsize=20, ysize=20):
        self.mapls = [[random.choice(self.mpc) for i in range(ysize)] for i in range(xsize)] #generate map grid
        self.dloc = [random.randint(0, xsize) for i in range(2)] #door location
        self.mapls[self.dloc[0]][self.dloc[1]] = '@' #put the door on the map
        self.units = [] #unit list
        self.floor = 1 #floor count,1 is first, 2 is second, etc
        self.pl = [random.randint(0, xsize),random.randint(0, ysize)] #player location
    #generates entire map, player location, etc

    def printMap(self):
        for i in range(len(self.mapls)):
            if i != self.pl[1]:
                print(self.mapls[i])
                continue
            else:
                printls = []
                for j in range(len(self.mapls[i])):
                    #print(j,':', self.pl[1])
                    if j != self.pl[0]:
                        printls.append(self.mapls[i][j])
                    else:
                        printls.append('&')
                print(printls)
    #print entire map

    def getPlayerView(self, radius):
        #self.pl is player location as an [x, y] list
        viewls = []
        counter = 0
        #print(rnge)

        for i in range(radius*2+1):
            #print(viewls)
            viewls.append([])
            obj = ''
            for j in range(radius*2+1):
                try:
                    #print([i+(self.pl[1]//2)][j+(self.pl[0]//2)])

                    obj=self.mapls  [i+(self.pl[1])-radius]   [j+(self.pl[0])-radius]

                    #(str([i+(self.pl[1])][j+(self.pl[0])]))
                    #print(self.mapls[i+(self.pl[1])][j+(self.pl[0])])
                    #print(obj + ' obj')
                except IndexError:

                    obj='#'
                    #print(obj + ' obj')
                if i+self.pl[1]-radius == self.pl[1] and j+self.pl[0]-radius == self.pl[0]:
                    obj = '&'
                viewls[counter].append(obj)

            counter+=1
            #print(counter)
        return viewls
    #Get list of pieces the player can view, replacing the outside values with #

    def printPlayerView(self, radius=2):
        for i in range(10):
            print('\n')
        view = self.getPlayerView(radius)
        ln = '+'
        for i in range(len(view[0])):
            ln += '--'
        ln += '-+'
        print(ln)
        ln = ''
        for ls in view:
            ln = '| '
            for char in ls:
                ln += char + ' '
            ln += '|'
            print(ln)
        ln='+'
        for i in range(len(view[0])):
            ln += '--'
        ln += '-+'
        print(ln)
    #print the player view in a pretty way, with some newlines before it
    '''
    def gameStep(self):
        for unit in self.units:
            pass #make the units move
    '''
    def movePlayer(self, direction):

        try:
            assert('w' in direction or 'a' in direction or 's' in direction or 'd' in direction)
        except:
            print('Please type a keyboard direction. [w, a, s, d, wa, wd, sa, sd, etc]]')
        else:
            move = [0, 0]

            if 'a' in direction:
                move[0] -= 1
            if 'w' in direction:
                move[1] += 1
            if 's' in direction:
                move[1] -= 1
            if 'd' in direction:
                move[0] += 1

            self.pl[0] += move[0]
            self.pl[1] += move[1]
    #move the player, theres also some error detection that we probably dont need



#unit tests. theyre a blast

gm = Game()
gm.genMap(1000, 1000)

gm.printPlayerView(10)
gm.pl[0] += 10
gm.pl[1] += 10
gm.printPlayerView(10)
