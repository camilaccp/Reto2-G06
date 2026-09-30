import random
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):

    """Crea una nueva tabla de hash (map) donde sus entradas llave-valor 
    se inicializan con valores None-None.

    Parameters:
    num_elements (int): Cuantos elementos voy a guardar
    load_factor (float): que tan llena vamos a dejar que se ponga la tabla antes de que se haga un rehash
    prime (int): el numero primo del hash, si no me lo dan vale 109345121

    Returns:
    Tabla recien creada.
    Return type:
    map_linear_probing"""

    #La capacidad es cuanto puedo guardar, si quiero guardar por ejemplo 100 elementos con un
    #factor de carga de 0.5, la tabla debe tener al menos 100/0.5 = 200 casillas. 
    #La documentacion va a pedir el primo mayor siguiente de ese numero.
    
    capacidad = mf.next_prime(num_elements/load_factor)
    
    #scale y shift son los a y b de la formula de MAD y tenemos que elegirlos al azar
    #según los rangos que nos dan.
    
    scale = random.randint(1, prime-1)
    shift = random.randint(0, prime-1)
    
    #la tabla es un array list con capacity de casillas y cada una con un
    #map_entry vacio
    
    tabla = al.new_list()
    for _ in range(capacidad):
        al.add_last(tabla, me.new_map_entry(None, None))
        
    #Vemos que la tabla no empieza con un size 0 sino que viene como llena pero con casillas vacias.
    
    my_map = {
        "prime": prime,
        "capacity": capacidad,
        "scale": scale,
        "shift": shift,
        "table": tabla,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }
    
    return my_map


    
def put(my_map, key, value):
    
    """
    1. Calculamos la posicion inicial con el hash
    2. le pregutnamos a find_slot si la llave existe y si si en que posicion
    3. si ya existe solo actualizamos el valor, entonces el size aqui no cambia
    4. si no existe, pongo la pareja nueva en la posicion libre, sumo 1 al size y recalculo el factor de carga.
    5. si el factor de carga repaso el limite, toca hacer hash.
    
    """
    
    hash_value = mf.hash_value(my_map, key)
    ocupado, pos = find_slot(my_map, key, hash_value)
    
    if ocupado:
        entry = al.get_element(my_map["table"], pos)
        me.set_value(entry, value)
    else:
        al.change_info(my_map["table"], pos, me.new_map_entry(key, value))
        my_map["size"] +=1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    
def contains(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    ocupado, pos = find_slot(my_map, key, hash_value)
    return ocupado

def get(my_map, key):
    """
    Da el valor asociado a la llave key. Si la llave no existe, devuelve None.
    """
    hash_value = mf.hash_value(my_map, key)
    ocupado, pos = find_slot(my_map, key, hash_value)
    if ocupado:
        entry = al.get_element(my_map["table"], pos)
        return me.get_value(entry)
    return None


def remove(my_map, key):
    
    hash_value = mf.hash_value(my_map, key)
    ocupado, pos = find_slot(my_map, key, hash_value)
    if ocupado:
        al.change_info(my_map["table"], pos, me.new_map_entry("__EMPTY__", "__EMPTY__"))
        my_map["size"] -=1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map


def key_set(my_map):
    
    llaves = al.new_list()
    for i in range(al.size(my_map["table"])):
        entrada = al.get_element(my_map["table"],i)
        llave = me.get_key(entrada)
        
        if llave is not None and llave != "__EMPTY__":
            al.add_last(llaves, llave)
    return llaves

def value_set(my_map):
    
    valores = al.new_list()
    for i in range(al.size(my_map["table"])):
        entrada = al.get_element(my_map["table"],i)
        llave = me.get_key(entrada)
                
        if llave is not None and llave != "__EMPTY__":
            al.add_last(valores, me.get_value(entrada))
    return valores

def is_empty(my_map):
    return my_map["size"] == 0


def size(my_map):
    """
    Numero de elementos en el mapa.
    """
    return my_map["size"]


#FUNCIONES AUXILIARES

def default_compare(key, entry):
    
    """ Compara una llave con la llave de entrada """
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def is_available(table, pos):
    
    """ Dice si en esa casilla se puede insertar, es decir, si esta vacia (None)
    o si alli hubo algo que se borró, que se marca con la llave "__EMPTY__" """
    
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False
    

def find_slot(my_map, key, hash_value):
    
    """
    Esta es la funcion clave, arranca en hash_value y avanza casilla por casilla
    1. si la casilla esta disponible, guarda la primera disponible que encuentra
    porq ahi va a insertarla, si ademas esta vacia de verdad (None), ya puede parar
    porq la llave no existe.
    2. si la casilla tiene la misma llave, la encontro, entonces esta ocupada en esa
    posicion.
    3. en cualquiera caso pasa a la sigueinte con (hash_value +1)%capacity, y el %
    hace que de la vuelta al llegar al final.
    """

    primero_available = None
    found = False
    ocupado = False
    
    while not found:
        if is_available(my_map["table"], hash_value):
            if primero_available is None:
                primero_available = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            primero_available = hash_value
            found = True
            ocupado = True
        hash_value = (hash_value+1) % my_map["capacity"]
    
    return ocupado, primero_available

def rehash(my_map):
    
    tabla_antigua = my_map["table"]
    nueva_capacidad = mf.next_prime(2 * my_map["capacity"])
    
    new_table = al.new_list()
    for _ in range(nueva_capacidad):
        al.add_last(new_table, me.new_map_entry(None, None))
        
    my_map["table"] = new_table
    my_map["capacity"] = nueva_capacidad
    my_map["size"] = 0
    my_map["current_factor"] = 0
    
    for i in range(al.size(tabla_antigua)):
        entry = al.get_element(tabla_antigua, i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            put(my_map, key, me.get_value(entry))
    
    return my_map



