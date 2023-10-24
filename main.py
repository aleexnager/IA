import math
import tkinter as tk #GUI
import networkx as nx #grafo
import random
from tkinter import *
from queue import PriorityQueue

# GUI
window = tk.Tk()
window.title("Mapa metro de Lyon")

row = 32 #dimensiones tablero (eje y)
col = 30 #dimensiones tablero (eje x)
init = (0,0) #posicion inicial (row,col)
end = (random.randint(0,row-1),random.randint(0,col-1)) #posicion final
print("Posicion final:",end)
while end == init:
    end = (random.randint(0,row-1),random.randint(0,col-1)) #asegurarnos de que no tiene el mismo inicio y final

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

# LINEAS DE METRO
# Crear un grafo
metro = nx.Graph()

# Agregar nodos (estaciones)
estaciones = {
    'A1', 'A2', 'AD', 'A4', 'AC', 'A6', 'A7', 'AB', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14',
    'B1', 'B2', 'B3', 'B4', 'B5', 'BD', 'B7', 'B8', 'B9', 'AB',
    'C1', 'C2', 'C3', 'C4', 'AC',
    'D1', 'D2', 'D3', 'D4', 'AD', 'D6', 'BD', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15',
}

metro.add_nodes_from(estaciones)

# Agregar aristas (conexiones)
conexiones = [
    ('A1', 'A2'), ('A2', 'AD'), ('AD', 'A4'), ('A4', 'AC'), ('AC', 'A6'), ('A6', 'A7'), ('A7', 'AB'), ('AB', 'A9'),
    ('A9', 'A10'), ('A10', 'A11'), ('A11', 'A12'), ('A12', 'A13'), ('A13', 'A14'),
    ('B1', 'B2'), ('B2', 'B3'), ('B3', 'B4'), ('B4', 'B5'), ('B5', 'BD'), ('BD', 'B7'), ('B7', 'B8'), ('B8', 'B9'),
    ('B9', 'AB'),
    ('C1', 'C2'), ('C2', 'C3'), ('C3', 'C4'), ('C4', 'AC'),
    ('D1', 'D2'), ('D2', 'D3'), ('D3', 'D4'), ('D4', 'AD'), ('AD', 'D6'), ('D6', 'BD'), ('BD', 'D8'), ('D8', 'D9'),
    ('D9', 'D10'), ('D10', 'D11'), ('D11', 'D12'), ('D12', 'D13'), ('D13', 'D14'), ('D14', 'D15'),
]

metro.add_edges_from(conexiones)

# Asignar pesos de 1 a todas las aristas
for u, v in metro.edges:
    metro[u][v]['distancia'] = 1

# TESTS
set_color(init[0],init[1],"green")
set_color(end[0],end[1],"red")

# distancia total
inicio = 'A1'
destino = 'D15'

distancia_total = nx.shortest_path_length(metro, source=inicio, target=destino, weight='distancia')
print("Distancia total:", distancia_total)

# estaciones vecinas
estacion = 'D15'
estaciones_conectadas = list(metro.neighbors(estacion))
print(f"Estaciones conectadas a {estacion}: {estaciones_conectadas}")


window.mainloop() #bucle principal tkinter