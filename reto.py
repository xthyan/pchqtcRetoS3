#Ejercicio 01: Mete los valores del 1 al 100 en una lista.

#valoresUnoCien = []

#for i in range(100):
#    valoresUnoCien.append(i+1)

#print(valoresUnoCien)

#metodoProfesor

#Declaraos la lista en blanco
#numeros = []

#Declaramos el limite en 1
#limit = 1

#mientras el limite no sea mayor que 100, se ejecutarà el while
#while limit <= 100:

    #Agregamos el nùmero a la lista decalrada inicialmetmente
    #numeros.append(limit)
    #Aumentamos en 1 la variable limit
    #limit = limit + 1

#Imprimirmos los resultados
#print(numeros)


#Ejercicio 02: Crea una lista con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la lista, muestra el contenido de esa posición sino muestra un mensaje de error.

mesesAnho = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre','Diciembre']
numeroMes = int(input("Ingresa del 1 al 12 para identificar el mes: "))
print(mesesAnho[numeroMes-1])