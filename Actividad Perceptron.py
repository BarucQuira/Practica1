# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:44:06 2023

Baruc Gtz Q
Inteligencia Artificial 
Parcial 2

@author: Usuario
"""


import numpy as np

W=np.array([1,1,1])
X=np.array([[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]])
Y=np.array([-1,-1,-1,1])
a=0.5
n=0
epoca=1

print(W)
while(epoca!=0):
    Yg=np.sign(np.dot(np.transpose(W),X[n,:]))
    if Yg==0:
        Yg=1
    W=W+a*(-Yg+Y[n])*X[n,:]
    n=n+1
    if n==3:
        epoca=epoca-1
        n=0
    print(W)
    
print("\nResultados:")
for i in range(4):
    print(np.sign(np.dot(np.transpose(W),X[i,:])))
    
print("\nEntonces con los valores anteriores obtenidos podemos clasificarlas de manera mas visual:\n")

print("\nTabla de verdad de dos entradas de compuerta 'AND': \n")
print("| 0 | 0 | = ", np.sign(np.dot(np.transpose(W),X[0,:])) >= 0,"-->",np.sign(np.dot(np.transpose(W),X[0,:])))
print("| 0 | 1 | = ", np.sign(np.dot(np.transpose(W),X[1,:])) >= 0,"-->",np.sign(np.dot(np.transpose(W),X[1,:])))
print("| 1 | 0 | = ", np.sign(np.dot(np.transpose(W),X[2,:])) >= 0,"-->",np.sign(np.dot(np.transpose(W),X[2,:])))
print("| 1 | 1 | = ", np.sign(np.dot(np.transpose(W),X[3,:])) >= 0," --> ",np.sign(np.dot(np.transpose(W),X[3,:])))