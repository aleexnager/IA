import math
import tkinter as tk #GUI
import random
from tkinter import *
from queue import PriorityQueue

# GUI
window = tk.Tk()
window.title("A* en el metro de Lyon")


row = 30 #dimensiones tablero (eje y)
col = row #dimensiones tablero (eje x)
inicio = (0,0) #posicion inicial
final = (random.randint(0,row),random.randint(0,col)) #posicion final
while final == inicio:
    final = (random.randint(0,row),random.randint(0,col)) #asegurarnos de que no tiene el mismo inicio y final

# TABLERO
# El tablero es una lista de listas
grid_cells = [] #lista de celdas
for i in range(row):
    cell_row = [] #lista de celdas por fila
    for j in range(col):
        cell = tk.Label(window, width=3, height=1, background="white", relief="solid", borderwidth=1) #crear celda
        cell.grid(row=j, column=i) #añadir celda a la ventana
        cell_row.append(cell) #añadir celda a la fila
    grid_cells.append(cell_row) #añadir fila a la lista de celdas

# FUNCIONES
def set_color(row, col, color):
    cell = grid_cells[row][col]
    cell.configure(background=color)

# TESTS
set_color(inicio[0],inicio[1],"green")
set_color(final[0],final[1],"red")

window.mainloop() #bucle principal tkinter