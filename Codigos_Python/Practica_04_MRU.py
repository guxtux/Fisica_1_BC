# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:47:25 2023

@author: gusto
"""

import numpy as np
import matplotlib.pyplot as plt

def velocidad(d, t):
    v = d/t
    return v

d = [0, 20, 50, 100, 200, 300, 350, 400]

c1 = [0.0, 1.8, 5.8, 12.0, 25.0, 39.0, 45.0, 51.0]
c2 = [0.0, 2.6, 6.5, 13.0, 26.0, 39.0, 45.0, 52.0]
c3 = [0.0, 2.0, 6.0, 12.0, 24.0, 36.0, 42.0, 48.8]

v1 = [0., ]
v2 = [0., ]
v3 = [0., ]

for i in range(1,len(d)):
    v1.append(velocidad(d[i], c1[i]))
    v2.append(velocidad(d[i], c2[i]))
    v3.append(velocidad(d[i], c3[i]))

print(v1)

plt.figure(1)
plt.plot(c1, v1, 'r--', lw=0.7, marker='o', label='Corredora 1')
plt.plot(c2, v2, 'b--', lw=0.7, marker='+', label='Corredora 2')
plt.plot(c3, v3, 'm--', lw=0.7, marker='^', label='Corredora 3')
plt.legend(loc='lower right')
plt.xlabel('Tiempo [s]')
plt.ylabel('Velocidad [m/s]')
plt.title('Comparación de velocidad entre las corredoras')

plt.figure(2)
plt.plot(c1, d, 'r--', lw=0.7, marker='o', label='Corredora 1')
plt.plot(c2, d, 'b--', lw=0.7, marker='+', label='Corredora 2')
plt.plot(c3, d, 'm--', lw=0.7, marker='^', label='Corredora 3')
plt.legend(loc='lower right')
plt.xlabel('Tiempo [s]')
plt.ylabel('Desplazamiento [m]')
plt.title('Comparación de desplazamiento entre las corredoras')

plt.show()