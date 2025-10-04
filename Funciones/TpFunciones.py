#EJERCICIO 1

# Definicion de funcion hola mundo

def imprimiendo_hola_mundo():
    print("Hola Mundo")

# Programa principal
imprimiendo_hola_mundo()

#----------------------------------------------------------------

#EJERCICIO 2

# Definicion de funcion de saludo personalizado
def saludo_personalizado(nombre):
    print("Hola " + nombre)

# Programa principal
nombre_usuario = input("Ingrese su nombre: ")
saludo_personalizado(nombre_usuario)

#----------------------------------------------------------------

#EJERCICIO 3

# Definicion de funcion de informacion personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#----------------------------------------------------------------

#EJERCICIO 4 

import math

# Definicion de funcion de area de circulo

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Definicion de funcion de perimetro de circulo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#----------------------------------------------------------------

#EJERCICIO 5

# Definicion de funcion de segundos a horas

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

# Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son {horas} hora/s.")

#----------------------------------------------------------------

#EJERCICIO 6

# Definicion funcion tabla de multiplicar

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#----------------------------------------------------------------

#EJERCICIO 7

# Tupla de dos numeros

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (division por cero)"
    return suma, resta, multiplicacion, division

# Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

#----------------------------------------------------------------

#EJERCICIO 8

# Calculo de ICM

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su Indice de Masa Corporal (IMC) es: {imc:.2f}")

#----------------------------------------------------------------

#EJERCICIO 9

# Calculo de Grados Celsius a Fahrenheit

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

#----------------------------------------------------------------

#EJERCICIO 10

# Calculo de promedio de 3 numeros

def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

# Programa principal

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

#----------------------------------------------------------------