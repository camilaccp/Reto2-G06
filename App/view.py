import sys
import os
from App import logic
from DataStructures.List import array_list as al
from DataStructures.Map import map_linear_probing as lp

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

data_dir = os.path.dirname(os.path.realpath(__file__)) + "/../Data/"

def print_order(order):
    print(f" {order["Order_ID"]} | {order["Product"]} | {order["Country"]} | {order["Channel"]} |"
          f" {order["Order_Date"]} | Cajas: {order["Boxes_Shipped"]} | "
          f"Precio/Caja: {order["Price_per_Box"]} | Amount: {order["Amount"]} ")


def print_first_last(lista, print_func, limite=20, mostrar=10):
    
    """ Si la lista tiene mas de limite elementos, imprime los primeros y ultimos mostrar elementos, si no imprime todos """
    
    total = al.size(lista)
    if total <= limite:
        for i in range(total):
            print_func(al.get_element(lista, i))
    else:
        print(f"Primeros {mostrar} elementos:")
        for i in range(mostrar):
            print_func(al.get_element(lista, i))
        print(f"\nUltimos {mostrar} elementos:")
        for i in range(total - mostrar, total):
            print_func(al.get_element(lista, i))

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    
    return logic.new_logic()

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    
    print("Archivos: 1) 100 elementos 2) 20% 3) 40% 4) 60% 5) 80% 6) 100%")
    option = input("Escoja el archivo: ")
    nombres = {"1": "100_elementos",
               "2": "20_pct",
               "3": "40_pct",
               "4": "60_pct",
               "5": "80_pct",
               "6": "100_pct",
               }
    
    filename = data_dir + "chocolate_sale_" + nombres[option] + ".csv"
    
    algo = logic.load_data(control, filename)
    orders = control["orders"]
    total = algo["total"]
    
    print(f"\nTiempo de Carga: {algo['time']:.2f} ms")
    print(f"Total de Pedidos: {total}")
    
    print("Pedidos por canal:")
    canales = lp.key_set(control["orders_by_channel"])
    for i in range(al.size(canales)):
        canal = al.get_element(canales, i)
        print(f" {canal}: {lp.get(control['orders_by_channel'], canal)}")
        
    print(f"Fecha más antigua: {algo['oldest']}")
    print(f"Fecha más reciente: {algo['newest']}")
    
    print("\nPedido con Amount mayor:")
    print_order(al.get_element(orders, 0))
    print("Pedido con Amonut menor:")
    print_order(al.get_element(orders, total -1))
    
    print("\nPrimeros 5 pedidos (de mayor a menor Amount):")
    for i in range(min(5, total)):
        print_order(al.get_element(orders, i))
    print("Ultimos 5 pedidos:")
    for i in range(max(0, total-5), total):
        print_order(al.get_element(orders, i))
    


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass

def print_order_req2(order):
    
    print(f" {order['Order_ID']} | {order['Product']} | {order['Channel']} | {order['Order_Date']} |"
            f" Cajas: {order['Boxes_Shipped']} | Precio/Caja: {order['Price_per_Box']} |"
            f" Marketing: {order['Marketing_Spend']} | Amount: {order['Amount']} ")
    
    
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    
    country = input("Ingrese el país: ").strip()
    min_boxes = int(input("Ingrese el número mínimo de cajas: "))
    max_boxes = int(input("Ingrese el número máximo de cajas: "))
    
    respuesta = logic.req_2(control, country, min_boxes, max_boxes)
    
    print(f"\nTiempo de ejecución: {respuesta['time']:.2f} ms")
    print(f"Total de pedidos que cumplieron con el filtro: {respuesta['total']}")
    print(f"Número de productos distintos: {respuesta['distinct_products']}")
    print(f"Promedio de Marketing Spend: {respuesta['avg_marketing']:.2f}")
    print(f"Promedio de Amount: {respuesta['avg_amount']:.2f}")
    if respuesta['top_product'] is not None:
        print(f"Producto con más pedidos: {respuesta['top_product']['product']} ({respuesta['top_product']['count']} pedidos)")
    else:
        print("\nPedidos (Boxes_Shipped ascendente):")
        print_first_last(respuesta['orders'], print_order_req2, limite=20, mostrar=10)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 5:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
