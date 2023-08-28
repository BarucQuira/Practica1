# -*- coding: utf-8 -*-
"""
Created on Tue May  9 00:08:27 2023

Baruc Gtz Q - 20310368
IA 2do parcial

@author: DELL
"""

#Se importan la librerias a utilizar 
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing


########### PREPARAR LA DATA ##########

#Importamos los datos de la misma librería de scikit-learn 
boston = fetch_california_housing()
print (boston) 
print()

########## ENTENDIMIENTO DE LA DATA ##

#Verifico la información contenida en el dataset 
print('Información en el dataset:') 
print(boston.keys())
print()

#Verifico las caracteristicas del dataset 
print('Características del dataset:')
print(boston.DESCR)

#Verifico la cantidad de datos que hay en los dataset 
print('Cantidad de datos:')
print(boston.data.shape) 
print()

#Verifico la información de las columnas

print('Nombres columnas:')
print (boston.feature_names)


########## PREPARAR LA DATA REGRESIÓN LINEAL MULTIPLE #####

#Seleccionamos las columna 5, 6 y 7 del dataset 
X_multiple = boston.data[:, 5:8] 
print(X_multiple)

#Defino los datos correspondientes a las etiquetas 
y_multiple = boston.target

############ IMPLEMENTACIÓN DE REGRESIÓN LINEAL MULTIPLE ######

from sklearn.model_selection import train_test_split

#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos 
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)

#Defino el algoritmo a utilizar

lr_multiple = linear_model.LinearRegression() 

#Entreno el modelo 
lr_multiple.fit(X_train, y_train)

#Realizo una predicción
Y_pred_multiple = lr_multiple.predict(X_test)
print('DATOS DEL MODELO REGRESION LINEAL MULTIPLE')
print() 

print("Valor de las pendientes o coeficientes 'a':")
print(lr_multiple.coef_)

print("Valor de la intersección o coeficiente 'b':")
print(lr_multiple.intercept_)

print("Precisión del modelo:")
print(lr_multiple.score(X_train,y_train))