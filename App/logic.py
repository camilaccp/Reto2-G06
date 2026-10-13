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

def prod_country_key(product, country):
    """ 
    LLave del indice Producto-Pais, el separador va a evitar choques como "AB" +"C" == "A" + "BC" """
    return product + "|" + country

def ordenar(lista, sort_crit):
    """
    Ordena la lista según el criterio de ordenamiento dado.
    """
    resultado = al.merge_sort(lista, sort_crit)
    if resultado is None:
        resultado = lista
    return resultado

def sort_crit_load(a, b):
    
    """Vamos a ordenar, entonces lo ordenamos de Amount descencendente, y si empatan entonces order id ascendente."""

    if a["Amount"] != b["Amount"]:
        return a["Amount"] > b["Amount"]
    return a["Order_ID"] < b["Order_ID"]

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
        add_to_index(catalog["order_by_prod_country"], prod_country_key(order["Product"], order["Country"]), order)
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
    
    catalog["orders"] = ordenar(catalog["orders"], sort_crit_load)
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

def sort_crit_req2(a, b):
    """Vamos a ordenar, entonces lo ordenamos de Boxes_Shipped ascendente, y si empatan entonces order date descendente, y luego order_id ascendente."""

    if a["Boxes_Shipped"] != b["Boxes_Shipped"]:
        return a["Boxes_Shipped"] < b["Boxes_Shipped"]
    if a["Order_Date"] != b["Order_Date"]:
        return a["Order_Date"] > b["Order_Date"]
    return a["Order_ID"] < b["Order_ID"]

def req_2(catalog, country, min_boxes, max_boxes):
    """
    Retorna el resultado del requerimiento 2
    
    1. Con orders_by_country, obtenemos la lista de pedidos de ese pais
    2. filtramos la lista por el rango de cajas incluyendo extremos
    3. con un mapa producto -> obtenemos en numero de pedidos, saco los prodiuctos distintos y el producto con mas pedidos
    4. ordenamos los filtrados con merge_sort.
    """
    # TODO: Modificar el requerimiento 2
    
    start = get_time()
    
    filtrados = al.new_list()
    conteo_productos = lp.new_map(20, 0.5)
    suma_marketing = 0
    suma_amount = 0
    
    pedidos_pais = lp.get(catalog["orders_by_country"], country) 
    if pedidos_pais is not None:
        for i in range(al.size(pedidos_pais)):
            pedido = al.get_element(pedidos_pais, i)
            if min_boxes <= pedido["Boxes_Shipped"] <= max_boxes:
                al.add_last(filtrados, pedido)
                suma_marketing += pedido["Marketing_Spend"]
                suma_amount += pedido["Amount"]
                
                conteo = lp.get(conteo_productos, pedido["Product"])
                if conteo is None:
                    lp.put(conteo_productos, pedido["Product"], 1)
                else:
                    lp.put(conteo_productos, pedido["Product"], conteo + 1)
    
    total = al.size(filtrados)
    
    # Obtenemos el producto con mas pedidos
    producto_top = None
    pedidos_top = 0
    productos = lp.key_set(conteo_productos)
    
    for i in range(al.size(productos)):
        producto = al.get_element(productos, i)
        cuenta = lp.get(conteo_productos, producto)
        if cuenta > pedidos_top or (cuenta == pedidos_top and producto < producto_top):
            producto_top = producto
            pedidos_top = cuenta
            
    if total > 0:
        filtrados = ordenar(filtrados, sort_crit_req2)
        promedio_marketing = suma_marketing / total
        promedio_amount = suma_amount / total
    else:
        promedio_marketing = 0
        promedio_amount = 0
    
    end = get_time()
    
    return { 
            "time": delta_time(start, end),
            "total": total,
            "num_products": lp.size(conteo_productos),
            "average_marketing": promedio_marketing,
            "average_amount": promedio_amount,
            "top_product": producto_top,
            "top_product_orders": pedidos_top,
            "orders": filtrados,
    }
            
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

def sort_crit_req5(a, b):
    
    """ Recaudo descendente, luego total de cajas descendente, luego nombre ascendente """
    
    if a["total_amount"] != b["total_amount"]:
        return a["total_amount"] > b["total_amount"]
    if a["total_boxes"] != b["total_boxes"]:
        return a["total_boxes"] > b["total_boxes"]
    return a["product"] < b["product"]
    

def req_5(catalog, n, country, start_date, end_date):
    """
    Retorna el resultado del requerimiento 5
    
    1. con orders_by_country obtenemos la lista de pedidos de ese pais
    2. filtro por fecha incluimos extremos, las fechas YYYY-MM-DD se comparan como texto
    3. agrupamos en un mapa producto _> registro los acumulados
    4. paso los registros a una lista y la ordeno con merge_sort y cojo los n primeros
    
    
    """
    # TODO: Modificar el requerimiento 5
    
    start = get_time()
    por_producto = lp.new_map(20, 0.5)
    total_pedidos = 0
    recaudo_total = 0 
    
    pedidos_pais = lp.get(catalog["orders_by_country"], country)
    if pedidos_pais is not None:
        for i in range(al.size(pedidos_pais)):
            pedido = al.get_element(pedidos_pais, i)
            if start_date <= pedido["Order_Date"] <= end_date:
                total_pedidos += 1
                recaudo_total += pedido["Amount"]
                
                registro = lp.get(por_producto, pedido["Product"])
                if registro is None:
                    registro = {
                        "Product": pedido["Product"],
                        "num_orders": 0,
                        "total_amount": 0,
                        "total_boxes": 0,
                        "sum_price": 0,
                        "sum_discount": 0,
                        "total_marketing": 0,
                    }
                    lp.put(por_producto, pedido["Product"], registro)
        
                registro["num_orders"] += 1
                registro["total_amount"] += pedido["Amount"]                    
                registro["total_boxes"] += pedido["Boxes_Shipped"]
                registro["sum_price"] += pedido["Price_per_Box"]
                registro["sum_discount"] += pedido["Discount_Pct"]
                registro["total_marketing"] += pedido["Marketing_Spend"]
        
    productos = lp.value_set(por_producto)
    for i in range(al.size(productos)):
        registro = al.get_element(productos, i)
        registro["avg_price"] = registro["sum_price"] / registro["num_orders"]
        registro["avg_discount"] = registro["sum_discount"] / registro["num_orders"]
    
    num_productos = al.size(productos)
    if num_productos > 0:
        productos = ordenar(productos, sort_crit_req5)
    
    top = al.new_list()
    for i in range(min(n, num_productos)):
        al.add_last(top, al.get_element(productos, i))
    
    end = get_time()
    
    return {
        "time": delta_time(start, end),
        "total_orders": total_pedidos,
        "total_amount": recaudo_total,
        "num_products": num_productos,
        "top_products": top,
    }
                

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
