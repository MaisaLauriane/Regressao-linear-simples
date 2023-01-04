# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:10:13 2023

@author: Maisa
"""

import random
import matplotlib.pyplot as plt

def make_list(num): 
  x = [] 
  y = [] 
  #cria lista com tamanho n de numeros aleatorios 
  for i in range(num): 
    num_random = random.randint(1, 50) 
    num_random2 = random.randint(1, 50) 
    x.append(num_random) 
    y.append(num_random2)

  return x,y

def make_mean(x): 
  somatorio= sum(x) 
  tamanho=len(x) 
  mean= somatorio/tamanho 
  return mean

def linear_regression(X,Y,m_x,m_y):
  n=len(X)
  S_xy = 0
  S_xx = 0
  for i in range(n):
      S_xy += (X[i] - m_x)*(Y[i] - m_y)
      S_xx += (X[i] - m_x)**2
        
    # Calcular os coeficientes
  cof_b1 = S_xy / S_xx
  cof_b0 = m_y - cof_b1*m_x
  return cof_b0,cof_b1

#if name == "main": 
num=8 
  #faz a lista com x e y 
X,Y= make_list(num) 
X = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 
Y = [-1., 2.5, 2., 4.5, 5., 6.5, 8., 8.5, 11., 10.5, 14., 12.5, 17., 14.5, 20., 16.5, 23., 18.5, 26., 20.5]

#X = [8, 9, 10, 3, 17, 19, 4, 8, 16, 10]
#Y = [14, 1, 16, 15, 15, 11, 18, 20, 15, 10]
#calculo da média
x_m= make_mean(X) 
y_m= make_mean(Y)

#calculando regressão 
Coef_B0, Coef_B1= linear_regression(X,Y,x_m,y_m) 
print('O coeficiente B1: ',Coef_B1,' | O coeficiente B0: ', Coef_B0)

y_pred1 = []

for x1 in X:
    y_pred = Coef_B0 + Coef_B1*x1
    y_pred1.append(y_pred)

plt.figure(figsize=(8,8))
plt.scatter(X, Y, color = "b", marker = "o", s = 50) 
plt.plot(X, y_pred1, color = "r") 
plt.title('Distribuição + Regressão Linear')
plt.xlabel('x', fontsize = 12) 
plt.ylabel('y', fontsize = 12) 
plt.show() 
