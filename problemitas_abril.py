""" 5) Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el 
color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color 
inválido” si es cualquier otro."""

""" color = str(input("ingrese un color escribiendo solo en minusculas: " ))

def determinar_color(color):
    if color == "verde":
        return (f'Puede pasar')
    elif color == "amarillo":
        return (f'Precaución')
    elif color == "rojo":
        return (f'No pasar')
    else:
        return (f'Color inválido')


print(determinar_color(color)) """


"""7) Hacer un programa que cuente del 1 al 100 inclusive e imprima sólo los números pares """

""" 
for i in range (101):
        if i %2 == 0:
                print (i).

Mi codigo mal hecho:

def encontrar_pares(numeros):
        numeros_pares = []
        for i in numeros (101):
                if i % 2 == 0:
                        numeros_pares.append(numeros)
        return {numeros_pares}
print(encontrar_pares)
 """

""" #Solucion:

def encontrar_pares():
        numeros_pares = []
        for i in range (101):
                if i % 2 == 0:
                        numeros_pares.append(i)
        return numeros_pares

print(encontrar_pares())

 """

"""
10) Hacer un programa que muestre el siguiente dibujo.
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

asteriscos = " *"
lista_de_asteriscos = []

print(asteriscos*10)
for i in range(8):
    lista_de_asteriscos.append(asteriscos)
    print(lista_de_asteriscos)
    
    
    



12)Hacer un programa que muestre el siguiente dibujo
*
* *
* * *
* * * *
* * * * *

asteriscos = " *"
lista_de_asteriscos = []

for i in range(5):
    lista_de_asteriscos.append(asteriscos)
    print(lista_de_asteriscos)


15)Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es
múltiplo del otro. Crea una función EsMultiplo que reciba
 los dos números, y devuelve si el primero es múltiplo del segundo.


def EsMultiplo(numero1, numero2):
    if numero1 % numero2 == 0:
        return "numero 1 es multiplo de numero 2"
    elif numero2 % numero1 == 0:
        return "numero 2 es multiplo de numero 1"
    else:
        return "los numeros no son multiplos entre si"

numero1 = int(input("ingrese un numero por favor: "))
numero2 = int(input("ingrese otro numero por favor: "))
print(EsMultiplo(numero1, numero2))


16)Crear una función que calcule la temperatura media de un día a partir de la temperatura
máxima y mínima.
 Crear un programa principal, que utilizando la función anterior, vaya pidiendo la
temperatura máxima y mínima de cada día y vaya mostrando la media.
 El programa pedirá el número de días que se van a introducir.
"""

def temperatura_media(temperatura1, temperatura2):
    temperatura_promedio = (temperatura1 + temperatura2)/2
    return temperatura_promedio

temperatura1 = int(input("ingrese la temperatura minima de hoy, por favor: "))
temperatura2 = int(input("ingrese la temperatura máxima de hoy, por favor: "))
print(temperatura_media(temperatura1, temperatura2))