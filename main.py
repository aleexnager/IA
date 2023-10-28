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
#init = (0,0) #posicion inicial (row,col)
#end = (random.randint(0,row-1),random.randint(0,col-1)) #posicion final
#print("Posicion final:",end)
#while end == init:
#    end = (random.randint(0,row-1),random.randint(0,col-1)) #asegurarnos de que no tiene el mismo inicio y final

# TABLERO
# El tablero es una lista de listas
grid_cells = [] #lista de celdas
for i in range(col):
    cell_row = [] #lista de celdas por fila
    for j in range(row):
        cell = tk.Label(window, width=3, height=1, background="grey85", relief="raised", borderwidth=1) #crear celda
        #cell = tk.Label(window, width=5, height=2, background="grey85", relief="raised", borderwidth=1) #mapa más grande
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

# Agregar aristas (conexiones) y pesos (distancia en metros)
# En nuestro caso el peso es la distancia entre dos estaciones pero podría ser el tiempo que tarda en llegar de una a otra
# Por tanto, nosotros comprobamos el camino más corto pero no el más rápido
conexiones = [
    ('A1', 'A2', 416), ('A2', 'AD', 654), ('AD', 'A4', 660), ('A4', 'AC', 460), ('AC', 'A6', 670), ('A6', 'A7', 660), ('A7', 'AB', 830),
    ('AB', 'A9', 770), ('A9', 'A10', 750), ('A10', 'A11', 590), ('A11', 'A12', 840), ('A12', 'A13', 680), ('A13', 'A14', 1050),
    ('B1', 'B2', 1780), ('B2', 'B3', 570), ('B3', 'B4', 800), ('B4', 'B5', 950), ('B5', 'BD', 960), ('BD', 'B7', 610), ('B7', 'B8', 990),
    ('B8', 'B9', 580), ('B9', 'AB', 440),
    ('C1', 'C2', 821), ('C2', 'C3', 659), ('C3', 'C4', 620), ('C4', 'AC', 400),
    ('D1', 'D2', 695), ('D2', 'D3', 955), ('D3', 'D4', 1740), ('D4', 'AD', 660), ('AD', 'D6', 710), ('D6', 'BD', 400), ('BD', 'D8', 610), 
    ('D8', 'D9', 900), ('D9', 'D10', 600), ('D10', 'D11', 640), ('D11', 'D12', 760), ('D12', 'D13', 1040), ('D13', 'D14', 1190), ('D14', 'D15', 1600),
]

for estacion1, estacion2, distancia in conexiones: #para añadir aristas con pesos y acceder a ellos
    metro.add_edge(estacion1, estacion2, distancia=distancia)

# DIBUJAR LINEAS
colores_lineas = {
    'Roja': 'red',
    'Azul': 'blue',
    'Naranja': 'orange',
    'Verde': 'green3',
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
        #Calcular la pendiente entre los dos nodos
        dx = pos2[1] - pos1[1]
        dy = pos2[0] - pos1[0]
        if abs(dx) > abs(dy):  # mayor cambio en x
            if dx > 0:
                # nodo2 a la derecha de nodo1
                for col in range(pos1[1], pos2[1] + 1):
                    row = pos2[0] + (col - pos2[1]) * dy / dx
                    set_color(int(row), col, color)
            else:
                # nodo2 a la izquierda de nodo1
                for col in range(pos2[1], pos1[1] + 1):
                    row = pos1[0] + (col - pos1[1]) * dy / dx
                    set_color(int(row), col, color)
        else:  # mayor cambio en y
            if dy > 0:
                # nodo2 abajo de nodo1
                for row in range(pos1[0], pos2[0] + 1):
                    col = pos2[1] + (row - pos2[0]) * dx / dy
                    set_color(row, int(col), color)
            else:
                # nodo2 arriba de nodo1
                for row in range(pos2[0], pos1[0] + 1):
                    col = pos1[1] + (row - pos1[0]) * dx / dy
                    set_color(row, int(col), color)

for estacion1, estacion2, distancia in conexiones:
    unir_y_pintar(estacion1, estacion2)

# DIBUJA NODOS
# Color nodos (para diferenciarlos del camino)
colores_nodos = {
    'Roja': 'red4',
    'Azul': 'blue4',
    'Naranja': 'orange4',
    'Verde': 'dark green',
}

def dibujar_nodos():
    for nodo, estacion in estaciones.items():
        linea = estacion['linea']
        color = colores_nodos.get(linea, 'black')  # Usar negro como color predeterminado si no se encuentra la línea
        pos = estacion['pos']
        if nodo in estaciones_transbordo:
            set_color(pos[0], pos[1], "yellow")
        else: # color por defecto
            set_color(pos[0], pos[1], color)

dibujar_nodos()

# MOSTRAR INFO
# Función para mostrar información de una estación en el mapa
def mostrar_info(event, estacion):
    nombre = metro.nodes[estacion]['nombre']
    lineas = set()  # Utilizamos un conjunto para evitar duplicados
    lineas.add(metro.nodes[estacion]['linea'])  # Agregamos la línea de la estación actual

    if estacion in estaciones_transbordo:  # Es estación transbordo
        for vecino in metro.neighbors(estacion):
            linea_vecino = metro.nodes[vecino]['linea']
            lineas.add(linea_vecino)  # Agregamos las líneas de los vecinos al conjunto
        lineas_str = ', '.join(lineas)
        info_label.config(text=f"Nombre: {nombre}\nLíneas: {lineas_str}")
    else:  # No es estación transbordo
        linea = metro.nodes[estacion]['linea']
        info_label.config(text=f"Nombre: {nombre}\nLínea: {linea}")

# Etiqueta para mostrar información
info_label = tk.Label(window, text="", background="grey85") #crear etiqueta
info_label.grid(row=row, columnspan=col) #añadir etiqueta a la ventana

# Configurar eventos de ratón para cada celda
for i in range(col): 
    for j in range(row):
        estacion = None
        for nodo, pos in estaciones.items():
            if pos['pos'] == (i, j):
                estacion = nodo #guardar estacion
                break
        if estacion: #si estaciópn tiene valor
            cell = grid_cells[i][j] #obtener celda
            cell.bind("<Enter>", lambda event, estacion=estacion: mostrar_info(event, estacion)) #mostrar info al pasar el ratón por encima
            cell.bind("<Leave>", lambda event: info_label.config(text="")) #borrar info al quitar el ratón

# ALGORITMO

# TESTS
#set_color(init[0],init[1],"green")
#set_color(end[0],end[1],"red")

# distancia total
inicio = 'A1'
destino = 'B1'

# distancia entre dos estaciones
distancia = nx.shortest_path_length(metro, inicio, destino, weight='distancia')
print(f"Distancia entre {inicio} {metro.nodes[inicio]} y {destino}: {distancia} m")

# estaciones vecinas
estacion = 'A1'
estaciones_conectadas = list(metro.neighbors(estacion))
print(f"Estaciones conectadas a {estacion} que esta en la pos {nx.get_node_attributes(metro, 'pos')[estacion]}: {estaciones_conectadas}")


window.mainloop() #bucle principal tkinter