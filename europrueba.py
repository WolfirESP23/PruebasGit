# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:54:53 2021

@author: JorgeRomeroBurdalo
"""

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

print(f"{numeros[1]} - {numeros[11]} - {numeros[21]} - {numeros[31]} - {numeros[41]}")
print(f"{numeros[2]} - {numeros[12]} - {numeros[22]} - {numeros[32]} - {numeros[42]}")  
print(f"{numeros[3]} - {numeros[13]} - {numeros[23]} - {numeros[33]} - {numeros[43]}")
print(f"{numeros[4]} - {numeros[14]} - {numeros[24]} - {numeros[34]} - {numeros[44]}")  
print(f"{numeros[5]} - {numeros[15]} - {numeros[25]} - {numeros[35]} - {numeros[45]}")  
print(f"{numeros[6]} - {numeros[16]} - {numeros[26]} - {numeros[36]} - {numeros[46]}")  
print(f"{numeros[7]} - {numeros[17]} - {numeros[27]} - {numeros[37]} - {numeros[47]}")  
print(f"{numeros[8]} - {numeros[18]} - {numeros[28]} - {numeros[38]} - {numeros[48]}")  
print(f"{numeros[9]} - {numeros[19]} - {numeros[29]} - {numeros[39]} - {numeros[49]}")

for numero in range(5):
  n1=int(input("Introduce el número: "))
  numeros[0+n1-1]= "X"
  print(f"{numeros[0]} - {numeros[10]} - {numeros[20]} - {numeros[30]} - {numeros[40]}")
  print(f"{numeros[1]} - {numeros[11]} - {numeros[21]} - {numeros[31]} - {numeros[41]}")
  print(f"{numeros[2]} - {numeros[12]} - {numeros[22]} - {numeros[32]} - {numeros[42]}")  
  print(f"{numeros[3]} - {numeros[13]} - {numeros[23]} - {numeros[33]} - {numeros[43]}")
  print(f"{numeros[4]} - {numeros[14]} - {numeros[24]} - {numeros[34]} - {numeros[44]}")  
  print(f"{numeros[5]} - {numeros[15]} - {numeros[25]} - {numeros[35]} - {numeros[45]}")  
  print(f"{numeros[6]} - {numeros[16]} - {numeros[26]} - {numeros[36]} - {numeros[46]}")  
  print(f"{numeros[7]} - {numeros[17]} - {numeros[27]} - {numeros[37]} - {numeros[47]}")  
  print(f"{numeros[8]} - {numeros[18]} - {numeros[28]} - {numeros[38]} - {numeros[48]}")  
  print(f"{numeros[9]} - {numeros[19]} - {numeros[29]} - {numeros[39]} - {numeros[49]}") 