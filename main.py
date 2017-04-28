
__autor__ = 'Fernando  Berrospi'

#LIBRERIAS
from tkinter import *
from math import *
from tkinter import messagebox
from random import *



#CONSTANTES
width = 1000
height = 600
background_color = '#D6EAF8'
tree_color = 9440319
change_tree_color = 2

heigh_tree = 115
level_tree = 15

angle_1 = 50
angle_2 = 70

x0 = width/2
y0 = height - 50
x1 = x0
y1 = y0 - heigh_tree

size = 7

#VENTANA
window = Tk()
window.title('Arbol Digital')
window.geometry(str(width)+'x'+str(height))
window.resizable(width = False, height = False)
#window.iconbitmap()

#CANVAS
canvas = Canvas(window,width = width, height = height, bg = background_color)
canvas.pack()

#METODOS AUXILIARES
def distance_points(xi,yi,xf,yf):
    return sqrt((xf-xi)**2 +(yf-y1)**2)
    
def tg(angle):
    return sin(angle)/cos(angle)

def hexa(n):
    return hex(n).replace('0x','#')


#ARBOL DIGITAL
def itera_tree_digital(xi,yi,xf,yf,angle_1,angle_2,n,heigh_tree,size,tree_color):
    try:
        if n > 0 and yi > yf and xf - xi != 0:
            if size == 1 :
                size = 2
            d = heigh_tree
            angle_temp = (90 + randint(angle_1,angle_2))*pi/180
            m = (yf-yi)/(xf-xi)
            m1 = (m-tg(angle_temp))/(1+tg(angle_temp)*m) #Derecha
            m2 = (m+tg(angle_temp))/(1-tg(angle_temp)*m) #Izquierda
            
            x1 = ((m1-m)*xf + m*(-d)) / (m1-m)
            y1 = m1*(x1-xf) + yf
            canvas.create_line(xf,yf,x1,y1,width=size,fill= hexa(tree_color))
            itera_tree_digital(xf,yf,x1,y1,angle_1,angle_2,n-1,heigh_tree/uniform(1,2),size-1,tree_color - change_tree_color)

            x2 = ((m2-m)*xf + m*(d))/(m2-m) 
            y2 = m2*(x2-xf) + yf
            canvas.create_line(xf,yf,x2,y2,width=size,fill= hexa(tree_color))
            itera_tree_digital(xf,yf,x2,y2,angle_1,angle_2,n-1,heigh_tree/uniform(1,2),size-1,tree_color - change_tree_color)
    except:
        return

def create_tree_digital(xi,yi,xf,yf,angle_1,angle_2,n,heigh_tree,size,tree_color):
    canvas.create_line(xi,yi,xf,yf,width=size,fill= hexa(tree_color))
    
    x1,y1 = width/2 - heigh_tree*2/3, yf - heigh_tree*2/3
    x2,y2 = width/2 + heigh_tree*2/3 , yf - heigh_tree*2/3
    
    canvas.create_line(xf,yf,x1,y1,width=size-1,fill= hexa(tree_color - change_tree_color))
    canvas.create_line(xf,yf,x2,y2,width=size-1,fill= hexa(tree_color - change_tree_color))
    
    itera_tree_digital(xf,yf,x1,y1,angle_1,angle_2,n-1,heigh_tree/uniform(1,2),size-2,tree_color - change_tree_color*2)
    itera_tree_digital(xf,yf,x2,y2,angle_1,angle_2,n-1,heigh_tree/uniform(1,2),size-2,tree_color - change_tree_color*2)

    canvas.create_rectangle(0,yi,width,height,fill='#A2D9CE')
    
        

create_tree_digital(x0,y0,x1,y1,angle_1,angle_2,level_tree,heigh_tree,size,tree_color)
mainloop()
