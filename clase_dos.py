#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:02:43 2021

@author: robertomorales
"""
# Condicionales

# Tabla de Verdad

# Tabla del and
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabla del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negación

print(not True)  # False
print(not False)  # True

# Mas de dos condiciones al mismo tiempo

print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True

# Jerarquía de operaciones
# 1. Paréntesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquía de operaciones booleanas
# 1. Paréntesis y llaves
# 2. Tabla de verdad

# Estructura if
x = -1
if(x > 0):
    print('1')
else:
    print('2')
    print('3')


# HUA que dada la edad de una persona indique si es mayor
# o menor de edad

edad = int(input('Digite su edad: '))
if(edad >= 18):
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad')

# HUA que indique si un estudiante aprobó o reprobó una
# asignatura teniendo en cuenta que aprueba con mínimo
# una calificación de 3.0 hasta 5.0. El rango válido de una nota es
# entre 0 y 5.

nota_final = float(input('Digite la nota final: '))
if(nota_final >= 3.0 and nota_final <= 5.0):
    print('Usted aprobó la asignatura')
elif(nota_final < 3.0 and nota_final > 0):
    print('Usted reprobó la asignatura')
else:
    print('La nota ingresada no es válida')

# HUA que dado un número n diga si es negativo, positivo o
# cero.

n = float(input('Digite el número: '))
if (n > 0):
    print(f'El número {n} es positivo')
elif (n < 0):
    print(f'El número {n} es negativo')
else:
    print(f'El número es cero')


# Ciclos
    
# Ciclo for
    
for valor in range(11):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 11, 2):
    print(valor)

for valor in range(11):
    print(valor)
    print(valor + 1)

# HUA que de las n notas de un estudiante  y calcule el promedio
# académico final


num = int(input('Digite número de notas cursadas: '))
if(num > 0):
    acumulador = 0
    for x in range(num):
        nota = float(input(f'Digite la nota {x + 1}: '))
        acumulador = acumulador + nota
    promedio = acumulador / num
    promedio = round(promedio, 2)
    print(f'El promedio final es: {promedio}')
else:
    print('El número de notas no puede ser menor o igual a cero')
    



