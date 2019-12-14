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

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] # Declaramos la lista con los meses del año
bandera = True # Declaramos la bandera en True, para siempre ejecutar el while

while bandera == True: # Mientras la bandera sea True, se ejecutara el while.
    numeroMes = int(input('Ingrese el numero de un mes: ')) # Solicitamos el ingreso de un numero y convertirmos el dato en entero

    if numeroMes > 12: # Validamos que el numero se encuentre dentro del rango del 1 a 12
        print('ERROR..!') # En caso se mayor que 12, saldra un Error
    else:
        if numeroMes == 0: # Regla de Negocio: Si ingresas el valor cero, se termina el programa
            bandera = False
            print(meses)
        else:
            index = numeroMes - 1 # Al numero ingesado por el usuario le restamos uno para que coincida con el indice verdadero del mes.
            print(meses[index])