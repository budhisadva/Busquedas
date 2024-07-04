from Estructuras.Lineales.ColaPrioridades import ColaPrioridades
from Estructuras.Lineales.Cola import Cola
from Estructuras.Lineales.Pila import Pila
from .Heuristicas import euclidiana
from random import sample
from time import sleep

def bfs(laberinto, agente):
    visitados = [agente.s0]
    cola = Cola()
    cola.queue(agente.s0)
    i=0
    while not cola.empty() and agente.actual != agente.F:
        actual = cola.dequeue()
        agente.actual = actual
        for accion in agente.A:
            vecino = agente.T(actual,accion)
            if vecino is not None and vecino not in visitados:
                cola.queue(vecino)
                visitados.append(vecino)
        laberinto.actualiza(agente)
        print(laberinto, "\n")
        sleep(.05)
        i += 1
    return i

def dfs(laberinto, agente):
    visitados = [agente.s0]
    pila = Pila()
    pila.push(agente.s0)
    i=0
    while not pila.empty() and agente.actual != agente.F:
        actual = pila.pop()
        agente.actual = actual
        for accion in agente.A:
            vecino = agente.T(actual,accion)
            if vecino is not None and vecino not in visitados:
                pila.push(vecino)
                visitados.append(vecino)
        laberinto.actualiza(agente)
        print(laberinto, "\n")
        sleep(.05)
        i +=1
    return i

def primero_ambicioso(laberinto, agente):
    visitados = []
    frontera = ColaPrioridades()
    frontera.queue({"actual":agente.s0, "meta":agente.F}, euclidiana)
    i=0
    while not frontera.empty() and agente.actual != agente.F:
        actual = frontera.dequeue()
        visitados.append(actual[0])
        agente.actual = actual[0]
        for accion in agente.A:
            vecino = agente.T(actual[0],accion)
            if vecino is not None and vecino not in visitados:
                frontera.queue({"actual":vecino, "meta":agente.F}, euclidiana)
        laberinto.actualiza(agente)
        print(laberinto, "\n")
        sleep(.1)
        i+=1
    return i
