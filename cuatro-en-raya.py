import sys
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

# Inicializa todos los modulos de PyGame
pygame.init()

# Configuracion de pantalla Hay un ancho de 825 pixeles y 800 pixeles de alto de Pantalla. No se establece opciones
# adicionales (0). La profundidad a utilizar en los colores seran de 32 bits.
screen = pygame.display.set_mode((825, 800), 0, 32)
# El titulo de la ventana del Juego, sera "4 en raya".
pygame.display.set_caption('4 en raya')

# Colores en codigo RGB
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (195, 195, 195)
rojo = (255, 0, 0)
amarillo = (255, 216, 0)

screen.fill(blanco)  # La pantalla tendra un fondo color Blanco.


# Funciones de Posicion
def posicionHijo(posicion_cuadro_padre, personalizado=False):
    x = posicion_cuadro_padre[0]
    y = posicion_cuadro_padre[1]
    if personalizado:
        return (x + 100, y + 25)
    else:
        return (x + 50, y + 50)


def posicionPadre(posicion, anchoXAlto, fila, raiz=False, personalizado=False):
    x = posicion[0]
    y = posicion[1]
    ancho = anchoXAlto[0]
    alto = anchoXAlto[1]
    # PRIMERA FILA
    if raiz == False and fila == 1 and personalizado == False:
        margen = 20
        return (x + ancho + margen, 1)
    # MAS DE 1 FILA
    elif raiz and fila >= 2 and personalizado == False:
        margen = 20
        return (1, y + alto + margen)
    elif raiz == False and fila >= 2 and personalizado == False:
        margen = 20
        return (x + ancho + margen, y)
    # SEPTIMA FILA - POSICION PERSONALIZADO
    elif raiz and personalizado:
        margen = 20
        x = x - 50
        return (x, y + alto + margen)


# CUADROS PADRE
# POSICION CUADROS PADRE
# PRIMERA FILA
posicionPadreCuadro = [1, 1]
anchoXAltoCuadro = [100, 100]
posicionPadreCuadro2 = posicionPadre(posicionPadreCuadro, anchoXAltoCuadro, 1)
posicionPadreCuadro3 = posicionPadre(posicionPadreCuadro2, anchoXAltoCuadro, 1)
posicionPadreCuadro4 = posicionPadre(posicionPadreCuadro3, anchoXAltoCuadro, 1)
posicionPadreCuadro5 = posicionPadre(posicionPadreCuadro4, anchoXAltoCuadro, 1)
posicionPadreCuadro6 = posicionPadre(posicionPadreCuadro5, anchoXAltoCuadro, 1)
posicionPadreCuadro7 = posicionPadre(posicionPadreCuadro6, anchoXAltoCuadro, 1)

# SEGUNDA FILA
posicionPadreCuadro8 = posicionPadre(posicionPadreCuadro, anchoXAltoCuadro, 2, True)
posicionPadreCuadro9 = posicionPadre(posicionPadreCuadro8, anchoXAltoCuadro, 2)
posicionPadreCuadro10 = posicionPadre(posicionPadreCuadro9, anchoXAltoCuadro, 2)
posicionPadreCuadro11 = posicionPadre(posicionPadreCuadro10, anchoXAltoCuadro, 2)
posicionPadreCuadro12 = posicionPadre(posicionPadreCuadro11, anchoXAltoCuadro, 2)
posicionPadreCuadro13 = posicionPadre(posicionPadreCuadro12, anchoXAltoCuadro, 2)
posicionPadreCuadro14 = posicionPadre(posicionPadreCuadro13, anchoXAltoCuadro, 2)

# TERCERA FILA
posicionPadreCuadro15 = posicionPadre(posicionPadreCuadro8, anchoXAltoCuadro, 3, True)
posicionPadreCuadro16 = posicionPadre(posicionPadreCuadro15, anchoXAltoCuadro, 3)
posicionPadreCuadro17 = posicionPadre(posicionPadreCuadro16, anchoXAltoCuadro, 3)
posicionPadreCuadro18 = posicionPadre(posicionPadreCuadro17, anchoXAltoCuadro, 3)
posicionPadreCuadro19 = posicionPadre(posicionPadreCuadro18, anchoXAltoCuadro, 3)
posicionPadreCuadro20 = posicionPadre(posicionPadreCuadro19, anchoXAltoCuadro, 3)
posicionPadreCuadro21 = posicionPadre(posicionPadreCuadro20, anchoXAltoCuadro, 3)

