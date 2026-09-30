
def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

# En la primera funcion, se crea una lista con elementos, y se pone la llave de size para saber cuantos elementos tiene la lista, y se inicializa en 0.

def get_element (my_list, pos):
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1  
    return node ["info"]

# En la segunda funcion, se obtiene el elemento de la lista en la posicion index, y se retorna ese elemento.

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp=my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

# en la tercera funcion, se verifica si un elemento esta presente en la lista, usando una funcion de comparacion.

def add_first(my_list, element):

    new_node = {"info": element, "next": my_list["first"]}
    my_list["first"] = new_node
    if my_list["last"] is None:
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

# En la cuarta funcion, se agrega un elemento al principio de la lista, creando un nuevo nodo que apunta al nodo que estaba primero, y actualizando el puntero "first" de la lista para que apunte a este nuevo nodo. Si la lista estaba vacía, también se actualiza el puntero "last" para que apunte a este nuevo nodo. Finalmente, se incrementa el tamaño de la lista en 1.

def add_last(my_list, element):

    new_node = {"info": element, "next": None} # se crea un nodo cuyo "next" es None porque al ser el último, no apunta a nada más.
    if my_list["size"] == 0: # Si la lista está vacía, el nuevo nodo es tanto el primero como el último.
        my_list["first"] = new_node
        my_list["last"] = new_node
    else: # Si ya tenía elementos, tomamos el nodo que estaba de último (my_list["last"]), hacemos que su puntero "next" apunte al nuevo nodo, y luego actualizamos el puntero "last" de la lista para que sea este nuevo nodo.
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1 # se incrementa el tamaño.
    return my_list

# En la quinta funcion, se retorna el tamaño de la lista

def size(my_list):

    return my_list["size"]

def first_element(my_list):

    if my_list["size"] > 0: #validamos que la lista tenga elementos
        return my_list["first"]["info"] #Como "first" es el primer nodo (un diccionario), accedemos a su llave "info" para obtener el valor que contiene guardado, sin necesidad de recorrer toda la lista.
    return None

# En la sexta funcion, se retorna el primer elemento de la lista,

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] > 0: #validamos que la lista tenga elementos
        return my_list["last"]["info"] #Como "last" es el último nodo (un diccionario), accedemos a su llave "info" para obtener el valor que contiene guardado, sin necesidad de recorrer toda la lista.
    return None

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    else:
        if pos == 0:
            my_list["first"] = my_list["first"]["next"]
            if my_list["size"] == 1:
                my_list["last"] = None
        else:
            anterior = my_list["first"]
            for _ in range(pos - 1):
                anterior = anterior["next"]
            actual = anterior["next"]
            actual = actual["next"]
            if actual == my_list["last"]:
                my_list["last"] = anterior
        my_list["size"] -= 1
    return my_list

def remove_last(my_list):
    element = None
    if my_list["size"] > 0:
        element = my_list["last"]["info"]
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            current = my_list["first"]
            while current["next"] != my_list["last"]:
                current = current["next"]
            current["next"] = None
            my_list["last"] = current
        my_list["size"] -= 1
    return element

def remove_first(my_list):
    
    element = None
    if my_list["size"] > 0:
        element = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        
        if my_list["size"] == 0:
            my_list["last"] = None
    return element

