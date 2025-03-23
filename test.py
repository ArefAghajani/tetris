import tkinter as tk
Screen = (300, 600)
root = tk.Tk()
frame = tk.Frame(root, bg = 'Gray')
canvas = tk.Canvas(frame,width=Screen[0],height= Screen[1] , bg = 'Black')
canvas.grid(row= 1 , column= 1 , padx= 30 , pady = 30)
frame.grid(row = 0 , column=0)

rect = canvas.create_rectangle(10,10,290,20,fill = 'Red')
i = 1
def blink0(n = 200):
    global i
    print(n)
    if n < 0 :
        i = -1 * i
    elif n > 200 :
        i = -1 * i
    canvas.itemconfig(rect,fill = 'Blue')
    root.after(n,lambda : blink1(n-5 * i))
def blink1(n = 200):
    print(n)
    canvas.itemconfig(rect,fill = 'Red')
    root.after(n,lambda : blink0(n-5 * i))
blink0()
def mat2can (mat:list):

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]:
                x = j*Screen[0]/10 
                y = i*Screen[1]/20
                canvas.create_rectangle(x,y,x + Screen[0]/10, y + Screen[1]/20,fill = 'Green')
mat = [[0,1],[0,1],[1,1]]
mat2can(mat)








tk.mainloop()