# CUARTA FILA
posicionPadreCuadro22 = posicionPadre(posicionPadreCuadro15, anchoXAltoCuadro, 4, True)
posicionPadreCuadro23 = posicionPadre(posicionPadreCuadro22, anchoXAltoCuadro, 4)
posicionPadreCuadro24 = posicionPadre(posicionPadreCuadro23, anchoXAltoCuadro, 4)
posicionPadreCuadro25 = posicionPadre(posicionPadreCuadro24, anchoXAltoCuadro, 4)
posicionPadreCuadro26 = posicionPadre(posicionPadreCuadro25, anchoXAltoCuadro, 4)
posicionPadreCuadro27 = posicionPadre(posicionPadreCuadro26, anchoXAltoCuadro, 4)
posicionPadreCuadro28 = posicionPadre(posicionPadreCuadro27, anchoXAltoCuadro, 4)
# QUINTA FILA
posicionPadreCuadro29 = posicionPadre(posicionPadreCuadro22, anchoXAltoCuadro, 5, True)
posicionPadreCuadro30 = posicionPadre(posicionPadreCuadro29, anchoXAltoCuadro, 5)
posicionPadreCuadro31 = posicionPadre(posicionPadreCuadro30, anchoXAltoCuadro, 5)
posicionPadreCuadro32 = posicionPadre(posicionPadreCuadro31, anchoXAltoCuadro, 5)
posicionPadreCuadro33 = posicionPadre(posicionPadreCuadro32, anchoXAltoCuadro, 5)
posicionPadreCuadro34 = posicionPadre(posicionPadreCuadro33, anchoXAltoCuadro, 5)
posicionPadreCuadro35 = posicionPadre(posicionPadreCuadro34, anchoXAltoCuadro, 5)
# SEXTA FILA
posicionPadreCuadro36 = posicionPadre(posicionPadreCuadro29, anchoXAltoCuadro, 6, True)
posicionPadreCuadro37 = posicionPadre(posicionPadreCuadro36, anchoXAltoCuadro, 6)
posicionPadreCuadro38 = posicionPadre(posicionPadreCuadro37, anchoXAltoCuadro, 6)
posicionPadreCuadro39 = posicionPadre(posicionPadreCuadro38, anchoXAltoCuadro, 6)
posicionPadreCuadro40 = posicionPadre(posicionPadreCuadro39, anchoXAltoCuadro, 6)
posicionPadreCuadro41 = posicionPadre(posicionPadreCuadro40, anchoXAltoCuadro, 6)
posicionPadreCuadro42 = posicionPadre(posicionPadreCuadro41, anchoXAltoCuadro, 6)

# SEPTIMA FILA
posicionPadreCuadro43 = posicionPadre(posicionPadreCuadro39, anchoXAltoCuadro, 7, True, True)

# CIRCULO HIJOS - PROPIEDADES
radio_relleno = (50, 50)
colores = {
    1: gris,
    2: gris,
    3: gris,
    4: gris,
    5: gris,
    6: gris,
    7: gris,
    8: gris,
    9: gris,
    10: gris,
    11: gris,
    12: gris,
    13: gris,
    14: gris,
    15: gris,
    16: gris,
    17: gris,
    18: gris,
    19: gris,
    20: gris,
    21: gris,
    22: gris,
    23: gris,
    24: gris,
    25: gris,
    26: gris,
    27: gris,
    28: gris,
    29: gris,
    30: gris,
    31: gris,
    32: gris,
    33: gris,
    34: gris,
    35: gris,
    36: gris,
    37: gris,
    38: gris,
    39: gris,
    40: gris,
    41: gris,
    42: gris
}
# LETRAS HIJOS
# Fuente de Texto de los Cuadros Hijos
# Creamos un Objeto Fuente de un Archivo. La fuente a utilizar es el freesansbold.ttf y el tamaño establecido es de 20px.
fuenteTexto = pygame.font.Font('freesansbold.ttf', 20)

# SEPTIMA FILA
# Se renderiza el Objeto Fuente en otro Objeto capaz de ser Renderizado en Pantalla, este objeto es llamado como Objeto Surface/Superficie.
# A la hora de Renderizar le decimos que el Texto sera "LIMPIAR TABLERO", que el Antialias trabajara en ese Objeto Surface y que el color del texto sera Blanco, y el fondo sera de un color Negro.
# El Objeto Surface no tiene posicion.
texto_del_cuadro_surface43 = fuenteTexto.render('LIMPIAR TABLERO', True, blanco, negro)
# POSICION LETRAS HIJO
# LIMPIAR TABLERO
# SEPTIMA FILA
# El get_rect: Crea un nuevo Rect con el tamaño del Surface y se ubicara en la posicion x,y (0,0).
texto_del_cuadro_rect43 = texto_del_cuadro_surface43.get_rect()
# Para modificar la posicion del Rect utilizaremos Center.
texto_del_cuadro_rect43.center = (posicionHijo(posicionPadreCuadro43, True))

