import math
import tkinter as tk #GUI
import networkx as nx #grafo
import random
from tkinter import *
from queue import PriorityQueue

# GUI
window = tk.Tk()
window.title("Mapa metro de Lyon")

col = 30 #dimensiones tablero (eje x)
row = 32 #dimensiones tablero (eje y)
init = (0,0) #posicion inicial (row,col)
end = (random.randint(0,row-1),random.randint(0,col-1)) #posicion final
print("Posicion final:",end)
while end == init:
    end = (random.randint(0,row-1),random.randint(0,col-1)) #asegurarnos de que no tiene el mismo inicio y final

# TABLERO
# El tablero es una lista de listas
grid_cells = [] #lista de celdas
for i in range(col):
    cell_row = [] #lista de celdas por fila
    for j in range(row):
        cell = tk.Label(window, width=3, height=1, background="grey85", relief="raised", borderwidth=1) #crear celda
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

# Agregar nodos (estaciones) y atributos (nombre y posicion en tablero)
estaciones = {
    'A1': {'nombre': 'Perrache', 'linea': 'Roja', 'pos': (6,18)}, 'A2': {'nombre': 'Ampère Victor Hugo', 'linea': 'Roja', 'pos': (7,16)}, 
    'AD': {'nombre': 'Bellecour', 'linea': 'Roja', 'pos': (8,14)}, 'A4': {'nombre': 'Cordeliers', 'linea': 'Roja', 'pos': (9,12)}, 
    'AC': {'nombre': 'Hôtel de Ville Louis Pradel', 'linea': 'Roja', 'pos': (9,10)}, 'A6': {'nombre': 'Foch', 'linea': 'Roja', 'pos': (11,10)}, 
    'A7': {'nombre': 'Masséna', 'linea': 'Roja', 'pos': (13,10)}, 'AB': {'nombre': 'Charpennes Charles Hernu', 'linea': 'Roja', 'pos': (15,10)}, 
    'A9': {'nombre': 'République Villeurbanne', 'linea': 'Roja', 'pos': (17,10)}, 'A10': {'nombre': 'Gratte-Ciel', 'linea': 'Roja', 'pos': (19,10)}, 
    'A11': {'nombre': 'Flachet', 'linea': 'Roja', 'pos': (21,10)}, 'A12': {'nombre': 'Cusset', 'linea': 'Roja', 'pos': (23,10)}, 
    'A13': {'nombre': 'Laurent Bonnevay Astroballe', 'linea': 'Roja', 'pos': (25,10)}, 'A14': {'nombre': 'Vaulx-en-Velin La Sole', 'linea': 'Roja', 'pos': (27,10)}, 
    'B1': {'nombre': 'Oullins Gare', 'linea': 'Azul', 'pos': (6,27)}, 'B2': {'nombre': 'Stade de Gerland', 'linea': 'Azul', 'pos': (9,24)}, 
    'B3': {'nombre': 'Debourg', 'linea': 'Azul', 'pos': (10,22)}, 'B4': {'nombre': 'Place Jean Jaurès', 'linea': 'Azul', 'pos': (11,20)}, 
    'B5': {'nombre': 'Jean Macé', 'linea': 'Azul', 'pos': (12,18)}, 'BD': {'nombre': 'Saxe Gambetta', 'linea': 'Azul', 'pos': (12,16)}, 
    'B7': {'nombre': 'Place Guichard Bourse de Travail', 'linea': 'Azul', 'pos': (12,14)}, 'B8': {'nombre': 'Gare Part-Dieu Vivier Merle', 'linea': 'Azul', 'pos': (14,14)}, 
    'B9': {'nombre': 'Brotteaux', 'linea': 'Azul', 'pos': (15,12)}, 'AB': {'nombre': 'Charpennes Charles Hernu', 'linea': 'Azul', 'pos': (15,10)},
    'C1': {'nombre': 'Cuire', 'linea': 'Naranja', 'pos': (9,2)}, 'C2': {'nombre': 'Hénon', 'linea': 'Naranja', 'pos': (7,4)}, 
    'C3': {'nombre': 'Croix-Rousse', 'linea': 'Naranja', 'pos': (8,6)}, 'C4': {'nombre': 'Croix-Paquet', 'linea': 'Naranja', 'pos': (9,8)}, 
    'AC': {'nombre': 'Hôtel de Ville Louis Pradel', 'linea': 'Naranja', 'pos': (9,10)}, 
    'D1': {'nombre': 'Gare de Valse', 'linea': 'Verde', 'pos': (2,6)}, 'D2': {'nombre': 'Valmy', 'linea': 'Verde', 'pos': (2,8)}, 
    'D3': {'nombre': 'Gorge de Loup', 'linea': 'Verde', 'pos': (2,11)}, 'D4': {'nombre': 'Minimes Théätres Romais', 'linea': 'Verde', 'pos': (6,13)}, 
    'AD': {'nombre': 'Bellecour', 'linea': 'Verde', 'pos': (8,14)}, 'D6': {'nombre': 'Guillotière', 'linea': 'Verde', 'pos': (10,15)}, 
    'BD': {'nombre': 'Saxe Gambetta', 'linea': 'Verde', 'pos': (12,16)}, 'D8': {'nombre': 'Garibaldi', 'linea': 'Verde', 'pos': (14,17)}, 
    'D9': {'nombre': 'Sans-Souci', 'linea': 'Verde', 'pos': (16,18)}, 'D10': {'nombre': 'Monplaisir-Lumière', 'linea': 'Verde', 'pos': (18,19)}, 
    'D11': {'nombre': 'Grange Blanche', 'linea': 'Verde', 'pos': (20,20)}, 'D12': {'nombre': 'Laennec', 'linea': 'Verde', 'pos': (22,21)}, 
    'D13': {'nombre': 'Mermoz Pinnel', 'linea': 'Verde', 'pos': (22,24)}, 'D14': {'nombre': 'Parilly', 'linea': 'Verde', 'pos': (22,26)}, 
    'D15': {'nombre': 'Gare de Vénissieux', 'linea': 'Verde', 'pos': (22,29)},
}

