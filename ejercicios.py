#ejercicio 1:Saludo perzonalizado

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

año_actual = 2026
nacimiento = año_actual - edad

print("Hola", nombre)
print("Naciste aproximadamente en", nacimiento)

#ejercicio 2:Par o impar

num = int(input("Ingresa un número: "))

if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#ejercicio 3:El peaje

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes conducir")
else:
    print("Aún no tienes edad para conducir")

#ejercicio 4:El mayor de dos

a = int(input("Número 1: "))
b = int(input("Número 2: "))

if a > b:
    print("El mayor es", a)
else:
    print("El mayor es", b)

#ejercicio 5:Positivo,negativo o cero

num = int(input("Ingresa un número: "))

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Es cero")

#ejercicio 6:Categoria de edad

edad = int(input("Edad: "))

if edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")

#ejercicio 7:Descuento

total = float(input("Total compra: "))

if total < 50:
    descuento = 0
elif total <= 100:
    descuento = total * 0.05
else:
    descuento = total * 0.10

print("Total a pagar:", total - descuento)

#ejercicio 8:Año bisiesto

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

#ejercicio 9:IMC

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

#ejercicio 10:Credito

salario = float(input("Salario: "))
deuda = input("¿Tiene deuda? (si/no): ")

if salario > 1000 and deuda == "no":
    print("Crédito aprobado")
else:
    print("Crédito denegado")

#ejercicio 11:Cuenta regresiva

num = int(input("Número: "))

while num >= 0:
    print(num)
    num -= 1

print("¡Despegue!")

#ejercicio 12:Suma de N

n = int(input("Número: "))
suma = 0

for i in range(1, n+1):
    suma += i

print("Resultado:", suma)

#ejercicio 13:Tabla de multiplicar

num = int(input("Número: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)

#ejercicio 14:PIN

pin = "1234"
entrada = ""

while entrada != pin:
    entrada = input("Ingresa el PIN: ")

print("Acceso correcto")

#ejercicio 15:Vocales

texto = input("Frase: ")
contador = 0

for letra in texto:
    if letra in "aeiouAEIOU":
        contador += 1

print("Vocales:", contador)

#ejercicio 16:Adivina el numero

secreto = 20
intentos = 5

for i in range(intentos):
    num = int(input("Adivina: "))

    if num == secreto:
        print("Correcto")
        break
    elif num < secreto:
        print("Muy bajo")
    else:
        print("Muy alto")

#ejercicio 17:Numero primo

num = int(input("Número: "))
primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False

if primo and num > 1:
    print("Es primo")
else:
    print("No es primo")

#ejercicio 18:Cjero

saldo = 1000
opcion = 0

while opcion != 3:
    print("1. Ver saldo")
    print("2. Retirar")
    print("3. Salir")
    opcion = int(input("Opción: "))

    if opcion == 1:
        print("Saldo:", saldo)
    elif opcion == 2:
        dinero = int(input("Cantidad: "))
        if dinero <= saldo:
            saldo -= dinero
        else:
            print("No hay saldo suficiente")

#ejercicio 19:Caja registradora

total = 0

while True:
    precio = float(input("Precio (0 para salir): "))
    if precio == 0:
        break
    total += precio

if total > 100:
    total *= 0.9

print("Total:", total)

#ejercicio 20:Fibonacci

n = int(input("Cantidad: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b


