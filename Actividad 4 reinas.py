# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:38:08 2023

Baruc Gutiérrez Quirarte - 6F 
Inteligencia Artificial

@author: DELL
"""
import numpy as np

cuadricula = np.zeros((4,4), dtype='int64')


def movlegal(fila,columna):
    for i in range(columna):
        if fila[i]==fila[columna] or fila[i]-fila[columna]==columna-i or fila[columna]-fila[i]==columna-i:
            return False
    return True

def cuatro_reinas(fila):
    k=0  
    n=len(fila)
   
    fila[k]=-1

    while k>-1:
        fila[k]+=1
        
        while(fila[k]<n) and not movlegal(fila,k):
            fila[k]+= 1
        if fila[k]<n:
            if k==n-1:
                return True
            else:
                k+=1  
                fila[k]=-1
        else:
            k-=1  
    return False  



fila = [0,0,0,0]
if cuatro_reinas(fila) == True:
        
    for i in range(4):
        for j in range (4):
            for x in range (4):
                if(x == i):
                    if(fila[x] == j):
                        cuadricula[i,j] = 1
            
    print("La fila resultante es:\n", fila)
    
    print("\nLos 1's en la cuadricula representan la posición de las reinas.")
    print("La cuadricula resultante es:\n", cuadricula)
   
else:
    print("No hay solución")