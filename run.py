from Algoritmos.Busquedas import bfs, dfs, primero_ambicioso
from Entidades.Laberinto import Laberinto
from Entidades.Agente import Agente
from random import randint

def genera_coor(renglon, columna):
    return (randint(0, renglon-1), randint(0, columna-1))

if __name__ == '__main__':
    matrix = Laberinto(20,20)
    smith = Agente(matrix)
    smith.set_inicio( genera_coor(20,20) )
    smith.set_meta( genera_coor(20,20) )
    a = bfs(matrix, smith)
    # ---------------------
    matrix2 = Laberinto(20,20)
    smith2 = Agente(matrix2)
    smith2.set_inicio( genera_coor(20,20) )
    smith2.set_meta( genera_coor(20,20) )
    b = dfs(matrix2, smith2)
    # ---------------------
    matrix3 = Laberinto(20,20)
    smith3 = Agente(matrix3)
    smith3.set_inicio( genera_coor(20,20) )
    smith3.set_meta( genera_coor(20,20) )
    c = primero_ambicioso(matrix3, smith3)
    # ---------------------
    print(f"bfs: {a}, dfs: {b}, Ambicioso: {c}")
