#EJERCICIO 1

for i in range (1, 101):
    print(i)


#---------------------------------------------------------------------------------------

#EJERCICIO 2

#Solicitar al usuario que ingrese un número entero, usamos el entero de ese numero e inicializamos digitos
numero = int(input("Ingrese un número: "))
numero = abs(numero)
digitos = 0

#Dividimos el numero entre 10 hasta que sea 0, incrementando digitos en cada iteracion
while numero > 0:
    numero //= 10
    digitos += 1
print(f"El número tiene {digitos} dígitos.")

#---------------------------------------------------------------------------------------

#EJERCICIO 3

#Solicitar al usuario que ingrese dos números enteros
numero1 = int(input("Ingrese un número entero: "))
numero2 = int(input("Ingrese otro número entero: "))
suma = 0

#Determinar el rango entre los dos números y sumar los números en ese rango
inicio = min(numero1, numero2) + 1
final = max(numero1, numero2)

#Usamos un bucle for para sumar los números en el rango
for i in range(inicio, final):
    suma += i
print(f"La suma de los números entre {numero1} y {numero2} es: {suma}")


#---------------------------------------------------------------------------------------

#EJERCICIO 4

#Solicitamos al usuario que ingrese un número entero e inicializamos suma
numero = int(input("Ingrese un número: "))
suma = 0

#Utilizamos un bucle while para sumar los números hasta que el usuario ingrese 0
while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número: "))
print("La suma total es:", suma)


#---------------------------------------------------------------------------------------

#EJERCICIO 5

#Solicitamos al usuario que adivine un número entre 0 y 9
numero = int(input("Adivina el número entre 0 y 9: "))

#Establecemos el número correcto y un contador de intentos
numeroCorrecto = 5
suma = 0

#Usamos un bucle while para permitir al usuario intentar adivinar el número hasta que lo consiga y contamos los intentos
while numero != numeroCorrecto:
    print("Número incorrecto, intenta de nuevo.")
    numero = int(input("Adivina el número entre 0 y 9: "))
    suma += 1
print(f"¡Felicidades! Has adivinado el número {numeroCorrecto} en {suma} intentos.")


#---------------------------------------------------------------------------------------

#EJERCICIO 6

#Imprimir números pares del 100 al 2 en orden descendente
for i in range(100, 0, -2):
    print(i)


#--------------------------------------------------------------------------------------

#EJERCICIO 7

#Solicitar al usuario que ingrese un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))
suma = 0

#Utilizar un bucle for para sumar los números desde 0 hasta el número ingresado
for i in range(numero + 1):
    suma += i
print(f"La suma de los números desde 0 hasta {numero} es: {suma}")


#---------------------------------------------------------------------------------------

#EJERCICIO 8

#Inicializamos contadores y definimos la cantidad de números a procesar
numeros = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

#Usamos un bucle for para procesar cada número ingresado por el usuario
for i in range(numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    if numero % 2 != 0:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


#---------------------------------------------------------------------------------------

#EJERCICIO 9

#Calculo de la media de 100 numeros ingresados por el usuario, inicializamos suma y media
numeros = 100
suma = 0
media = 0

#Usamos un bucle for para sumar los números y calcular la media
for i in range(numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero
    media = suma / numeros
print(f"La media de estos numeros es: {media}")


#---------------------------------------------------------------------------------------

#EJERCICIO 10

#Solicitamos al usuario que ingrese un número entero y inicializamos numero_invertido
numero = int(input("Ingrese un número: "))
numero_invertido = 0

#En un bucle while, extraemos cada dígito del número y construimos el número invertido
while numero > 0:
    digito = numero % 10            
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10           

print("El número invertido es:", numero_invertido)
