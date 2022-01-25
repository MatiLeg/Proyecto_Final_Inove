import csv

def autenticacion():

    try:
        with open('usuarios.csv') as auth:
            auth = list(csv.DictReader(auth))
        
            print("Por favor autentiquese a continuacion:")
   
        usuario_ingresado = input('Usuario: ')

        usuario_ingresado_ToF = False

        while usuario_ingresado_ToF == False:

            for i in range(len(auth)):
                user = auth[i]
                for k,v in user.items():
                    if v == usuario_ingresado:
                        usuario_ingresado_ToF = True

            if usuario_ingresado_ToF == False:
                print("Usuario invalido, vuelve a intentarlo.")
                usuario_ingresado = input('Usuario: ')

        return usuario_ingresado

    except:
        return "error"


def agregar_usuario():

    header = ["user"]
    csvfile = open('usuarios.csv', 'a')
    writer = csv.DictWriter(csvfile, fieldnames=header)

    usuario_nuevo = input("Usuario nuevo: ")
    lista_usuariosnuevos = {'user': usuario_nuevo}
    writer.writerow(lista_usuariosnuevos)
    csvfile.close()

def reporte_pedidos():

    with open('pedidos.csv') as pedidos:
        pedidos = list(csv.DictReader(pedidos))

    cantidad_pedidos = len(pedidos)
    precio_total = cantidad_pedidos * 170
    print("Viandas totales: ", cantidad_pedidos)
    print("Total a pagar al proveedor: $", precio_total)

def agregar_pedido(usuario):

    header = ["user", "pedido"]
    csvfile = open('pedidos.csv', 'a')
    writer = csv.DictWriter(csvfile, fieldnames=header)

    pedido = input("Pedido: ")
    lista_pedido = {'user': usuario, 'pedido': pedido}
    writer.writerow(lista_pedido)
    csvfile.close()

    print("Muchas gracias, su pedido fue cargado correctamente.")





if __name__ == '__main__':

    print("SOLICITUD DE PEDIDOS DE VIANDAS")
    
    # Se autentica de que el usuario exista en el CSV
    usuario = autenticacion()
    
    # Verificamos si el usuario es admin o no
    if usuario == "administrador":
        print("Lista de opciones disponibles:")
        print("1. Agregar usuarios")
        print("2. Generar costo total a pagar al proveedor (precio por vianda $170)")
        print("3. Salir")

        opcion1 = input("Opcion: ")

        while opcion1 != "3":
            if opcion1 == "1":
                agregar_usuario()
            elif opcion1 == "2":
                reporte_pedidos()
            opcion1 = input("Opcion: ")

    elif usuario == "error":
        print("No fue posible abrir el archivo 'usuarios.csv'. Por favor informar a IT")

    else:
        print("Lista de opciones disponibles:")
        print("1. Solicitar vianda")
        print("2. Salir")
        opcion2 = input("Opcion: ")
        while opcion2 != "2":
            if opcion2 == "1":
                print("Por favor, a continuación escriba su pedido.")
                agregar_pedido(usuario)
            opcion2 = input("Opcion: ")
    print("Adios.")