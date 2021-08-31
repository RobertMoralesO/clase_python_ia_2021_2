#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 18:50:09 2021

@author: robertomorales
"""

print('Hello world')

# Variables
a = 3
print(type(a))
a = "Hola"
print(type(a))
a = 3.5
print(type(a))
a = True
print(type(a))

# Operaciones

# Suma

a = 5
b = 2
c = a + b
print(c)

# Resta

a = 5
b = 2
c = a - b
print(c)

# Multiplicación

a = 5
b = 2
c = a * b
print(c)

# División

a = 5
b = 2
c = a / b
print(c)


a = 5
b = 2
c = a // b
print(c)

# Potencia

a = 5
b = 2
c = a ** b
print(c)

# Raiz

a = 27
c = a ** (1/3)
print(c)

# import math
# raiz = math.sqrt(25)
# print(raiz)

# Tipos de datos

# String str
a = "Hola Mundo"
a = 'Hola Mundo'
b = "I can't do it"
c = 'Alias "Roberto"'

# Entero int
a = 5

# Decimal float
a = 5.6

# Booleano bool
x = True
y = False

# Conversiones entre tipos de datos

# Convertir de x a entero

a = '3'
y = int(a)
print(y)
print(type(y))

# Convertir de x a decimal

a = '3'
y = float(a)
print(y)
print(type(y))

# Convertir de x a string

a = 3
y = str(a)
print(y)
print(type(y))

# Concatenaciones

a = 'hola'
b = 'mundo'
c = a + ' ' + b

a = 'hola'
b = a * 5


# Capturar por pantalla

nombre = input('Digite su nombre: ')
print('Hola', nombre)


print('Digite su nombre: ')
nombre = input()
print('Hola', nombre)


# HUA que sume dos números e imprima su resultado

numero_uno = float(input('Digite el número uno: '))
numero_dos = float(input('Digite el número dos: '))
suma = numero_uno + numero_dos
# print(suma)
# print('La suma es: ', suma)
print(f'La suma de los número {numero_uno} + {numero_dos} es {suma}')

# HUA que lea un número y lo eleve al cuadrado
base = int(input('Digite la base a elevar: '))
potencia = base ** 2
print(f'El resultado de elevar {base} al cuadrado es: {potencia}')

# HUA que tome el valor de un producto, le aplique el 20%
# de descuento, imprima el valor del producto inicial,
# el valor con descuento y el valor ahorrado

vproducto = float(input('Digite el valor del producto: $'))
descuento = vproducto * 0.20
vfinal = vproducto - descuento
print(f'El valor inicial del producto es: ${vproducto:,}')
print(f'El valor del descuento es: ${descuento:,}')
print(f'El valor final del producto es: ${vfinal:,}')



