# Bloque Padre Detectado por Eventos de PyGames
# FILA 1
# Rect: El Objeto Pygame almacenara las posiciones del Rect (Rectangulo) (X,Y,Width,Height).
cuadroPadre1 = pygame.Rect(posicionPadreCuadro[0], posicionPadreCuadro[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre2 = pygame.Rect(posicionPadreCuadro2[0], posicionPadreCuadro2[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre3 = pygame.Rect(posicionPadreCuadro3[0], posicionPadreCuadro3[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre4 = pygame.Rect(posicionPadreCuadro4[0], posicionPadreCuadro4[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre5 = pygame.Rect(posicionPadreCuadro5[0], posicionPadreCuadro5[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre6 = pygame.Rect(posicionPadreCuadro6[0], posicionPadreCuadro6[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre7 = pygame.Rect(posicionPadreCuadro7[0], posicionPadreCuadro7[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
# FILA 2
cuadroPadre8 = pygame.Rect(posicionPadreCuadro8[0], posicionPadreCuadro8[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre9 = pygame.Rect(posicionPadreCuadro9[0], posicionPadreCuadro9[1], anchoXAltoCuadro[0], anchoXAltoCuadro[1])
cuadroPadre10 = pygame.Rect(posicionPadreCuadro10[0], posicionPadreCuadro10[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre11 = pygame.Rect(posicionPadreCuadro11[0], posicionPadreCuadro11[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre12 = pygame.Rect(posicionPadreCuadro12[0], posicionPadreCuadro12[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre13 = pygame.Rect(posicionPadreCuadro13[0], posicionPadreCuadro13[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre14 = pygame.Rect(posicionPadreCuadro14[0], posicionPadreCuadro14[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
# FILA 3
cuadroPadre15 = pygame.Rect(posicionPadreCuadro15[0], posicionPadreCuadro15[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre16 = pygame.Rect(posicionPadreCuadro16[0], posicionPadreCuadro16[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre17 = pygame.Rect(posicionPadreCuadro17[0], posicionPadreCuadro17[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre18 = pygame.Rect(posicionPadreCuadro18[0], posicionPadreCuadro18[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre19 = pygame.Rect(posicionPadreCuadro19[0], posicionPadreCuadro19[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre20 = pygame.Rect(posicionPadreCuadro20[0], posicionPadreCuadro20[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre21 = pygame.Rect(posicionPadreCuadro21[0], posicionPadreCuadro21[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
# FILA 4
cuadroPadre22 = pygame.Rect(posicionPadreCuadro22[0], posicionPadreCuadro22[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre23 = pygame.Rect(posicionPadreCuadro23[0], posicionPadreCuadro23[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre24 = pygame.Rect(posicionPadreCuadro24[0], posicionPadreCuadro24[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre25 = pygame.Rect(posicionPadreCuadro25[0], posicionPadreCuadro25[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre26 = pygame.Rect(posicionPadreCuadro26[0], posicionPadreCuadro26[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre27 = pygame.Rect(posicionPadreCuadro27[0], posicionPadreCuadro27[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre28 = pygame.Rect(posicionPadreCuadro28[0], posicionPadreCuadro28[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
# FILA 5
cuadroPadre29 = pygame.Rect(posicionPadreCuadro29[0], posicionPadreCuadro29[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre30 = pygame.Rect(posicionPadreCuadro30[0], posicionPadreCuadro30[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre31 = pygame.Rect(posicionPadreCuadro31[0], posicionPadreCuadro31[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre32 = pygame.Rect(posicionPadreCuadro32[0], posicionPadreCuadro32[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre33 = pygame.Rect(posicionPadreCuadro33[0], posicionPadreCuadro33[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre34 = pygame.Rect(posicionPadreCuadro34[0], posicionPadreCuadro34[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre35 = pygame.Rect(posicionPadreCuadro35[0], posicionPadreCuadro35[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
# FILA 6
cuadroPadre36 = pygame.Rect(posicionPadreCuadro36[0], posicionPadreCuadro36[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre37 = pygame.Rect(posicionPadreCuadro37[0], posicionPadreCuadro37[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre38 = pygame.Rect(posicionPadreCuadro38[0], posicionPadreCuadro38[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre39 = pygame.Rect(posicionPadreCuadro39[0], posicionPadreCuadro39[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre40 = pygame.Rect(posicionPadreCuadro40[0], posicionPadreCuadro40[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre41 = pygame.Rect(posicionPadreCuadro41[0], posicionPadreCuadro41[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
cuadroPadre42 = pygame.Rect(posicionPadreCuadro42[0], posicionPadreCuadro42[1], anchoXAltoCuadro[0],
                            anchoXAltoCuadro[1])
# FILA 7
cuadroPadre43 = pygame.Rect(posicionPadreCuadro43[0], posicionPadreCuadro43[1], anchoXAltoCuadro[0] + 100, 50)

# Coleccion Posiciones Padre
# Control de Bloques clickeados, solo debe de ser 1 vez
columna_circulos_hijo = {
    "columna_1": {"completo": False, "filas": {
        1: [False, 1],
        2: [False, 8],
        3: [False, 15],
        4: [False, 22],
        5: [False, 29],
        6: [False, 36]
    }
                  },
    "columna_2": {"completo": False, "filas": {
        1: [False, 2],
        2: [False, 9],
        3: [False, 16],
        4: [False, 23],
        5: [False, 30],
        6: [False, 37]
    }
                  },
    "columna_3": {"completo": False, "filas": {
        1: [False, 3],
        2: [False, 10],
        3: [False, 17],
        4: [False, 24],
        5: [False, 31],
        6: [False, 38]
    }
                  },
    "columna_4": {"completo": False, "filas": {
        1: [False, 4],
        2: [False, 11],
        3: [False, 18],
        4: [False, 25],
        5: [False, 32],
        6: [False, 39]
    }
                  },
    "columna_5": {"completo": False, "filas": {
        1: [False, 5],
        2: [False, 12],
        3: [False, 19],
        4: [False, 26],
        5: [False, 33],
        6: [False, 40]
    }
                  },
    "columna_6": {"completo": False, "filas": {
        1: [False, 6],
        2: [False, 13],
        3: [False, 20],
        4: [False, 27],
        5: [False, 34],
        6: [False, 41]
    }
                  },
    "columna_7": {"completo": False, "filas": {
        1: [False, 7],
        2: [False, 14],
        3: [False, 21],
        4: [False, 28],
        5: [False, 35],
        6: [False, 42]
    }
                  }
}


# Funcion que determina las maneras de Ganar y retorna True si se cumple alguno por X jugador.
def ganar(colores):
    jugadores = (rojo, amarillo)
    for jugador in range(len(jugadores)):
        # CONDICION PARA GANAR POR FILAS
        for i in range(4):
            if colores[1 + i] == jugadores[jugador] and colores[2 + i] == jugadores[jugador] and colores[3 + i] == \
                    jugadores[jugador] and colores[4 + i] == jugadores[jugador]:
                return True
            elif colores[8 + i] == jugadores[jugador] and colores[9 + i] == jugadores[jugador] and colores[10 + i] == \
                    jugadores[jugador] and colores[11 + i] == jugadores[jugador]:
                return True
            elif colores[15 + i] == jugadores[jugador] and colores[16 + i] == jugadores[jugador] and colores[17 + i] == \
                    jugadores[jugador] and colores[18 + i] == jugadores[jugador]:
                return True
            elif colores[22 + i] == jugadores[jugador] and colores[23 + i] == jugadores[jugador] and colores[24 + i] == \
                    jugadores[jugador] and colores[25 + i] == jugadores[jugador]:
                return True
            elif colores[29 + i] == jugadores[jugador] and colores[30 + i] == jugadores[jugador] and colores[31 + i] == \
                    jugadores[jugador] and colores[32 + i] == jugadores[jugador]:
                return True
            elif colores[36 + i] == jugadores[jugador] and colores[37 + i] == jugadores[jugador] and colores[38 + i] == \
                    jugadores[jugador] and colores[39 + i] == jugadores[jugador]:
                return True
        # CONDICION PARA GANAR POR COLUMNAS
        for c in range(3):
            e = 7 * c
            if colores[1 + e] == jugadores[jugador] and colores[8 + e] == jugadores[jugador] and colores[15 + e] == \
                    jugadores[jugador] and colores[22 + e] == jugadores[jugador]:
                return True
            elif colores[2 + e] == jugadores[jugador] and colores[9 + e] == jugadores[jugador] and colores[16 + e] == \
                    jugadores[jugador] and colores[23 + e] == jugadores[jugador]:
                return True
            elif colores[3 + e] == jugadores[jugador] and colores[10 + e] == jugadores[jugador] and colores[17 + e] == \
                    jugadores[jugador] and colores[24 + e] == jugadores[jugador]:
                return True
            elif colores[4 + e] == jugadores[jugador] and colores[11 + e] == jugadores[jugador] and colores[18 + e] == \
                    jugadores[jugador] and colores[25 + e] == jugadores[jugador]:
                return True
            elif colores[5 + e] == jugadores[jugador] and colores[12 + e] == jugadores[jugador] and colores[19 + e] == \
                    jugadores[jugador] and colores[26 + e] == jugadores[jugador]:
                return True
            elif colores[6 + e] == jugadores[jugador] and colores[13 + e] == jugadores[jugador] and colores[20 + e] == \
                    jugadores[jugador] and colores[27 + e] == jugadores[jugador]:
                return True
            elif colores[7 + e] == jugadores[jugador] and colores[14 + e] == jugadores[jugador] and colores[21 + e] == \
                    jugadores[jugador] and colores[28 + e] == jugadores[jugador]:
                return True
        # CONDICION PARA GANAR POR X
        # MOVER EN MANERA HORIZONTAL
        for x in range(4):
            for y in range(3):
                z = 7 * y
                if colores[1 + z + x] == jugadores[jugador] and colores[9 + z + x] == jugadores[jugador] and colores[
                    17 + z + x] == jugadores[jugador] and colores[25 + z + x] == jugadores[jugador]:
                    return True
                elif colores[22 + z + x] == jugadores[jugador] and colores[16 + z + x] == jugadores[jugador] and \
                        colores[10 + z + x] == jugadores[jugador] and colores[4 + z + x] == jugadores[jugador]:
                    return True


# Variable que contea los Turnos del Juego
turno = 0
while True:  # El juego entra en un Loop
    # pygame.event.get(): Esto obtendra todos los eventos y los eliminara de la Cola.
    for event in pygame.event.get():
        # Si en todos los eventos, hay un evento del tipo QUIT.
        if event.type == QUIT:
            # Todos los modulos de pygame habilitados previamente por pygame.init(), seran inhabilitados.
            pygame.quit()
            # La ventana se cerrara.
            sys.exit()
        # Si en todos los eventos, hay un evento del tipo pygame.MOUSEBUTTONDOWN.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Detectara dentro del evento de Tipo MOUSEBUTTONDOWN si su SubEvento Button tiene el valor 1.
            # 1 es el Boton Izquierdo, 2 es el Medio, 3 es el Derecho.
            if event.button == 1:
                # 'event.pos' es la posicion del Mouse cuando se dio el Click de tipo 1.
                cuadroPadreColumna1_Fila1 = cuadroPadre1.collidepoint(event.pos)
                cuadroPadreColumna2_Fila1 = cuadroPadre2.collidepoint(event.pos)
                cuadroPadreColumna3_Fila1 = cuadroPadre3.collidepoint(event.pos)
                cuadroPadreColumna4_Fila1 = cuadroPadre4.collidepoint(event.pos)
                cuadroPadreColumna5_Fila1 = cuadroPadre5.collidepoint(event.pos)
                cuadroPadreColumna6_Fila1 = cuadroPadre6.collidepoint(event.pos)
                cuadroPadreColumna7_Fila1 = cuadroPadre7.collidepoint(event.pos)

                cuadroPadreColumna1_Fila2 = cuadroPadre8.collidepoint(event.pos)
                cuadroPadreColumna2_Fila2 = cuadroPadre9.collidepoint(event.pos)
                cuadroPadreColumna3_Fila2 = cuadroPadre10.collidepoint(event.pos)
                cuadroPadreColumna4_Fila2 = cuadroPadre11.collidepoint(event.pos)
                cuadroPadreColumna5_Fila2 = cuadroPadre12.collidepoint(event.pos)
                cuadroPadreColumna6_Fila2 = cuadroPadre13.collidepoint(event.pos)
                cuadroPadreColumna7_Fila2 = cuadroPadre14.collidepoint(event.pos)

                cuadroPadreColumna1_Fila3 = cuadroPadre15.collidepoint(event.pos)
                cuadroPadreColumna2_Fila3 = cuadroPadre16.collidepoint(event.pos)
                cuadroPadreColumna3_Fila3 = cuadroPadre17.collidepoint(event.pos)
                cuadroPadreColumna4_Fila3 = cuadroPadre18.collidepoint(event.pos)
                cuadroPadreColumna5_Fila3 = cuadroPadre19.collidepoint(event.pos)
                cuadroPadreColumna6_Fila3 = cuadroPadre20.collidepoint(event.pos)
                cuadroPadreColumna7_Fila3 = cuadroPadre21.collidepoint(event.pos)

                cuadroPadreColumna1_Fila4 = cuadroPadre22.collidepoint(event.pos)
                cuadroPadreColumna2_Fila4 = cuadroPadre23.collidepoint(event.pos)
                cuadroPadreColumna3_Fila4 = cuadroPadre24.collidepoint(event.pos)
                cuadroPadreColumna4_Fila4 = cuadroPadre25.collidepoint(event.pos)
                cuadroPadreColumna5_Fila4 = cuadroPadre26.collidepoint(event.pos)
                cuadroPadreColumna6_Fila4 = cuadroPadre27.collidepoint(event.pos)
                cuadroPadreColumna7_Fila4 = cuadroPadre28.collidepoint(event.pos)

                cuadroPadreColumna1_Fila5 = cuadroPadre29.collidepoint(event.pos)
                cuadroPadreColumna2_Fila5 = cuadroPadre30.collidepoint(event.pos)
                cuadroPadreColumna3_Fila5 = cuadroPadre31.collidepoint(event.pos)
                cuadroPadreColumna4_Fila5 = cuadroPadre32.collidepoint(event.pos)
                cuadroPadreColumna5_Fila5 = cuadroPadre33.collidepoint(event.pos)
                cuadroPadreColumna6_Fila5 = cuadroPadre34.collidepoint(event.pos)
                cuadroPadreColumna7_Fila5 = cuadroPadre35.collidepoint(event.pos)

                cuadroPadreColumna1_Fila6 = cuadroPadre36.collidepoint(event.pos)
                cuadroPadreColumna2_Fila6 = cuadroPadre37.collidepoint(event.pos)
                cuadroPadreColumna3_Fila6 = cuadroPadre38.collidepoint(event.pos)
                cuadroPadreColumna4_Fila6 = cuadroPadre39.collidepoint(event.pos)
                cuadroPadreColumna5_Fila6 = cuadroPadre40.collidepoint(event.pos)
                cuadroPadreColumna6_Fila6 = cuadroPadre41.collidepoint(event.pos)
                cuadroPadreColumna7_Fila6 = cuadroPadre42.collidepoint(event.pos)

                cuadroPadre_LimpiarPantalla_Fila7 = cuadroPadre43.collidepoint(event.pos)

                if cuadroPadreColumna1_Fila1 or cuadroPadreColumna1_Fila2 or cuadroPadreColumna1_Fila3 or cuadroPadreColumna1_Fila4 or cuadroPadreColumna1_Fila5 or cuadroPadreColumna1_Fila6:
                    if columna_circulos_hijo["columna_1"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_1"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_1"]["filas"][fila][1]
                                columna_circulos_hijo["columna_1"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_1"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_1"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna2_Fila1 or cuadroPadreColumna2_Fila2 or cuadroPadreColumna2_Fila3 or cuadroPadreColumna2_Fila4 or cuadroPadreColumna2_Fila5 or cuadroPadreColumna2_Fila6:
                    if columna_circulos_hijo["columna_2"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_2"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_2"]["filas"][fila][1]
                                columna_circulos_hijo["columna_2"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_2"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_2"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna3_Fila1 or cuadroPadreColumna3_Fila2 or cuadroPadreColumna3_Fila3 or cuadroPadreColumna3_Fila4 or cuadroPadreColumna3_Fila5 or cuadroPadreColumna3_Fila6:
                    if columna_circulos_hijo["columna_3"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_3"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_3"]["filas"][fila][1]
                                columna_circulos_hijo["columna_3"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_3"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_3"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna4_Fila1 or cuadroPadreColumna4_Fila2 or cuadroPadreColumna4_Fila3 or cuadroPadreColumna4_Fila4 or cuadroPadreColumna4_Fila5 or cuadroPadreColumna4_Fila6:
                    if columna_circulos_hijo["columna_4"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_4"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_4"]["filas"][fila][1]
                                columna_circulos_hijo["columna_4"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_4"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_4"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna5_Fila1 or cuadroPadreColumna5_Fila2 or cuadroPadreColumna5_Fila3 or cuadroPadreColumna5_Fila4 or cuadroPadreColumna5_Fila5 or cuadroPadreColumna5_Fila6:
                    if columna_circulos_hijo["columna_5"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_5"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_5"]["filas"][fila][1]
                                columna_circulos_hijo["columna_5"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_5"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_5"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna6_Fila1 or cuadroPadreColumna6_Fila2 or cuadroPadreColumna6_Fila3 or cuadroPadreColumna6_Fila4 or cuadroPadreColumna6_Fila5 or cuadroPadreColumna6_Fila6:
                    if columna_circulos_hijo["columna_6"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_6"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_6"]["filas"][fila][1]
                                columna_circulos_hijo["columna_6"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_6"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_6"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadreColumna7_Fila1 or cuadroPadreColumna7_Fila2 or cuadroPadreColumna7_Fila3 or cuadroPadreColumna7_Fila4 or cuadroPadreColumna7_Fila5 or cuadroPadreColumna7_Fila6:
                    if columna_circulos_hijo["columna_7"]["completo"] == False:
                        # RELLENAR EL CIRCULO HIJO DE LA ULTIMA FILA SIN CIRCULO A RELLENAR DE  ESA COLUMNA
                        for fila in range(6, 0, -1):
                            if columna_circulos_hijo["columna_7"]["filas"][fila][0] == False:
                                id_hijo = columna_circulos_hijo["columna_7"]["filas"][fila][1]
                                columna_circulos_hijo["columna_7"]["filas"][fila][0] = True
                                if turno % 2 == 0:
                                    colores[id_hijo] = rojo
                                else:
                                    colores[id_hijo] = amarillo
                                if columna_circulos_hijo["columna_7"]["filas"][1][0] == True:
                                    print("No me volvere a ejecutar mas")
                                    columna_circulos_hijo["columna_7"]["completo"] = True
                                break
                        turno = turno + 1
                elif cuadroPadre_LimpiarPantalla_Fila7:
                    for i in range(len(colores)):
                        colores[i] = gris
                    print(columna_circulos_hijo)
                    for columna in range(1, len(columna_circulos_hijo) + 1):
                        columna_str = str(columna)
                        columna_circulos_hijo["columna_" + columna_str]["completo"] = False
                        for fila in range(1, len(columna_circulos_hijo["columna_" + columna_str]["filas"]) + 1):
                            columna_circulos_hijo["columna_" + columna_str]["filas"][fila][0] = False
                    print(columna_circulos_hijo)
    # DIBUJA EN PANTALLA
    # DIBUJA LOS CUADROS PADRES
    # 1 FILA
    # pygame.draw.rect: Dibuja un rectanculo en pantalla. (Surface, color, Rect).
    # Rect: Almacena datos como el (X,Y,Width,Height)
    pygame.draw.rect(screen, gris, cuadroPadre1)
    pygame.draw.rect(screen, gris, cuadroPadre2)
    pygame.draw.rect(screen, gris, cuadroPadre3)
    pygame.draw.rect(screen, gris, cuadroPadre4)
    pygame.draw.rect(screen, gris, cuadroPadre5)
    pygame.draw.rect(screen, gris, cuadroPadre6)
    pygame.draw.rect(screen, gris, cuadroPadre7)
    # 2 FILA
    pygame.draw.rect(screen, gris, cuadroPadre8)
    pygame.draw.rect(screen, gris, cuadroPadre9)
    pygame.draw.rect(screen, gris, cuadroPadre10)
    pygame.draw.rect(screen, gris, cuadroPadre11)
    pygame.draw.rect(screen, gris, cuadroPadre12)
    pygame.draw.rect(screen, gris, cuadroPadre13)
    pygame.draw.rect(screen, gris, cuadroPadre14)
    # 3 FILA
    pygame.draw.rect(screen, gris, cuadroPadre15)
    pygame.draw.rect(screen, gris, cuadroPadre16)
    pygame.draw.rect(screen, gris, cuadroPadre17)
    pygame.draw.rect(screen, gris, cuadroPadre18)
    pygame.draw.rect(screen, gris, cuadroPadre19)
    pygame.draw.rect(screen, gris, cuadroPadre20)
    pygame.draw.rect(screen, gris, cuadroPadre21)
    # 4 FILA
    pygame.draw.rect(screen, gris, cuadroPadre22)
    pygame.draw.rect(screen, gris, cuadroPadre23)
    pygame.draw.rect(screen, gris, cuadroPadre24)
    pygame.draw.rect(screen, gris, cuadroPadre25)
    pygame.draw.rect(screen, gris, cuadroPadre26)
    pygame.draw.rect(screen, gris, cuadroPadre27)
    pygame.draw.rect(screen, gris, cuadroPadre28)
    # 5 FILA
    pygame.draw.rect(screen, gris, cuadroPadre29)
    pygame.draw.rect(screen, gris, cuadroPadre30)
    pygame.draw.rect(screen, gris, cuadroPadre31)
    pygame.draw.rect(screen, gris, cuadroPadre32)
    pygame.draw.rect(screen, gris, cuadroPadre33)
    pygame.draw.rect(screen, gris, cuadroPadre34)
    pygame.draw.rect(screen, gris, cuadroPadre35)
    # 6 FILA
    pygame.draw.rect(screen, gris, cuadroPadre36)
    pygame.draw.rect(screen, gris, cuadroPadre37)
    pygame.draw.rect(screen, gris, cuadroPadre38)
    pygame.draw.rect(screen, gris, cuadroPadre39)
    pygame.draw.rect(screen, gris, cuadroPadre40)
    pygame.draw.rect(screen, gris, cuadroPadre41)
    pygame.draw.rect(screen, gris, cuadroPadre42)
    # 7 FILA
    pygame.draw.rect(screen, negro, cuadroPadre43)
    # DIBUJA LOS CIRCULOS HIJOS    
    # 1 FILA
    # pygame.draw.circle: Dibuja un circulo en pantalla. (Surface, color, posicionCentro, radio).
    pygame.draw.circle(screen, colores[1], posicionHijo(posicionPadreCuadro), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[2], posicionHijo(posicionPadreCuadro2), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[3], posicionHijo(posicionPadreCuadro3), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[4], posicionHijo(posicionPadreCuadro4), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[5], posicionHijo(posicionPadreCuadro5), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[6], posicionHijo(posicionPadreCuadro6), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[7], posicionHijo(posicionPadreCuadro7), radio_relleno[0], radio_relleno[1])
    # 2 FILA
    pygame.draw.circle(screen, colores[8], posicionHijo(posicionPadreCuadro8), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[9], posicionHijo(posicionPadreCuadro9), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[10], posicionHijo(posicionPadreCuadro10), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[11], posicionHijo(posicionPadreCuadro11), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[12], posicionHijo(posicionPadreCuadro12), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[13], posicionHijo(posicionPadreCuadro13), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[14], posicionHijo(posicionPadreCuadro14), radio_relleno[0], radio_relleno[1])
    # 3 FILA
    pygame.draw.circle(screen, colores[15], posicionHijo(posicionPadreCuadro15), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[16], posicionHijo(posicionPadreCuadro16), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[17], posicionHijo(posicionPadreCuadro17), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[18], posicionHijo(posicionPadreCuadro18), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[19], posicionHijo(posicionPadreCuadro19), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[20], posicionHijo(posicionPadreCuadro20), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[21], posicionHijo(posicionPadreCuadro21), radio_relleno[0], radio_relleno[1])
    # 4 FILA
    pygame.draw.circle(screen, colores[22], posicionHijo(posicionPadreCuadro22), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[23], posicionHijo(posicionPadreCuadro23), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[24], posicionHijo(posicionPadreCuadro24), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[25], posicionHijo(posicionPadreCuadro25), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[26], posicionHijo(posicionPadreCuadro26), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[27], posicionHijo(posicionPadreCuadro27), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[28], posicionHijo(posicionPadreCuadro28), radio_relleno[0], radio_relleno[1])
    # 5 FILA
    pygame.draw.circle(screen, colores[29], posicionHijo(posicionPadreCuadro29), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[30], posicionHijo(posicionPadreCuadro30), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[31], posicionHijo(posicionPadreCuadro31), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[32], posicionHijo(posicionPadreCuadro32), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[33], posicionHijo(posicionPadreCuadro33), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[34], posicionHijo(posicionPadreCuadro34), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[35], posicionHijo(posicionPadreCuadro35), radio_relleno[0], radio_relleno[1])
    # 6 FILA
    pygame.draw.circle(screen, colores[36], posicionHijo(posicionPadreCuadro36), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[37], posicionHijo(posicionPadreCuadro37), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[38], posicionHijo(posicionPadreCuadro38), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[39], posicionHijo(posicionPadreCuadro39), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[40], posicionHijo(posicionPadreCuadro40), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[41], posicionHijo(posicionPadreCuadro41), radio_relleno[0], radio_relleno[1])
    pygame.draw.circle(screen, colores[42], posicionHijo(posicionPadreCuadro42), radio_relleno[0], radio_relleno[1])
    # DIBUJA EL CUADRO HIJO CON TEXTO
    # blit: Dibuja un Objeto Surface en la Posicion del Objeto Rect.
    screen.blit(texto_del_cuadro_surface43, texto_del_cuadro_rect43)
    # SI SE GANA, QUIERO QUE ME MUESTRE UN ALERTA CON EL MENSAJE DE FELCITACIONES
    pygame.display.update()  # Es una funcion que permite que solo una parte de la pantalla se actualice en lugar de toda el area de la superficie. En esta ocacion, no pasamos ningun argumento, entonces actualizara toda la Area de la Superficie.
    if ganar(colores):
        cantidad_de_turnos = str(round(turno / 2))
        if turno % 2 == 1:
            ganador = "ROJO"
        else:
            ganador = "AMARILLO"
        messagebox.showinfo('Mensaje de Informacion',
                            'GANASTE JUGADOR ' + ganador + " EN " + cantidad_de_turnos + " TURNOS :D\nJuego desarrollado por: Juan Serrano.")
        for i in range(len(colores)):
            colores[i] = gris
        for columna in range(1, len(columna_circulos_hijo) + 1):
            columna_str = str(columna)
            columna_circulos_hijo["columna_" + columna_str]["completo"] = False
            for fila in range(1, len(columna_circulos_hijo["columna_" + columna_str]["filas"]) + 1):
                columna_circulos_hijo["columna_" + columna_str]["filas"][fila][0] = False
        turno = 0
