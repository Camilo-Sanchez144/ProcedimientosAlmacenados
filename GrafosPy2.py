import mysql.connector

# Conexión a la base de datos
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="grafos"
    )

# Crear un nodo
def crear_nodo(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.callproc('CrearNodo', [nombre])
    conexion.commit()
    cursor.close()
    conexion.close()

# Crear una arista
def crear_arista(origen, destino):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.callproc('CrearArista', [origen, destino])
    conexion.commit()
    cursor.close()
    conexion.close()

# Leer conexiones de un nodo
def leer_conexiones(ciudad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.callproc('LeerConexiones', [ciudad])
    for resultado in cursor.stored_results():
        print(f"Conexiones de {ciudad}:")
        for fila in resultado.fetchall():
            print(f"- {fila[0]}")
    cursor.close()
    conexion.close()

# Actualizar una conexión
def actualizar_conexion(origen, conexion_antigua, nueva_conexion):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.callproc('ActualizarConexion', [origen, conexion_antigua, nueva_conexion])
    conexion.commit()
    cursor.close()
    conexion.close()

# Eliminar un nodo
def eliminar_nodo(ciudad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.callproc('EliminarNodo', [ciudad])
    conexion.commit()
    cursor.close()
    conexion.close()

# Menú de opciones
def menu():
    while True:
        print("\n========= Menú =========")
        print("1. Crear nodo")
        print("2. Crear arista")
        print("3. Leer conexiones")
        print("4. Actualizar conexión")
        print("5. Eliminar nodo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del nodo: ")
            crear_nodo(nombre)
        elif opcion == "2":
            origen = input("Ingrese el nodo origen: ")
            destino = input("Ingrese el nodo destino: ")
            crear_arista(origen, destino)
        elif opcion == "3":
            ciudad = input("Ingrese el nombre del nodo: ")
            leer_conexiones(ciudad)
        elif opcion == "4":
            origen = input("Ingrese el nodo origen: ")
            conexion_antigua = input("Ingrese la conexión antigua: ")
            nueva_conexion = input("Ingrese la nueva conexión: ")
            actualizar_conexion(origen, conexion_antigua, nueva_conexion)
        elif opcion == "5":
            ciudad = input("Ingrese el nombre del nodo a eliminar: ")
            eliminar_nodo(ciudad)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar la aplicación
menu()
