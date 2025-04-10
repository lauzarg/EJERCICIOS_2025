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
Mi codigo mal hecho:


def encontrar_pares(numeros):
        numeros_pares = []
        for i in numeros (101):
                if i % 2 == 0:
                        numeros_pares.append(numeros)
        return {numeros_pares}
print(encontrar_pares)
 """

#Solucion:

def encontrar_pares():
        numeros_pares = []
        for i in range (101):
                if i % 2 == 0:
                        numeros_pares.append(i)
        return numeros_pares

print(encontrar_pares())