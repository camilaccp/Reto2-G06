def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

# En la primera funcion, se crea una lista con elementos, y se pone la llave de size para saber cuantos elementos tiene la lista, y se inicializa en 0.

def get_element(my_list, index):
    return my_list['elements'][index]

# En la segunda funcion, se obtiene el elemento de la lista en la posicion index, y se retorna ese elemento.

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    if size > 0:
        existe = False
        for pos in range(0, size):
            info = my_list['elements'][pos]
            if cmp_function(element, info) == 0:
                existe = True
                break
        if existe:
            return pos
    return -1

# En la tercera funcion, se verifica si un elemento esta presente en la lista, usando una funcion de comparacion. 
# Si el elemento esta presente, se retorna la posicion del elemento en la lista, de lo contrario se retorna -1.

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

#Agregar un elemento al principio de la lista, usando el metodo insert() para insertar el elemento 
# en la posicion 0 de la lista, y se incrementa el tamaño de la lista en 1.

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

# Agregar un elemento al final de la lista, usando el metodo append() para agregar el elemento
# al final de la lista, y se incrementa el tamaño de la lista en 1. 

def size(my_list):
    return my_list["size"]

# En la quinta funcion, se retorna el tamaño de la lista, 
# usando la llave size para obtener el valor del tamaño de la lista.

def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][0]
    return None

# En la sexta funcion, se retorna el primer elemento de la lista,

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][my_list["size"] - 1]
    return None

def delete_element(my_list, pos):
    
    if pos < 0 or pos >= my_list["size"]:
        return None
    
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] > 0:
        element = my_list["elements"][0]
        del my_list["elements"][0]
        my_list["size"] -= 1
        return element
    return None

def remove_last(my_list):
    if my_list["size"] > 0:
        element = my_list["elements"].pop() #este elimina el ultimo elemento de la lista
        my_list["size"] -= 1
        return element
    return None

def insert_element(my_list, pos, element):
    if pos < 0 or pos > my_list["size"]:
        return None
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_element):
    if pos < 0 or pos >= my_list["size"]:
        return None
    my_list["elements"][pos] = new_element
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        return None
    temporal = my_list["elements"][pos1]
    my_list["elements"][pos1] = my_list["elements"][pos2]
    my_list["elements"][pos2] = temporal
    
    return my_list

def sub_list(my_list, pos1, pos2):
    
    if (pos1 < 0) or (pos1 >= my_list["size"]) or (pos2 < 0) or (pos2 >= my_list["size"]) or (pos1 > pos2):
        return None
    resultado = new_list()
    for i in range(pos1, pos2 + 1):
        add_last(resultado, my_list["elements"][i])
    return resultado
        
#Esta funcion crea una sublista de la lista original, desde la posicion pos1 hasta la posicion pos2, y retorna la nueva sublista.

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

def selection_sort(my_list, sort_crit=default_sort_criteria):
    
    """
    Esta funcion ordena la lista dada usando el algoritmo de seleccion (selection sort)
    Entonces, en cada vuelta, busca el elemento que deberia ir primero segun el criterio ingresado
    dentro del rango que falta por ordenar, y lo intercambia con la posicion actual
    
    """
    
    #En cada vuelta que va haciendo, va a buscar cual es el elemento que deberia ir en la posicion actual y lo trae con un intercambio.
    
    size = my_list["size"]
    for i in range(0, size): #Empiezo el recorrido de 0 a size
        elegido = i
        for j in range(i+1, size): #Empiezo el sub recorrido una posicion despues de i, no antes porque se supone que eso ya se evaluo
            if sort_crit(my_list["elements"][j], my_list["elements"][elegido]):
                #Si el elemento j deberia ir antes que el elegido actual, entonces ahi j pasa a ser el nuevo elegido.
                elegido = j
        #Si el elegido es diferente a i entoces hacemos un exchange, si son iguales pues nada se queda igual
        if elegido != i:
            exchange(my_list, i, elegido)
    
    return my_list

