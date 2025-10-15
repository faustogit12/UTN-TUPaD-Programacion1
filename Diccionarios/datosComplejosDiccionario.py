# EJERCICIO 1
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
} 

# Añadir frutas nuevas

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Diccionario actualizado
print(precios_frutas) 

#---------------------------------------------------------------

# EJERCICIO 2
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
} 

# Añadir frutas nuevas

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Nuevos precios de banana, manzana, melon

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

# Diccionario actualizado
print(precios_frutas) 

#---------------------------------------------------------------

# EJERCICIO 3

precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
} 

# Añadir frutas nuevas

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Nuevos precios de banana, manzana, melon

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

# Lista con solo las frutas
lista_frutas = list(precios_frutas.keys())

# Diccionario actualizado
print(precios_frutas) 

# Lista de frutas
print(lista_frutas)


#-------------------------------------------------------------------

# EJERCICIO 4

carga_contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el numero de telefono de {nombre}: ")
    carga_contactos[nombre] = numero

#Consultar contacto
consulta_contacto = input("Ingrese el numero del contacto que quiera consultar: ")

# Mostrar el numero si existe

if consulta_contacto in carga_contactos:
    print(f"El numero {consulta_contacto} es: {carga_contactos[consulta_contacto]}")
else:
    print("Ese contacto no esta en la agenda de contactos")

#-------------------------------------------------------------------

# EJERCICIO 5

# Pedir ingreso de frase

frase = input("Ingrese una frase: ")

# Separacion en palabras

palabras = frase.split()

# Palabras unicas

palabras_unicas = set(palabras)

# Recuento de veces que aparece cada palabra

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Resultados

print("Palabras unicas: ", palabras_unicas)
print("Recuento: ", recuento)

#------------------------------------------------------------------

# EJERCICIO 6

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Calculo y promedios

print("Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#-------------------------------------------------------------------

# EJERCICIO 7

parcial1 = {"Juan", "Laura", "Fabricio", "Cristian"}
parcial2 = {"Roberto", "Carolina", "Mauricio", "Juan"}

# Aprobados en ambos parciales

ambos = parcial1 & parcial2

# Aprobados en un solo parcial

solo_uno = parcial1 ^ parcial2

# Aprobados en al menos un parcial

al_menos1 = parcial1 | parcial2

# Resultados
print("Aprobados en ambos parciales: ", ambos)
print("Aprobados solo en uno de los dos parciales: ", solo_uno)
print("Aprobados en al menos un parcial: ", al_menos1)

#------------------------------------------------------------------

# EJERCICIO 8

# Diccionario

stock_productos = {
    "Mouse" : 20,
    "Teclado" : 17,
    "Monitor 27 pulgadas" : 23,
    "Gabinete" : 15
}

# Menu de eleccion (consultar, agregar stock o agregar producto)

# Consultar stock

def gestionar_stock(stock, producto):
    if producto in stock:
        print(f"Stock de '{producto}': {stock[producto]} unidades.")
    else:
        print("Este producto '{producto}' no esta ingresado en el inventario.")

# Agregar unidades al stock o productos al inventario

def actualizar_stock(stock, producto, unidades):
    if producto in stock:
        stock[producto] += unidades
        print(f"Se agregaron {unidades} unidades a '{producto}. Nuevo stock: {stock[producto]}")
    else:
        stock[producto] = unidades
        print(f"Producto '{producto} agregado con {unidades} unidades.")

# Menu interactivo
while True:
    print("Menu interactivo")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto")
    print("3. Agregar nuevo producto")
    print("4. Salir")

    opcion = input("Ingrese una opcion para continuar: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a consultar: ")
        gestionar_stock(stock_productos, producto)

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto existente: ")
        try:
            unidades = int(input(f"Cantidad de unidades a agregar a '{producto}': "))
            actualizar_stock(stock_productos, producto, unidades)
        except ValueError:
            print("Error: Ingrese un numero valido.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        try:
            unidades = int(input(f"Cantidad de unidades iniciales para '{producto}': "))
            actualizar_stock(stock_productos, producto, unidades)
        except ValueError:
            print(" Error: ingrese un número válido.")

    elif opcion == "4":
        print("Saliendo del inventario.")
        break

    else:
        print("Opcion invalida. Elija entre 1 y 4")
        

#---------------------------------------------------------------

# EJERCICIO 9

agenda = {
    ("Lunes", "19:30"): "Ir al gimnasio",
    ("Martes","12:00"): "Turno psicologo",
    ("Miercoles", "16:30"): "Comprar regalo de cumpleaños para Marcos",
    ("Viernes", "9:30"): "Turno Kinesiologo"
}

dia = input("Ingrese el dia (ej. 'lunes'): ").lower()
hora = input("Ingrese la hora (ej. '10:00'): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad el {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay actividad registrada el {dia} a las {hora}.")

#---------------------------------------------------------------

# EJERCICIO 10

# Diccionario con paises y capitales

diccionario_origianl = {
    "Alemania": "Berlín",
    "Austria": "Viena",
    "Azerbaiyan": "Baku",
    "Colombia": "Bogota",
    "Ecuador": "Quito"
}

# Diccionario anterior invertido
invertido = {}

for pais, capital in diccionario_origianl.items():
    invertido[capital] = pais

# Resultado
print("Diccionario invertido: ")
print(invertido)



