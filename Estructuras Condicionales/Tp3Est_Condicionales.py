#EJERCICIO1

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Verificar si es mayor de edad
if edad >= 18:
    print("Usted es mayor de edad.")


#----------------------------------------------------------------------------------------------
#EJERCICIO2

# Solicitar al usuario que ingrese una nota
nota = float(input("Ingrese su nota (0-10): "))

# Verificar si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#----------------------------------------------------------------------------------------------
#EJERCICIO3

# Solicitar al usuario que ingrese un número entero
par = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar
if par % 2 == 0:
    print("El número es par.")
else:
    print("Por favor, ingrese un número par.")


#----------------------------------------------------------------------------------------------
#EJERCICIO4

# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Verificar a que categoria pertenece
if edad < 12:
    print("Usted es un niño.")
elif 12 <= edad < 18:
    print("Usted es un adolescente.")
elif 18 <= edad < 30: 
    print("Usted es un Adulto/a joven.")
else:
    print("Usted es un adulto.")


#----------------------------------------------------------------------------------------------
#EJERCICIO5

# Solicitar al usuario que ingrese una contraseña
contraseña = input("Ingrese la contraseña (8 a 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una constraseña correcta.")
else:
    contraseña = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#----------------------------------------------------------------------------------------------
#EJERCICIO6

import random 
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar los resultados
print("Lista de numeros", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determinar el sesgo de la distribución
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif moda < mediana < media:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución es simétrica.")
else:
    print("La distribución no cumple con los criterios para determinar el sesgo.")


#----------------------------------------------------------------------------------------------
#EJERCICIO7

# Solicitar al usuario que ingrese una frase o palabra
frase = input("Ingrese una frase o palabra: ")

# Obtener la última letra de la frase
ultimaLetra = frase[-1]

# Verificar si la última letra es una vocal
if ultimaLetra.lower() in 'aeiou':
    print(frase + "!")
else:
    print(frase)


#----------------------------------------------------------------------------------------------
#EJERCICIO8

# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Solicitar al usuario que ingres los numeros 1, 2 o 3
numero = int(input("Ingrese un número (1, 2 o 3): "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Número inválido. Por favor, ingrese 1, 2 o 3.")


#----------------------------------------------------------------------------------------------
#EJERCICIO9

# Solicitar la magnitud de un terremoto
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

# Determinar la categoría del terremoto
if magnitud < 3:
    print("El terremoto es de categoría: Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("El terremoto es de categoría: Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("El terremoto es de categoría: Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("El terremoto es de categoría: Fuerte  (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("El terremoto es de categoría: Mayor  (puede causar daños significativos).")
elif 7 <= magnitud:
    print("El terremoto es de categoría: Extremo  (puede causar graves daños a gran escala).")

#----------------------------------------------------------------------------------------------
#EJERCICIO10

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().lower()
mes = input("¿Qué mes es? (en letras, por ejemplo: marzo): ").strip().lower()
dia = int(input("¿Qué día es? (en número): "))

# Diccionario para convertir meses a números
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

mes_num = meses.get(mes, 0)

if mes_num == 0:
    print("Mes inválido.")
else:
    # Convertir fecha a formato (mes, día) para comparar fácilmente
    fecha = (mes_num, dia)

    # Definir rangos de fechas para cada estación
    if hemisferio == "n" or hemisferio == "norte":
        if (fecha >= (12, 21) or fecha <= (3, 20)):
            estacion = "invierno"
        elif (fecha >= (3, 21) and fecha <= (6, 20)):
            estacion = "primavera"
        elif (fecha >= (6, 21) and fecha <= (9, 20)):
            estacion = "verano"
        elif (fecha >= (9, 21) and fecha <= (12, 20)):
            estacion = "otoño"
        else:
            estacion = "Fecha inválida"
    elif hemisferio == "s" or hemisferio == "sur":
        if (fecha >= (12, 21) or fecha <= (3, 20)):
            estacion = "verano"
        elif (fecha >= (3, 21) and fecha <= (6, 20)):
            estacion = "otoño"
        elif (fecha >= (6, 21) and fecha <= (9, 20)):
            estacion = "invierno"
        elif (fecha >= (9, 21) and fecha <= (12, 20)):
            estacion = "primavera"
        else:
            estacion = "Fecha inválida"
    else:
        estacion = "Hemisferio inválido"
    print(f"En el hemisferio {hemisferio.upper()}, el {dia} de {mes} es {estacion}.")


#----------------------------------------------------------------------------------------------