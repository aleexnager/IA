>[!WARNING]\
>El plagio o intento de copia de este material en el proyecto de la asignatura de Inteligencia Artificial impartida por la ETSIINF de la UPM supondrá un suspenso inmediato. Este contenido es únicamente informativo y de uso didáctico, los autores de este proyecto no nos hacemos responsables del mal uso que se le pueda dar al contenido de este repositorio. ([LICENSE](/LICENSE))

# Algorítmo de búsqueda A*

## Algorítmo A* implemnetado en python

### Autores:
- Alejandro Náger Fernández-Calvo (a.nager@alumnos.upm.es)
- Alfonso del Río Cuesta (alfonso.delrio@alumnos.upm.es)

### Enunciado:
[Practica IA Lyon 2023](/docs/Practica%20IA%20Lyon%202023.pdf)

## Instalación:
Primero que todo nos aseguraremos de tener python instalado con `python --version`. En caso de no estar instalado lo instalaremos con:
```
$ sudo apt-get install python3.6
```
Ahora vamos a instalar dos herramientas, una para el entorno gráfico y otra para trabajar con grafos. El gestor de paquetes de python es `pip`. Para instalarlo usaremos:
```
$ sudo apt install pyhton3-pip
```
Para el entorno gráfico se ha usado la herramienta GUI `tkinter`. Para instalarla usaremos:
```
$ sudo apt-get install python3-tk
```
Para facilitar el trabajo con grafos en el código también se ha usado el paquete `networkx`. Para instalarlo usaremos:
```
$ pip install networkx
```

## Posibles mejoras en el código:
Actualmente las estaciones inicio y fin se asignan al final del código de manera manual.
  1. Haciendo click en el mapa (mucho más compleja)

>[!TIP]
>Se puede ampliar el mapa descomentando la `línea 21` y comentando la `línea 20`
