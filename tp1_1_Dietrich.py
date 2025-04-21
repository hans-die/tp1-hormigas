from random import choice
import time 
from termcolor import colored

filas = 30
columnas = 30
obs = 20  #Obstaculos
comida = 15 #COMIDA
numero_hormigas = 5 #Hormigas

simulaciones = 200 #Numero de simulaciones

# Grilla verde
def creacion_grilla(f,c):
    """
    -Parametros de entrada: Las respectivas filas (int) y columnas (int) que elija
    -Parametros de salida: La matriz(list)
    -Lo que hace esta funcion es recibir dos numeros y arma una lista de listas con las respectivas filas y columnas. A su vez imprime todos esos datos
    en color verde.
     """
    matriz = [[colored("▓▓","green")for i in range(f)]for i in range(c)] 
    return matriz

matriz_verde = creacion_grilla(filas,columnas)

def creacion_matriz(fil,col):  # Agarro a la matriz que es una lista de listas y la convierto en una lista entera
    """
    -P.E: Las respectivas filas (int) y columnas (int) que elija
    -P.S: La matriz en una lista(list)
    -Basicamente lo que hace esta funcion es convertir la grilla anterior que era una lista de listas y crea una nueva que es una lista entera.
    Esto me facilita operaciones futuras.
     """
    matriz_libre = []
    for f in range(fil):
        for c in range(col):
            matriz_libre.append((f,c))
    return matriz_libre

matriz_libre = creacion_matriz(filas,columnas)

lugares_usados = [] #lista para evitar repeticion
obstaculoss = []

def poner_obstaculos(matriz):
    """
    -Lo que hace esta funcion es poner los obstaculos en la grilla. Agarra un valor random de la matriz completa y lo pinta de negro, a su vez mete este valor
    en una lista donde van todos las celdas usadas.
    -P.e: La matriz (list)
    -P.S: La posicion de los obstaculos en la matriz (list)
    """
    for i in range(obs):
        obstaculos = choice(matriz_libre) #Busco 10 lugares
        f, c = obstaculos
        matriz_verde[f][c] = colored("▓▓", "grey")
        lugares_usados.append(obstaculos)
        obstaculoss.append(obstaculos)
    return matriz[f][c]

poner_obstaculos(matriz_verde)
morfi = []
def poner_comida(matriz):
    """
    -Lo que hace esta funcion es poner la comida en la grilla. Agarra un valor random de la matriz completa y lo pinta de blanco, a su vez mete este valor
    en una lista donde van todos las celdas usadas.
    -P.e: La matriz (list)
    -P.S: La posicion de la comida en la matriz (list)
    """
    for i in range(comida):
        while True:
            celda_comida = choice(matriz_libre) #Busco 25 lugares
            if celda_comida not in lugares_usados:
                f, c = celda_comida
                matriz[f][c] = colored("▓▓","white")
                lugares_usados.append(celda_comida)
                morfi.append(celda_comida)
                break
    return matriz[f][c]

poner_comida(matriz_verde)

hormigas = []
#HORMIGA
def poner_hormiga(matriz):
    """
    -Lo que hace esta funcion es poner las hormigas en la grilla. Agarra un valor random de la matriz completa y lo pinta de rojo, a su vez mete este valor
    en una lista donde van todos las celdas usadas. Tambien mete a las hormigas en una lista.
    -P.e: La matriz (list)
    -P.S: La posicion de las hormigas en la matriz (list)
    """
    for i in range(numero_hormigas):
            while True:
                hormiga = choice(matriz_libre)
                if hormiga not in lugares_usados:
                    f, c = hormiga
                    matriz[f][c] = colored("▓▓","red")
                    lugares_usados.append(hormiga)            
                    hormigas.append(hormiga)
                    break
    return matriz[f][c]

poner_hormiga(matriz_verde)

movimiento = [(-1,0),(1,0),(0,-1),(0,1)] #fijo estos numeros como si fuese un control remoto, izq,der,arriba,abajo

def movimiento_hormigas(posicion_actual,matriz,movimiento): #movimiento de una hormiga
    """
    Lo primero que hace esta funcion es elegir por random un numero de la lista "movimiento". Luego suma / resta este numero con la posicion actual de la hormiga.
    Despues por medio de un if chequea que la nueva posicion de la hormiga este dentro de la matriz y no arriba de un obstaculo. Por ultimo, si esto se cumple
    pinta de color amarillo la celda previa y pinta de roja la nueva. Ademas suma los pasos de cada hormiga y cuenta la comida que comen las hormigas.
    -Sus parametros de entrada son: la posicion de la hormiga actual, la matriz completa, los posibles movimientos de la hormiga
    -El parametro de salida es la nueva posicion de la hormiga,los pasos de cada hormiga y la comida recogida, siempre y cuando se cumpla el if, sino es la posicion vieja(o sea no se mueve)
    """
    pasos = 0
    contador_comida = 0
    intentos = 0
    while True:
        eleccion = choice(movimiento) #agarro un numero random de la lista
        nueva_f = posicion_actual[0] + eleccion[0]
        nueva_c = posicion_actual[1] + eleccion[1]
        nueva_posicion = (nueva_f,nueva_c) # creo la nueva posicion de la hormiga, sumandole el numero anterior
        fila_g = len(matriz)
        columna_g = len(matriz[0])
        if -1 < nueva_f < fila_g and -1 < nueva_c < columna_g and matriz[nueva_f][nueva_c] != colored("▓▓", "grey") and matriz[nueva_f][nueva_c]!= colored("▓▓","red"): #asi es como hago que la hormiga no pueda salirse la matriz y no pueda avanzar ante un obs
            if matriz[nueva_f][nueva_c] == colored("▓▓","white"): #asi es como cuento cada vez que una hormiga come
                contador_comida += 1
            matriz[nueva_f][nueva_c] = colored("▓▓","red") # si se cumple el primer if se pinta la nueva celda de rojo
            pasos += 1 # lo mismo que lo anterior, si se cumple el primer if se suma un paso.
            matriz[posicion_actual[0]][posicion_actual[1]] = colored("▓▓","yellow")
            return nueva_posicion, pasos, contador_comida # armo 3 return si se cumple cada if, si no se cumplen retorna el if de abajo, devolviendo el valor previo al if.
        intentos += 1
        if intentos > 10:
            return posicion_actual,pasos, contador_comida

lol = len(hormigas)
lol2 = len(obstaculoss)
lol3 = len(morfi)
pasos_totales = 0
comida_recogida = 0
for l in range(simulaciones):
    for i in range(len(hormigas)): #la forma que encontra para repetir la funcion para cada hormiga
        hormigas[i], pasos, comida_tot = movimiento_hormigas(hormigas[i],matriz_verde,movimiento)
        pasos_totales +=pasos #sumo cada paso a la comida recogida, luego la imprimo en cada simulacion y al final del programa.
        comida_recogida += comida_tot #hago lo mismo que con los pasos.
    #print("\033c", end="")  # LIMPIA LA PANTALLA (OPCIONAL) - Probarlo borrando "#" del comienzo
    print(f" {colored('Simulacion','blue')} {colored(l+1,'green')}/{colored(simulaciones,'white')}\tPasos: {pasos_totales}\t{colored(f'Comida: {comida_recogida}','red')} \t {lol} \t {lol2} \t {lol3}")
    for linea in matriz_verde: #ejecuto el programa     
        print("".join(linea))
    time.sleep(0.001)


print(colored(f"\n\t-Simulacion terminada.\n\t-Pasos totales recorridos: {pasos_totales}\n\t-Comida recogida total: {comida_recogida} ","green"))
