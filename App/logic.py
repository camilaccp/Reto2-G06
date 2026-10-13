import time
import csv
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp

csv.field_size_limit(2147483647)


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    Para el numero de llaves que espero.
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "orders": al.new_list(), #CREAMOS la lista princiapl con todos los pedidos. Esta le sacaremos todos los reportes de carga.
        "orders_by_month": lp.new_map(30, 0.5), #Para el Req #1, "YYYY-MM"
        "orders_by_country": lp.new_map(50, 0.5), #Para el Req 2 y 5, pais, entonces me da una lista de pedidos de ese pais
        "orders_by_date": lp.new_map(800, 0.5),
        "orders_by_prod_country": lp.new_map(200, 0.5),
        "orders_by_product": lp.new_map(50, 0.5),
        "orders_by_channel": lp.new_map(10, 0.5),
        
        }
    return catalog

def build_order(row):
    
    """ Esta funcion va a convertir una fila del CSV (que es todo texto) a un pedido con sus
    numeros convertidos """
    
    pedido = {
        "Order_ID": row["Order_ID"],
        "Product": row["Product"],
        "Country": row["Country"],
        "Channel": row["Channel"],
        "Order_Date": row["Order_Date"],
        "Discount_Pct": float(row["Discount_Pct"]),
        "Price_per_Box": float(row["Price_per_Box"]),
        "Marketing_Spend": float(row["Marketing_Spend"]),
        "Boxes_Shipped": int(row["Boxes_Shipped"]),
        "Amount": float(row["Amount"]), 
    }
    
    return pedido

def add_to_index(index, key, order):
    
    """ Va a meter el pedido en la lista de su llave, si esta no existe, enton la crea"""

    val = lp.get(index, key)
    if val is not None:
        val = al.new_list()
        lp.put(index, key, val)
    al.add_last(val, order)
    
def sort_crit_load(a, b):
    
    """Vamos a ordenar, entonces lo ordenamos de Amount descencendente, y si empatan entonces order id ascendente."""

    if a["Amount"] != b["Amount"]:
        return a["Amount"] > b["Amount"]
    return a["Order_ID"] != b["Order_ID"]

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    
    start = get_time()
    viejo = None
    nuevo = None
    
    file = open(filename, encoding="utf-8")
    reader = csv.DictReader(file)
    
    for row in reader:
        order = build_order(row)
        date = order["Order_Date"]
        
        al.add_last(catalog["orders"], order)
        add_to_index(catalog["order_by_month"], date[:7], order)
        add_to_index(catalog["order_by_country"], order["Country"], order)
        add_to_index(catalog["order_by_date"], date, order)
        add_to_index(catalog["order_by_prod_country"], order["Product"] + order["Country"], order)
        add_to_index(catalog["order_by_product"], order["Product"], order)
        
        cuenta = lp.get(catalog["orders_by_channel"], order["Channel"])
        if cuenta is None:
            lp.put(catalog["orders_by_channel"], order["Channel"], 1)
        else:
            lp.put(catalog["orders_by_channel"], order["Channel"], cuenta +1)
        
        if viejo is None or date < viejo:
            viejo = date
        if nuevo is None or date > nuevo:
            nuevo = date
    file.close()
    
    al.merge_sort(catalog["orders"], sort_crit_load)
    end = get_time()
    
    return {
        "time": delta_time(start, end),
        "total": al.size(catalog["orders"]),
        "oldest": viejo,
        "newest": nuevo,
    }
            
        
# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