def insert_element(my_list, pos, element):

    if pos <= 0:

        nuevo = {"info": element, "next": my_list["first"]} #diccionario 
        my_list["first"] = nuevo
        
        if my_list["size"] == 0:
            my_list["last"] = nuevo
        my_list["size"] += 1
        
    elif pos >= my_list["size"]:

        nuevo = {"info": element, "next": None}
        
        if my_list["size"] == 0:
            my_list["first"] = nuevo
            my_list["last"] = nuevo
        else:
            my_list["last"]["next"] = nuevo
            my_list["last"] = nuevo
        my_list["size"] += 1
    else:

        actual = my_list["first"]
        for algo in range(pos - 1):
            actual = actual["next"]
        nuevo = {"info": element, "next": actual["next"]}
        actual["next"] = nuevo
        my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):

    if 0 <= pos < my_list["size"]:
        actual = my_list["first"]
        for _ in range(pos):
            actual = actual["next"]
        actual["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if 0 <= pos1 < my_list["size"] and 0 <= pos2 < my_list["size"]:
        actual1 = my_list["first"]
        for _ in range(pos1):
            actual1 = actual1["next"]
        
        actual2 = my_list["first"]
        for _ in range(pos2):
            actual2 = actual2["next"]
        
        temporal = actual1['info']
        actual1["info"] = actual2["info"]
        actual2["info"] = temporal
        
    return my_list

def sub_list(my_list, start, end):    
    sub = new_list()
    
    if 0 <= start <= end < my_list["size"]:
        current = my_list["first"]
        for _ in range(start):
            current = current["next"]
            
        for _ in range(end - start + 1):
            add_last(sub, current["info"])
            current = current["next"]
    return sub

def default_sort_criteria(elemento1, elemento2):
    
    """
    Esta es una funcion de comparacion por defecto que usamos para 
    ordernar elementos.
    Retorna True si el elemento1 es menor que el elemento2, y pues false en caso contraro.
    
    """
    
    ordenada = False
    if elemento1 < elemento2:
        ordenada = True
    return ordenada

def selection_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            pos2 = pos1
            while (pos2 > 0) and (sort_crit(get_element(my_list, pos2), get_element(my_list, pos2-1))):
                exchange(my_list, pos2, pos2-1)
                pos2 -= 1
            pos1 += 1
    return my_list

def insertion_sort(my_list, sort_crit):
    if size(my_list) > 1:
        n = size(my_list)
        pos1 = 0
        while pos1 < n:
            pos2 = pos1
            while (pos2 > 0) and (sort_crit(
                get_element(my_list, pos2), get_element(my_list, pos2-1))):
                node_prev = my_list["first"]
                p = 0
                while p < pos2 - 1:
                    node_prev = node_prev["next"]
                    p += 1
                node_act = node_prev["next"]               
                aux = node_prev["info"]
                node_prev["info"] = node_act["info"]
                node_act["info"] = aux
                pos2 -= 1
            pos1 += 1
    return my_list

def shell_sort(my_list, sort_crit):
    if size(my_list) > 1:
        n = size(my_list)
        h = 1
        while h < n//3:   
            h = 3*h + 1
        while (h >= 1):
            for i in range(h, n):
                j = i
                while (j >= h) and sort_crit(
                                    get_element(my_list, j),
                                    get_element(my_list, j-h)):
                    exchange(my_list, j, j-h)
                    j -= h
            h //= 3    
    return my_list

""" 
La idea de hacer merge sort sobre una lista enlazada es:
1. dividimos la lista, pero encontrando el noso de la mitad
2. conquistar: llamamos al merge sort recursivamente sobre cada mitad (que ya serian sublista enlazadas)
3. combinamos, entonces en vez de comparar primero[i] y segundo[j] con indiices, necesito
es comparar el dato del nodo1 con el dato del nodo 2 y voy luego reconectando punterso para poder
armar la lista.

"""

#Primero creamos una funcion que nos ayude a encontrar el nodo de la mitad.

def encontar_mitad(primer_nodo):
    
    lento = primer_nodo #El lento va a avanzar de a 1
    rapido = primer_nodo #El rapido va a avanzar de a 2
    anterior = None #Esto lo usamos para poder cortar el enlace
    
    while rapido is not None and rapido["next"] is not None:
        
        #Antes de mover lento, lo guardo donde estaba anterior, porque cuando ya termine el while, necesitare saber cual es el ultimo nodo de la primera mitad.
        anterior = lento
        
        #Lento avanza solo un nodo
        lento = lento["next"]
        
        #Rapido avanza dos nodos
        rapido = rapido["next"]["next"]
    
    #Cuando ya acabamos el while, el lento va a quedar parado en el primer nodo de la segunda mitad. Esa mitad 
    #aun va a estar pegada a la primera, entonces hacemos un if que corte esta coneccion. 
    #Le dice al ultimo nodo de la primera mita que su ultimo nodo ya no existe.
    
    if anterior is not None:
        anterior["next"] = None
    
    #lo que buscamos aca es que cuando fast llega al final (digamos su puntero next es None)
    # el slow esta en la mitad de lo que el recorrio.
    
    return lento 

def merge(izquierda, derecha, sort_crit):
    
    #Hacemos este nodo vacio para usarlo como punto de arranque.
    
    nodo = {'info': None, 'next': None}
    cola = nodo
    
    while izquierda is not None and derecha is not None:
        if sort_crit(izquierda['info'],derecha['info']):
            cola['next'] = izquierda
            izquierda = izquierda['next']
        else:
            cola['next'] = derecha
            derecha = derecha['next']
            
        cola = cola['next']
        
    #Cuando ya acabamos el while, una de las dos listas debio haber quedado vacia, mientras que la otra
    #tiene nodos colgando, pero estos nodos que quedan se supone que ya estan ordenados entre si, entonces
    #no necesitamos compararlos uno por uno, simplemente pegar el resto completo de una vez
    
    if izquierda is not None:
        cola['next'] = izquierda
    else:
        cola['next'] = derecha
    
    return nodo['next']

def merge_sort_rec(first_node, sort_crit):
    
    #Evaluamos el caso base.
    
    if first_node is None or first_node['next'] is None:
        return first_node
    
    #Encontramos la mitad y cortamos la lista en dos.
    derecha = encontar_mitad(first_node)
    
    #Ahora tenemos las dos listas separadas
    izquierda = first_node
    
    izquierda_ordenado = merge_sort_rec(izquierda, sort_crit)
    derecha_ordenado = merge_sort_rec(derecha, sort_crit)
    
    resultado = merge(izquierda_ordenado, derecha_ordenado, sort_crit)
    
    return resultado 

def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    
    my_list["first"] = merge_sort_rec(my_list["first"], sort_crit)
    
    actual = my_list["first"]
    while actual["next"] is not None:
        actual = actual["next"]
    my_list["last"] = actual
    
    return my_list

def particion(my_list, pequeño, grande, sort_crit):
    
    pivote = get_element(my_list, grande)
    i = pequeño - 1
    
    for j in range(pequeño, grande):
        if sort_crit(get_element(my_list,j), pivote):
            i+=1
            exchange(my_list, i, j)
    exchange(my_list, i+1, grande)
    return i+1

def quick_sort_1(my_list, pequeño, grande, sort_crit):
    if pequeño < grande:
        posicion_pivote = particion(my_list, pequeño, grande, sort_crit)
        quick_sort_1(my_list, pequeño, posicion_pivote-1, sort_crit)
        quick_sort_1(my_list, posicion_pivote+1, grande, sort_crit)

def quick_sort(my_list, sort_crit=default_sort_criteria):
    
    """Esto va a ordenar la liosta usando el algoritmo de quick sort"""
    
    quick_sort_1(my_list, 0, size(my_list)-1, sort_crit)
    return my_list

#Copiar y pegar lo que ya hicimos en array
    

