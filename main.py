import tkinter as tk
import random
from tkinter import messagebox
import pygame

class Shape:
    O = {0 : [[1,1],[1,1]]}
    I = {0 : [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]], 1 : [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]] , 2 : [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]] , 3:[[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]}
    S = {0 : [[0,1,1],[1,1,0],[0,0,0]] , 1 : [[0,1,0],[0,1,1],[0,0,1]] , 2 : [[0,0,0],[0,1,1],[1,1,0]] , 3 : [[1,0,0],[1,1,0],[0,1,0]] }
    Z = {0 : [[1,1,0],[0,1,1],[0,0,0]] , 1 : [[0,0,1],[0,1,1],[0,1,0]] , 2 : [[0,0,0],[1,1,0],[0,1,1]] , 3 : [[0,1,0],[1,1,0],[1,0,0]]}
    L = {0 : [[0,1,0],[0,1,0],[0,1,1]] , 1 : [[0,0,0],[1,1,1],[1,0,0]] , 2 : [[1,1,0],[0,1,0],[0,1,0]] , 3 : [[0,0,1],[1,1,1],[0,0,0]]}
    J = {0 : [[0,1,0],[0,1,0],[1,1,0]] , 1 : [[1,0,0],[1,1,1],[0,0,0]] , 2 : [[0,1,1],[0,1,0],[0,1,0]] , 3 : [[0,0,0],[1,1,1],[0,0,1]]}
    T = {0 : [[0,1,0],[1,1,1],[0,0,0]] , 1 : [[0,1,0],[0,1,1],[0,1,0]] , 2 : [[0,0,0],[1,1,1],[0,1,0]] , 3 : [[0,1,0],[1,1,0],[0,1,0]]}
    def __init__(self, sha):
        self.name = sha
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
        self.rotation = 0
    def show(self):
        mat = self.shape[self.rotation]
        if type(mat[0][0]) == int:
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    mat[i][j] = self.color if mat[i][j] else 'Black'
        return mat
    def rotate (self):
        self.rotation = (self.rotation + 1) % len(self.shape)
    def reverse_rotate (self):
        self.rotation = (self.rotation -1) % len(self.shape)
    def width(self):
        return len(self.shape[self.rotation])
