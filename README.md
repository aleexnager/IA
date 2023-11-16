# Algorítmo de búsqueda A*

## Algorítmo A* implemnetado en python

### Autores:
- Alejandro Náger Fernández-Calvo (a.nager@alumnos.upm.es)
- X (X@alumnos.upm.es)
- Y (Y@alumnos.upm.es)
- Z (Z@alumnos.upm.es)

### Enunciado:
[Practica IA Lyon 2023](/docs/Practica%20IA%20Lyon%202023.pdf)

## Instalación:
Primero que todo nos aseguraremos de tener python instalado con `pyhton --version`. En caso de no estar instalado lo instalaremos con:
```
sudo apt install pyhton-pip
```
Para el entorno gráfico se ha usado la herramienta GUI `tkinter`. Para instalarla usaremos:
```
sudo apt-get install tkinter
```
Para facilitar el trabajo con grafos en el código también se ha usado la herramienta `networkx`. Para instalarla usaremos:
```
pip-networkx
```

### Posibles mejoras en el código:
Actualmente las estaciones inicio y fin se asignan al final del código de manera manual. También hay que destacar que estamos usando los códigos de las estaciones en lugar de sus nombres por simplicidad pero perfectamente podemos implementar en una o dos lineas que se les pueda llamar por su nombre también.
Las ideas que se me han ocurrido para asignar los valores a las variables inicio y fin son:
  1. Preguntando por ellos y pasando los argumentos por terminal
  2. Haciendo click en el mapa (mucho más compleja)
Sois libres de realizar cualquier modificación en el codigo `main.py` pero cread vuestra propia rama o usad la rama testing antes de hacer merge con la rama principal.

### Recomendaciones:
Se puede ampliar el mapa descomentando la línea 21 y comentando la línea 20