for nodo, estacion in estaciones.items(): #para añadir nodos con atributos y acceder a ellos
    metro.add_node(nodo, nombre=estacion['nombre'], linea=estacion['linea'], pos=estacion['pos'])

# Agregar aristas (conexiones) y pesos (distancia)
conexiones = [
    ('A1', 'A2', 5), ('A2', 'AD', 1), ('AD', 'A4', 1), ('A4', 'AC', 1), ('AC', 'A6', 1), ('A6', 'A7', 1), ('A7', 'AB', 1),
    ('AB', 'A9', 1), ('A9', 'A10', 1), ('A10', 'A11', 1), ('A11', 'A12', 1), ('A12', 'A13', 1), ('A13', 'A14', 1),
    ('B1', 'B2', 1), ('B2', 'B3', 1), ('B3', 'B4', 1), ('B4', 'B5', 1), ('B5', 'BD', 1), ('BD', 'B7', 1), ('B7', 'B8', 1),
    ('B8', 'B9', 1), ('B9', 'AB', 1),
    ('C1', 'C2', 1), ('C2', 'C3', 1), ('C3', 'C4', 1), ('C4', 'AC', 1),
    ('D1', 'D2', 1), ('D2', 'D3', 1), ('D3', 'D4', 1), ('D4', 'AD', 1), ('AD', 'D6', 1), ('D6', 'BD', 1), ('BD', 'D8', 1), 
    ('D8', 'D9', 1), ('D9', 'D10', 1), ('D10', 'D11', 1), ('D11', 'D12', 1), ('D12', 'D13', 1), ('D13', 'D14', 1), ('D14', 'D15', 1),
]

for estacion1, estacion2, distancia in conexiones: #para añadir aristas con pesos y acceder a ellos
    metro.add_edge(estacion1, estacion2, distancia=distancia)

# DIBUJAR LINEAS
colores_lineas = {
    'Roja': 'red',
    'Azul': 'blue',
    'Naranja': 'orange',
    'Verde': 'green',
}

estaciones_transbordo = {
    'AB',
    'AC',
    'AD',
    'BD',
}