class Tetris:
    shapes_order = []
    shapes_order.append(Shape(random.choice(['O','I','S','Z','L','J','T'])))
    Screen = []
    def __init__(self, root:tk , width =300 ):
        pygame.mixer.init()
        pygame.mixer.music.load('tetris.final.mp3')
        pygame.mixer.music.play(-1,0,1000)
        self.level = 0
        self.score = 0
        self.is_over = False
        self.root = root
        self.width, self.height = width , 2 * width
        self.unit = self.width / 10        
        self.frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.root, width=self.width, height= self.height , bg = 'Black')
        self.next = tk.Canvas(self.frame , width= 4 * self.unit , height = 4 * self.unit)
        self.level_label = tk.Label(self.frame, text = f'your level is : {self.level}')
        self.score_label = tk.Label(self.frame , text = f'your score is : {self.score}')
        self.lable = tk.Label(self.frame , text= 'next object')
        self.author = tk.Label(self.frame,text ='music by : \nAref & Radin',fg = 'Red')
        self.canvas.grid(row = 0 , column= 0)
        self.next.grid(row = 1 , column= 1)
        self.lable.grid(row=0 , column= 1)
        self.frame.grid(row= 0 , column= 1)
        self.level_label.grid(row = 2 , column= 1)
        self.score_label.grid(row = 3 , column= 1)
        self.author.grid(row = 4 , column=1)
        self.automove = True
        self.generator()
        self.next_obj_draw()
        self.Origin = [4*self.unit,0]
        self.current = []
        self.delta = 1000
        self.move(self.delta)
        self.root.bind("<Right>",self.move_right)
        self.root.bind("<Left>",self.move_left)
        self.root.bind("<Up>", self.rotate)
        self.root.bind("<Down>", self.speedup)
        self.root.bind("<KeyRelease-Down>" , self.speedup_release)
        self.root.after(self.delta,self.is_game_over)

    def generator(self):
        if not self.is_over:
            Tetris.shapes_order.append(Shape(random.choice(['O','I','S','Z','L','J','T'])))
            Tetris.shapes_order = Tetris.shapes_order[-2:]
    def draw(self, canvas: tk.Canvas, shape:Shape, Origin:list, flag=False):
        '''flag var is about drawing in the main canvas'''
        if flag :
            self.current = []
        for i in range(len(shape.show())) :
            for j in range(len(shape.show()[i])):
                if shape.show()[i][j] != 'Black':
                    x0 = Origin[0]+j*self.unit
                    y0 = Origin[1] + i*self.unit
                    Rect = canvas.create_rectangle( x0,y0,x0+ self.unit , y0+self.unit ,fill= shape.color)
                    if flag:
                        self.current.append(Rect)
    def move_right(self, event):

        if self.collision_check(1,0):
            self.Origin[0]+=self.unit
        self.present_obj_draw()
    def move_left(self, event):

        if self.collision_check(-1,0):
            self.Origin[0]-=self.unit
        self.present_obj_draw()
    def speedup(self, event):
        self.automove = False
        if self.collision_check(0,1):
            self.Origin[1] += self.unit 
            self.present_obj_draw()
        self.automove = True
    def speedup_release(self,event):
        self.automove = True
        self.present_obj_draw()
    def rotate(self, event):
        if self.Origin[0]>= 0 and self.Origin[0]+self.shapes_order[0].width() * self.unit <= 10*self.unit and self.Origin[1] + self.shapes_order[0].width()*self.unit< 20 * self.unit:
            enclosed = list(self.canvas.find_enclosed(self.Origin[0]-self.unit/2, self.Origin[1]-self.unit/2, self.Origin[0]+self.unit/2+self.shapes_order[0].width()*self.unit, self.Origin[1]+self.unit/2+self.shapes_order[0].width()*self.unit))
            for i in self.current:
                if i in enclosed:
                    enclosed.remove(i)
            if not enclosed:
                self.shapes_order[0].rotate()
                self.present_obj_draw()
    def collision_check(self,dx=0,dy=0):
        flag = True
        for i in self.current:
            x0 , y0 , x1 , y1 = self.canvas.coords(i)
            nx0 , ny0 , nx1 , ny1 = x0 + dx*self.unit , y0 + dy *self.unit , x1+dx*self.unit , y1+dy*self.unit
            if nx0<0:
                return False
            if nx1> self.unit*10:
                return False
            if ny1 > 20*self.unit:
                return False
            enclosed = list(self.canvas.find_enclosed(nx0-self.unit/2,ny0-self.unit/2,nx1+self.unit/2,ny1+self.unit/2))
            for j in enclosed:
                if j in self.current:
                    enclosed.remove(j)
            flag = False if enclosed else flag
        return flag
    def move(self,n):
        self.complete_row()
        self.present_obj_draw()
        if self.automove:
            self.present_obj_draw()
            # if self.check_down():
            if self.collision_check(0,1):
                self.Origin[1] += self.unit
                self.present_obj_draw()
            else:
                self.draw(self.canvas,self.shapes_order[0],self.Origin)
                for i in self.current:
                    self.Screen.append(i)
                self.Origin = [4*self.unit, 0]
                self.generator()
                self.next_obj_draw()
                self.present_obj_draw()
                self.complete_row()
        # self.complete_row()
        self.root.after(n,self.move,self.delta)
    def next_obj_draw(self):
        self.next.delete('all')
        self.draw(self.next,self.shapes_order[1],[0,0])
    def present_obj_draw(self):
        for i in self.current:
            self.canvas.delete(i)
        self.draw(self.canvas,self.shapes_order[0],self.Origin,True)
    def complete_row(self):
        scores = {0: 0 ,1:100,2:300,3:600,4:1000}
        row = dict()
        for i in self.canvas.find_all():
            if i not in  self.current:
                pos = self.canvas.coords(i)
                if pos[1] in row:
                    row[pos[1]].append(i)
                else:
                    row[pos[1]] = [i]
        tag = False
        rows = 0
        for j in row:
            if len(row[j]) >= 10:
                rows += 1
                tag = True
                for p in self.canvas.find_all():
                    if self.canvas.coords(p)[1] < self.canvas.coords(row[j][0])[1]:
                        self.canvas.move(p,0,self.unit)
                for k in row[j]:
                    self.canvas.delete(k)
        self.score += scores[rows]
        self.level += 1 if tag else 0
        self.delta -= 50 if tag else 0
        self.level_label.configure(text = f'your level is : {self.level}' )
        self.score_label.configure( text = f'your score is : {self.score}')
    def is_game_over(self):
        enclosed = list(self.canvas.find_enclosed(4*self.unit, 0 , 7*self.unit,3*self.unit))
        for i in self.current:
            if i in enclosed:
                enclosed.remove(i)
        if enclosed:
            self.close()
        self.root.after(self.delta,self.is_game_over)
    def close(self):
        self.root.withdraw()        
        messagebox.showinfo('you lose',f'gameover\nlevel : {self.level}\nscore : {self.score}')
        messagebox.showinfo('try to keep playing', 'you are always a loser\n don\'t forget it')
        self.root.quit()

root = tk.Tk()
game = Tetris(root,350)
root.mainloop()