def insertion_sort(my_list, sort_crit=default_sort_criteria):
    
    """
    Esta funcion va a orderna la lista usando el algoritmo de insercion o insertion sort
    entonces va a ir tomando cada elemento y lo va a ir incertando hacia atras, intercambiandolo
    mientras que siga siendo menor que el elemento anterior.
    """
    
    size = my_list["size"]
    
    #Empezamos en 1 y no en 0 porque un solo elemento ya esta "ordenado" por definicion. 
    # i Sera el elemento que vamos a ordenar o insertar en la parte que ya esta ordenada (0 hasta i-1)
    
    for i in range(1, size): 
        j = i
        
        #Mientras que no hayamos llegado de nuevo al inicio, y el elemento en j deba ir antes que su vecino izquierdo j-1, entoncess:
        
        while j > 0 and sort_crit(my_list["elements"][j], my_list["elements"][j-1]):
            exchange(my_list, j, j-1)
            #Avanzamos el puntero un paso hacia atras y volvemos a hacer la pregunta o el recorrido
            j -= 1
            
            #Asi hacemos que el while pare y siga el recorrido del for con los siguientes numeros.
    
    return my_list

#Es como un insertion sort pero tipo mejorado, entonces en vez de comparar solo los vecinos consecutivos, primero compara 
#los elementos por separado por un salto grande, y va reduceindo ese salto hasta llegar a 1.

def shell_sort(my_list, sort_crit=default_sort_criteria):
    
    """ 
    Este ordena la lista usando el algoritmo de Shell Sort
    Es una generalizacion de la insertion sort, compara elementos separados por un salto
    (gap) que se va reduciendo hasta que ese gap sea 1
    """
    
    size = my_list["size"]
    gap = 1
    
    #Calcula el gap inicial mas grande posible con la secuencia de 1, 4, 13, 40, conocida como la secuencia de Knuth, sin que se pase del size/3
    
    while gap < size//3:
        gap = 3 * gap + 1
        
    while gap >= 1:
        for i in range(gap, size):
            j = i
            while j >= gap and sort_crit(my_list["elements"][j], my_list["elements"][j-gap]):
                exchange(my_list, j, j-gap)
                j -= gap
        gap = gap //3
        
    return my_list            

def merge_sort(my_list, sort_crit=default_sort_criteria):
    """
    Esta funcion ordena la lista usando el algoritmo de merge sort
    """
    if size(my_list) <= 1:
        return my_list
    mid = size(my_list) // 2
    left_half = sub_list(my_list, 0, mid - 1)
    right_half = sub_list(my_list, mid, size(my_list) - 1)
    left_sorted = merge_sort(left_half, sort_crit)
    right_sorted = merge_sort(right_half, sort_crit)
    return merge(my_list, left_sorted, right_sorted, sort_crit)

def merge(my_list,left, right, sort_crit):
    left=left["elements"]
    right=right["elements"]
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if sort_crit(right[j], left[i]):
            my_list["elements"][k] = right[j]
            j+=1
        else:
            my_list["elements"][k] = left[i]
            i+=1
        k+=1
    while i < len(left):
        my_list["elements"][k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        my_list["elements"][k] = right[j]
        j+=1
        k+=1
    return my_list

""" quick_sort, en vez de dividir por la mitad y despues unir como en merge,
el quicksort lo que hace esque va a elegir un pivote, entonces acomoda
todo lo que sea menor a la izquierda y todo lo mayor a la derecha, entonces
eso lo llamamos tmb partición, y despues de esto, ordenamos recursivamente cada lado.
El pivote ya queda en su posicion final desde el princiipio sin necesidad de un merge
al final.

"""

def particion(my_list, pequeño, grande, sort_crit):
    
    """ Vamos a acomodar los elementos entre pequeño y grande alrededro
    de un pivote que seria el ultimo elemento.
    todo lo que va antes del pivote queda a su izquierda, y el resto
    a su derecha, al final va a retornar la posicion final del pivote.
    """
    
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