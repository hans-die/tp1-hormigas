def prueba:
    """
    -Descripcion conzica (2-3 lineas)
    -parametros de entrada
    -parametros de salida (que es lo que sale)
    - si queres mejorarlo poner el tipo de dato que entra y que sale
    """


def creacion_grilla(f,c): #Grilla verde
    """
    -Parametros de entrada: Las respectivas filas (int) y columnas (int) que elija
    -Parametros de salida: La matriz(list)
    -Lo que hace esta funcion es recibir dos numeros y arma una lista de listas con las respectivas filas y columnas. A su vez imprime todos esos datos
    en color verde.
     """
    matriz = [[colored("▓▓","green")for i in range(f)]for i in range(c)] 
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

def poner_obstaculos(matriz): #Esta funcion pone obstaculos
    """
    -Lo que hace esta funcion es poner los obstaculos en la grilla. Agarra un valor random de la matriz completa y lo pinta de negro, a su vez mete este valor
    en una lista donde van todos las celdas usadas.
    -P.e: La matriz (list)
    -P.S: La posicion de los obstaculos en la matriz (list)
    """
    for i in range(obs):
        obstaculos = random.choice(matriz_libre) #Busco 10 lugares
        f, c = obstaculos
        matriz[f][c] = colored("▓▓", "grey")
        lugares_usados.append(obstaculos)
    return matriz[f][c]

def poner_comida(matriz): #Pone comida
    """
    -Lo que hace esta funcion es poner la comida en la grilla. Agarra un valor random de la matriz completa y lo pinta de blanco, a su vez mete este valor
    en una lista donde van todos las celdas usadas.
    -P.e: La matriz (list)
    -P.S: La posicion de la comida en la matriz (list)
    """
    for i in range(comida):
        celda_comida = choice(matriz_libre) #Busco 25 lugares
        f, c = celda_comida
        if not (f,c) in lugares_usados:
            matriz[f][c] = colored("▓▓", "white")
            lugares_usados.append(celda_comida)
    return matriz[f][c]


def poner_hormiga(matriz):
    """
    -Lo que hace esta funcion es poner las hormigas en la grilla. Agarra un valor random de la matriz completa y lo pinta de rojo, a su vez mete este valor
    en una lista donde van todos las celdas usadas. Tambien mete a las hormigas en una lista.
    -P.e: La matriz (list)
    -P.S: La posicion de las hormigas en la matriz (list)
    """
    for i in range(numero_hormigas):
        hormiga = choice(matriz_libre) # 5 hormigas
        f, c = hormiga
        if not (f,c) in lugares_usados: 
            matriz[f][c] = colored("▓▓", "red")
            lugares_usados.append(hormiga)
            hormigas.append(hormiga)
    return matriz[f][c]


def movimiento_hormigas(posicion_actual,matriz,movimiento): #movimiento de una hormiga
    """
    Lo primero que hace esta funcion es elegir por random un numero de la lista "movimiento". Luego suma / resta este numero con la posicion actual de la hormiga.
    Despues por medio de un if chequea que la nueva posicion de la hormiga este dentro de la matriz y no arriba de un obstaculo. Por ultimo, si esto se cumple
    pinta de color amarillo la celda previa y pinta de roja la nueva.
    -Sus parametros de entrada son: la posicion de la hormiga actual, la matriz completa, los posibles movimientos de la hormiga
    -El parametro de salida es la nueva posicion de la hormiga, siempre y cuando se cumpla el if, sino es la posicion vieja(o sea no se mueve)
    """
    eleccion = random.choice(movimiento) #agarro un numero random de la lista
    nueva_f = posicion_actual[0] + eleccion[0]
    nueva_c = posicion_actual[1] + eleccion[1]
    nueva_posicion = (nueva_f,nueva_c) # creo la nueva posicion de la hormiga, sumandole el numero anterior
    fila_g = len(matriz)
    columna_g = len(matriz[0])
    if -1 < nueva_f < fila_g and -1 < nueva_c < columna_g and matriz[nueva_f][nueva_c] != colored("▓▓", "grey"): #asi es como hago que la hormiga no pueda salirse la matriz y no pueda avanzar ante un obs
        matriz[nueva_f][nueva_c] = colored("▓▓","red")
        matriz[posicion_actual[0]][posicion_actual[1]] = colored("▓▓","yellow")
        return nueva_posicion
    return posicion_actual