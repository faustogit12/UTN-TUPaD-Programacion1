#EJERCICIO 1

#LISTA 10 NOTAS DE ESTUDIANTES
notas = [6, 7.50 , 4.75, 6.50, 8, 9, 10, 4.50, 5.25, 7]
print("Lista de notas de estudiantes:")
print(notas)

#CALCULAR EL PROMEDIO DE LAS NOTAS
promedio = sum(notas) / len(notas)
print("El promedio de las notas es:", promedio)

#NOTA MAS ALTA Y MAS BAJA
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)
print("La nota más alta es:", nota_mas_alta)
print("La nota más baja es:", nota_mas_baja)


#EJERCICIO 2
#Pedir 5 productos al usuario
productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto {}: ".format(i+1))
    productos.append(producto)
print("Lista de productos ingresados:")
print(productos)

#Ordenar la lista de productos alfabéticamente
print("Lista de productos ordenados alfabéticamente:")
print(sorted(productos))

#Producto que se desea eliminar y actualizar la lista
producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print("Producto '{}' eliminado.".format(producto_a_eliminar))
else:
    print("El producto '{}' no se encuentra en la lista.".format(producto_a_eliminar))
print("Lista actualizada de productos:")
print(productos)

#EJERCICIO 3
#Lista de 15 numeros enteros al azar el 1 al 100
import random
numeros = [random.randint(1, 100) for _ in range(15)]
print("Lista de números generados:")
print(numeros)

#pares e impares
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Números pares:", pares)
print("Números impares:", impares)

#Observar cuantos numeros tiene cada lista
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

#EJERCICIO 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

#Nueva lista sin duplicados
nueva_lista = list(set(datos))

#ambas listas
print("Lista original: ", datos)
print("Lista nueva: ", nueva_lista)

#EJERCICIO 5
#Lista con nombres de 8 estudiantes
lista_estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge", "Lucía", "Pedro"]
print("Lista de estudiantes:")
print(lista_estudiantes)

#Agregar o eliminar y actualizar la lista
accion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").strip().lower()
if accion == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del estudiante a agregar: ")
    lista_estudiantes.append(nuevo_estudiante)
    print("Estudiante '{}' agregado.".format(nuevo_estudiante))
elif accion == "eliminar":
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in lista_estudiantes:
        lista_estudiantes.remove(estudiante_a_eliminar)
        print("Estudiante '{}' eliminado.".format(estudiante_a_eliminar))
    else:
        print("El estudiante '{}' no se encuentra en la lista.".format(estudiante_a_eliminar))
print("Lista actualizada de estudiantes:")
print(lista_estudiantes)

#EJERCICIO 6
#Lista de 7 numeros rotada a la derecha
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", numeros)
#Rotar a la derecha
rotada_a_la_derecha = [numeros[-1]] + numeros[:-1]
print("Lista rotada a la derecha:", rotada_a_la_derecha)

#EJERCICIO 7
#Matriz anidada 7x2 con T° max y min de 7 dias
temperaturas = [
    [30, 20],  # Lunes
    [32, 21],  # Martes
    [31, 19],  # Miércoles
    [29, 18],  # Jueves
    [28, 17],  # Viernes
    [27, 16],  # Sábado
    [26, 15]   # Domingo
]

print("Matriz de temperaturas (T° max y min de 7 días):")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#Promedios
suma_max = sum(dia[0] for dia in temperaturas)
suma_min = sum(dia[1] for dia in temperaturas)
promedio_max = suma_max / len(temperaturas)
promedio_min = suma_min / len(temperaturas)
print("Promedio de T° máxima de la semana:", promedio_max)
print("Promedio de T° mínima de la semana:", promedio_min)

#Dia en que se registro la mayor amplitud termica
amplitudes = [dia[0] - dia[1] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = dias[amplitudes.index(mayor_amplitud)]

#resultados
print("Día con mayor amplitud térmica:", dia_mayor_amplitud, "con una amplitud de", mayor_amplitud, "grados.")

#EJERCICIO 8
#Matriz de notas 5 estudiantes en 3 materias
notas_estudiantes = [
    [85, 90, 78],  # Estudiante 1
    [88, 76, 92],  # Estudiante 2
    [90, 91, 85],  # Estudiante 3
    [70, 80, 75],  # Estudiante 4
    [95, 89, 94]   # Estudiante 5
]
print("Matriz de notas de 5 estudiantes en 3 materias:")
print(notas_estudiantes)

#Promedio por estudiante
for i, notas in enumerate(notas_estudiantes):
    promedio = sum(notas) / len(notas)
    print("Promedio del Estudiante {}: {:.2f}".format(i+1, promedio))
#Promedio por materia
for j in range(3):
    suma_materia = sum(notas_estudiantes[i][j] for i in range(5))
    promedio_materia = suma_materia / 5
    print("Promedio de la Materia {}: {:.2f}".format(j+1, promedio_materia))



#EJERCICIO 9

#TA TE TI 3x3 con lista de listas con - como casillas vacias, contra dos jugadores

tablero = [["-" for _ in range(3)] for _ in range(3)]

#Mostrar tablero
def mostrar_tablero():
    print("/nTablero_actual")
    for fila in tablero:
        print(" | ".join(fila))
        print()

#funcion para validar posicion
def posicion_valida(fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == "-"

#Juego principal

Turno = "X"

for _ in range(9):
    mostrar_tablero()
    print("Turno de", Turno)
    fila = int(input("Ingresa la fila (0-2): "))
    columna = int(input("Ingresa la columna (0-2): "))
    if posicion_valida(fila, columna):
        tablero[fila][columna] = Turno
        Turno = "O" if Turno == "X" else "X"
    else:
        print("Posición inválida. Intenta de nuevo.")

mostrar_tablero()
print("Juego terminado.")


#EjERCICIO 10
#Matriz 4x7 4 productos vendidos en 7 dias
ventas = [
    [10, 12, 11, 14, 13, 15, 16],  # Producto 1
    [20, 22, 21, 24, 23, 25, 26],  # Producto 2
    [30, 32, 31, 34, 33, 35, 36],  # Producto 3
    [40, 42, 41, 44, 43, 45, 46]   # Producto 4
]

#Total vendido por producto
for i, producto in enumerate(ventas):
    total_producto = sum(producto)
    print("Total vendido del Producto {}: {}".format(i+1, total_producto))

#Dia con mayor cantidad de ventas
total_dias = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_mayor_ventas = total_dias.index(max(total_dias)) + 1
print("Día con mayor cantidad de ventas: Día {}".format(dia_mayor_ventas))

#Producto mas vendido
total_productos = [sum(ventas[i]) for i in range(4)]
producto_mas_vendido = total_productos.index(max(total_productos)) + 1
print("Producto más vendido: Producto {}".format(producto_mas_vendido))

