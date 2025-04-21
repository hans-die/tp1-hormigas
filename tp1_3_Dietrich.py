from random import choice

# Aclaracion: Las funciones tienen leves modificaciones , principalmente de reducciond e variables o condiciones las cuales facilitan el codigo
filas = 30
columnas = 30
obs = 10  #Obstaculos

numero_hormigas = 5 #Hormigas

simulaciones = 10000 #Numero de simulaciones

iteraciones = 200

movimiento = [(-1,0),(1,0),(0,-1),(0,1)] #fijo estos numeros como si fuese un control remoto, izq,der,arriba,abajo


# Grilla verde
def creacion_grilla(f,c):
    """
    -Parametros de entrada: Las respectivas filas (int) y columnas (int) que elija
    -Parametros de salida: La matriz(list)
    -Lo que hace esta funcion es recibir dos numeros y arma una lista de listas con las respectivas filas y columnas. A su vez imprime todos esos datos
    en color verde.
     """
    matriz = [["green"for i in range(f)]for i in range(c)] 
    return matriz



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


lugares_usados = [] #lista para evitar repeticion

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
        matriz_verde[f][c] = "grey"
        lugares_usados.append(obstaculos)
    return matriz[f][c]

def poner_obstaculos(matriz, matriz_libre, lugares_usados): # Hago cambios leves para modificar en este tp
    """
    -Lo que hace esta funcion es poner los obstaculos en la grilla. Agarra un valor random de la matriz completa y lo pinta de negro, a su vez mete este valor
        en una lista donde van todos las celdas usadas.
    -P.e: La matriz (list), la matriz libre y los lugares usados
    """
    for _ in range(obs):
        while True:
            obstaculo = choice(matriz_libre)
            if obstaculo not in lugares_usados:
                f, c = obstaculo
                matriz[f][c] = "grey"
                lugares_usados.append(obstaculo)
                break

hormigas = []
#HORMIGA
def poner_hormigas(matriz, matriz_libre, lugares_usados):
    """
    Esta funcion pone las hormigas dentro de una lista. Devuelve el lugar de cada hormiga de la grilla, dependiendo de cuantas 
    se fijan. 
    pe: La matriz entera, la matriz libre en lista d listas y los lugares usados para registrar
    ps: la posicion de las hormigas"""
    hormigas = []
    while len(hormigas) < numero_hormigas:
        pos = choice(matriz_libre)
        if pos not in lugares_usados:
            f, c = pos
            matriz[f][c] = "red"
            lugares_usados.append(pos)
            hormigas.append(pos)
    return hormigas


def movimiento_hormigas(posicion_actual, matriz):
    """
    -Esta funcion mueve a las hormigas, mediante algunas condiciones las cuales le permiten o no moverse a la hormiga.
    -pe: La posicion de cada hormiga, y la matriz
    -ps : la nueva posicion de las hormigas
    """
    eleccion = choice(movimiento)
    nueva_f = posicion_actual[0] + eleccion[0]
    nueva_c = posicion_actual[1] + eleccion[1]
    fila_g = len(matriz)
    columna_g = len(matriz[0])
    if 0 <= nueva_f < fila_g and 0 <= nueva_c < columna_g:
        if matriz[nueva_f][nueva_c] != "grey":
            return (nueva_f, nueva_c)
    return posicion_actual


area_total = 0
#Asi es como hago el calculo del area
for l in range(simulaciones):
    matriz_verde = creacion_grilla(filas, columnas) 
    matriz_libre = creacion_matriz(filas, columnas)
    lugares_usados = []
    poner_obstaculos(matriz_verde, matriz_libre, lugares_usados)
    hormigas = poner_hormigas(matriz_verde, matriz_libre, lugares_usados)
    
    celdas_visitadas = []
    for h in hormigas:
        celdas_visitadas.append(h)

    for l in range(iteraciones): #ahora repito todo por cada iteracion
        for i in range(len(hormigas)):
            nueva_pos = movimiento_hormigas(hormigas[i], matriz_verde)
            hormigas[i] = nueva_pos
            if nueva_pos not in celdas_visitadas:
                celdas_visitadas.append(nueva_pos)
    
    area_total += len(celdas_visitadas)

promedio_area = area_total / simulaciones #saco el promedio del area con las simulaciones
print(f"Area recorrida promedio: {promedio_area:.2f} celdas")

