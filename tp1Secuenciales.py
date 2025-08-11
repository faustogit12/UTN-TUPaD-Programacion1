#EJERCICIO 1
print("Hola Mundo!")


#-----------------------------------------------------------------------
#EJERCICIO 2
nombre = input("Introduce tu nombre: ")
print(f"Hola " + nombre + "!.")


#-----------------------------------------------------------------------
#EJERCICIO 3
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
lugarDeRecidencia = input("Introduce tu lugar de residencia: ")
print(f"Hola {nombre} {apellido}, tienes {edad} años y vives en {lugarDeRecidencia}.")


#-----------------------------------------------------------------------
#EJERCICIO 4
radio = float(input("Introduce el radio de la circunferencia: "))
pi = 3.14
print(f"El área de la circunferencia es: {area}.")
print(f"El perímetro de la circunferencia es: {perimetro}.")


#-----------------------------------------------------------------------
#EJERCICIO 5
segundos = int(input("Introduce un número: "))

#Conversión de segundos a horas
horas = segundos // 3600

#resultado
print(f"Los {segundos} segundos introducidos en horas es: {horas} horas")


#-----------------------------------------------------------------------
#EJERCICIO 6
numero = int(input("Introduce un número: "))

print(f"La tabla de multiplicar del {numero} es:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


#-----------------------------------------------------------------------
#EJERCICIO 7
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print(f"La suma de {numero1} y {numero2} es: {numero1 + numero2}.")
print(f"La resta de {numero1} y {numero2} es: {numero1 - numero2}.")
print(f"La multiplicación de {numero1} y {numero2} es: {numero1 * numero2}.")
print(f"La división de {numero1} y {numero2} es: {numero1 / numero2}.")


#-----------------------------------------------------------------------
#EJERCICIO 8
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

#calculo del IMC
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}.")


#-----------------------------------------------------------------------
temperatura = float(input("Introduce la temperatura en grados Celsius: "))

#Conversión de Celsius a Fahrenheit
fahrenheit = (temperatura * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}°F.")


#-----------------------------------------------------------------------
#EJERCICIO 10
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

#calculo del promedio
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los números {numero1}, {numero2} y {numero3} es: {promedio:.2f}.")


#-----------------------------------------------------------------------