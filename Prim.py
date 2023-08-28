# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Inteligencia Artificial

Parcial I

Código Prim

Baruc Gutiérrez Quirarte - 6F

"""

def prim(w,n,s):
    v=[]
    while(len(v) != n):
        v.append(0)
    v[s]=1
    E = []
    suma = 0
    for i in range(0,n-1):
        minimo = 9
        agregar_vertice = 0
        e = []
        for j in range(0,n):
            if(v[j] == 1):
                for k in range(0,n):
                    if(v[k] == 0 and w[j][k] < minimo):
                        agregar_vertice = k
                        e = [j,k]
                        minimo = w[j][k]
        suma += w[e[0]][e[1]]
        v[agregar_vertice] = 1
        E.append(e)
    return [E,suma]


n = 6
s = 0

""" Dado que en la figura se muestran 6 vertices, algunos unidos entre ellos,
    cada uno con un peso entre las aristas se hace una matriz de 6x6,
    donde las intersecciones pueden tener peso si estas aristas existen 
    o poner un valor de 9 si estos no tienen interseccion"""
    
w = [
      [9,4,2,9,3,9],#1
      [4,9,9,5,9,9],#2
      [2,9,9,1,6,3],#3
      [9,5,1,9,9,6],#4
      [3,9,6,9,9,2],#5
      [9,9,3,6,2,9]#6
]
"""El texto que se imprime es un poco distinto a como se expresa en
   la figura, los vertices que se imprimen es uno menos al de la
   figura, es decir, en lugar de comenzar por el vertice 1 (como
   en la figura),se inicia por el vertice 0 representando al vertice 1"""
   
print(prim(w,n,s))
            
    
        
    
