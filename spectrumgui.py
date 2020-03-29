import tkinter as tk
from tkinter import *
import time
import pyautogui
import math

s = 900
r = s//6
resolution = 3

t = tk.Tk()
t.geometry(str(s)+'x'+str(s))  
t.title('Screenshot') 

c = Canvas(t, width=s, height=s)
c.pack()

filler = []
for i in range(0,49,1):
    if i%4==0:
        filler.append((255, 0, 0))
    elif i%4==1 or i%4==3:
        filler.append((128,0,128))
    else:
        filler.append((0, 0, 255))

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def gradient(color1, color2):
    gradient = []
    diff = (color2[0] - color1[0],color2[1] - color1[1],color2[2] - color1[2])
    for i in range(0, r, resolution):
        color = (color1[0] + diff[0]*i//(r), color1[1] + diff[1]*i//(r), color1[2] + diff[2]*i//(r))
        gradient.append(color)
    return gradient


num = 0
for y in range(0, s, r):
    for x in range(0, s, r):
        gl = gradient(filler[num], filler[num+7])
        gr = gradient(filler[num+1], filler[num+8])
        for k in range(0, r, resolution):
            g = gradient(gl[k//resolution],gr[k//resolution])
            for j in range(0, r, resolution):
                c.create_rectangle(x+j, y+k, x+j+resolution, y+k+resolution, fill = rgb_to_hex(g[j//resolution]), outline = "")
                a = 1
        num+=1
    num+=1

t.mainloop()