import tkinter as tk
import random
def transPose (m):
    res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return res
class Shape:
    O = [[(1,'Blue'),(1,'Blue')],[(1,'Blue'),(1,'Blue')]]
    I = [[(1,'Yellow')],[(1,'Yellow')],[(1,'Yellow')],[(1,'Yellow')]]
    S = [[(0,'Black'),(1,'Red'),(1,'Red')],[(1,'Red'),(1,'Red'),(0,'Black')]]
    Z = [[(1,'Orange'),(1,'Orange'),(0,'Black')],[(0,'Black'),(1,'Orange'),(1,'Orange')]]
    L = [[(1,'Green'),(0,'Black')],[(1,'Green'),(0,'Black')],[(1,'Green'),(1,'Green')]]
    J = [[(0,'Black'),(1,'Pink')],[(0,'Black'),(1,'Pink')],[(1,'Pink'),(1,'Pink')]]
    T = [[(1,'Purple'),(1,'Purple'),(1,'Purple')],[(0,'Black'),(1,'Purple'),(0,'Black')]]
    def __init__(self, sha):
        if sha == 'O':
            self.shape = Shape.O
            self.color = 'Blue'
        elif sha == 'I':
            self.shape = Shape.I
            self.color = 'Yellow'
        elif sha == 'S':
            self.shape = Shape.S
            self.color = 'Red'
        elif sha == 'Z':
            self.shape = Shape.Z
            self.color = 'Orange'
        elif sha == 'L':
            self.shape = Shape.L
            self.color = 'Green'
        elif sha == 'J':
            self.shape = Shape.J
            self.color = 'Pink'
        elif sha == 'T':
            self.shape = Shape.T
            self.color = 'Purple'

    def show(self):
        return self.shape
    def transPose (self):
        self.shape = [[self.shape[j][i] for j in range(len(self.shape))] for i in range(len(self.shape[0]))]
class Tetris:
    shapes_order = [Shape('T')]
    Screen = [[0]*10]*20
    def __init__(self):
        self.generator()
    def generator(self):
        Tetris.shapes_order.append(Shape(random.choice(['O','I','S','Z','L','J','T'])))
        Tetris.shapes_order = Tetris.shapes_order[-2:]
    def draw(self):
        '''draw screen each frame'''

        pass
    def check(self):
        '''check complete row each frame'''
        
        pass




game = Tetris()
print(game.Screen)