def unir_y_pintar(nodo1, nodo2):
    #si ambos nodos están en la misma linea, pintar de ese color
    if estaciones[nodo1]['linea'] == estaciones[nodo2]['linea']:
        color = colores_lineas[estaciones[nodo1]['linea']]
    elif nodo1 in estaciones_transbordo: #es un nodo transbordo
        color = colores_lineas[estaciones[nodo2]['linea']]
    elif nodo2 in estaciones_transbordo: #es un nodo transbordo
        color = colores_lineas[estaciones[nodo1]['linea']]
    else: #si no, pintar de color morado (no debería pasar)
        color = 'purple'
        print(f"-",nodo1, nodo2)
    
    pos1 = estaciones[nodo1]['pos']
    pos2 = estaciones[nodo2]['pos']

    # Determinar la dirección de los nodos y pintar en el color correspondiente
    if pos1[0] == pos2[0]: #misma fila
        if pos1[1] < pos2[1]: #misma fila, nodo1 a la izquierda de nodo2
            for col in range(pos1[1], pos2[1] + 1): #pintar desde nodo1 hasta nodo2
                set_color(pos1[0], col, color)
        else: #misma fila, nodo1 a la derecha de nodo2
            for col in range(pos2[1], pos1[1] + 1): #pintar desde nodo2 hasta nodo1
                set_color(pos1[0], col, color)
    elif pos1[1] == pos2[1]: #misma columna
        if pos1[0] < pos2[0]: #misma columna, nodo1 arriba de nodo2
            for row in range(pos1[0], pos2[0] + 1): 
                set_color(row, pos1[1], color)
        else: #misma columna, nodo1 abajo de nodo2
            for row in range(pos2[0], pos1[0] + 1):
                set_color(row, pos1[1], color)
    else: #diagonal
        if pos1[0] < pos2[0] and pos1[1] < pos2[1]: #diagonal, nodo1 arriba-izquierda de nodo2
            row, col = pos1 #posicion inicial
            while row <= pos2[0] and col <= pos2[1]: 
                set_color(row, col, color)
                row += 1
                col += 1
        elif pos1[0] < pos2[0] and pos1[1] > pos2[1]: #diagonal, nodo1 arriba-derecha de nodo2
            row, col = pos1
            while row <= pos2[0] and col >= pos2[1]:
                set_color(row, col, color)
                row += 1
                col -= 1
        elif pos1[0] > pos2[0] and pos1[1] < pos2[1]: #diagonal, nodo1 abajo-izquierda de nodo2
            row, col = pos1
            while row >= pos2[0] and col <= pos2[1]:
                set_color(row, col, color)
                row -= 1
                col += 1
        else: #diagonal, nodo1 abajo-derecha de nodo2
            row, col = pos1
            while row >= pos2[0] and col >= pos2[1]:
                set_color(row, col, color)
                row -= 1
                col -= 1

for estacion1, estacion2, distancia in conexiones:
    unir_y_pintar(estacion1, estacion2)

set_color(5,13,"green") #rellenar un hueco en el mapa

# def dibujar_nodos():
#     for nodo, estacion in estaciones.items():
#         linea = estacion['linea']
#         color = colores_lineas.get(linea, 'black')  # Usar negro como color predeterminado si no se encuentra la línea
#         pos = estacion['pos']
#         if nodo == 'AB': # los colores de los transbordos están marcados como la mezcla de los colores de ambas lineas
#             set_color(pos[0], pos[1], "purple")
#         elif nodo == 'AC':
#             set_color(pos[0], pos[1], "maroon")
#         elif nodo == 'AD':
#             set_color(pos[0], pos[1], "yellow")
#         elif nodo == 'BD':
#             set_color(pos[0], pos[1], "turquoise1")
#         else: # color por defecto
#             set_color(pos[0], pos[1], color)

# dibujar_nodos()

# TESTS
#set_color(init[0],init[1],"green")
#set_color(end[0],end[1],"red")

# distancia total
inicio = 'A1'
destino = 'D15'

# distancia entre dos estaciones
distancia = nx.shortest_path_length(metro, inicio, destino, weight='distancia')
print(f"Distancia entre {inicio} {metro.nodes[inicio]} y {destino}: {distancia}")

# estaciones vecinas
estacion = 'A1'
estaciones_conectadas = list(metro.neighbors(estacion))
print(f"Estaciones conectadas a {estacion} que esta en la pos {nx.get_node_attributes(metro, 'pos')[estacion]}: {estaciones_conectadas}")


window.mainloop() #bucle principal tkinter