def function(a=0, b=0, c=10):  # Definimos una función con valores por defecto para los parámetros
  a *= 2  # Multiplicamos 'a' por 2
  b *= 3  # Multiplicamos 'b' por 3
  return a + b + c  # Retornamos la suma de 'a', 'b' y 'c'

# Trabajando con variables y tipos de datos
nombre = "Luis Daniel"  # Asignamos una cadena a 'nombre'
nombre = 9  # Reasignamos un entero a 'nombre'
nombre += 10  # Sumamos 10 a 'nombre' (ahora es 19)
print(nombre)  # Imprimimos el valor de 'nombre'

nombre = True  # Reasignamos un valor booleano a 'nombre'
print(nombre)  # Imprimimos el valor de 'nombre' (True)

# Conversión de tipos de datos
numero = "1111"  # Asignamos una cadena de caracteres a 'numero'
numero = int(numero, 10)  # Convertimos la cadena a un entero en base 10
print(numero)  # Imprimimos el número convertido

numero = str(numero)  # Convertimos el número en una cadena
print(numero + "1")  # Concatenamos la cadena con "1" e imprimimos

numero = float(numero)  # Convertimos la cadena a un número flotante
numero = int(numero)  # Convertimos el flotante a un entero
print(numero)  # Imprimimos el valor entero

# Definimos una variable con un solo carácter
caracter = 'a'  

# Operaciones matemáticas básicas
print(5/2)  # División normal (resultado flotante)
print(5//2)  # División entera (sin decimales)
print(25**(1/2))  # Raíz cuadrada de 25
print(64**(1/3))  # Raíz cúbica de 64

print("")  # Imprime una línea vacía

# Operaciones con módulo y horas
hora_inicial = 6
print("Son las", hora_inicial)  # Imprime la hora inicial
hora_inicial = (hora_inicial + 800) % 12  # Calcula la nueva hora en formato de 12 horas
print("La nueva hora es", str(hora_inicial))  # Imprime la nueva hora

# Condiciones IF - ELSE
numero = 10
if numero > 0 and numero < 10:  # Verifica si el número está entre 0 y 10
  print("numero mayor a 0")
  if numero % 2 == 0:  # Verifica si el número es par
    print("numero es par")
elif numero < 0:  # Si el número es negativo
  print("Numero menor que 0")
else:  # Si el número es 0
  print("Numero igual a 0")

# Bucle for con paso negativo
for i in range(10, 0, -2):  # Itera desde 10 hasta 1 con decremento de 2
  print(i)

# Trabajando con listas
lista = [0, 1, 1, 2, 3, 6, "h"]  # Definimos una lista con diferentes tipos de datos
lista.append(14)  # Agregamos el número 14 al final de la lista
lista.insert(1, 19)  # Insertamos el número 19 en la posición 1
print(lista)  # Imprimimos la lista

lista.pop(1)  # Eliminamos el elemento en la posición 1
print(lista)  # Imprimimos la lista después de eliminar el elemento

print(lista.count(1))  # Contamos cuántas veces aparece el número 1 en la lista
lista.clear()  # Vaciamos la lista
print(lista)  # Imprimimos la lista vacía

# Lista anidada y acceso a elementos
lista = [[1, 2, 3], "hola", 10, 'a', True]
print(lista[1][-1])  # Accedemos al último carácter de la segunda posición de la lista

# Entrada de datos desde el usuario
print(input("---Cual es tu nombre?"))  # Pregunta al usuario su nombre e imprime la respuesta
print(input())  # Recibe otra entrada del usuario y la imprime

# Llamada a la función con parámetros nombrados
a = function(b=1, c=2)  # Llamamos a la función con 'b' = 1 y 'c' = 2, 'a' toma su valor por defecto (0)
print(a)  # Imprimimos el resultado de la función
