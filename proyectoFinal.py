#Importamos Colorama
from colorama import init, Fore, Back, Style
init(autoreset= True)

#Importamos sqlite3
import sqlite3

# ------------------------------------------------------------------------------------------------------------
# Creación de la base de datos "Inventario"
def inicializar_bd():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nombre TEXT NOT NULL,
                    Descripcion TEXT,
                    Cantidad INTEGER NOT NULL,
                    Precio  REAL,
                    Categoria TEXT)''')
    conexion.commit()
    conexion.close()

# ------------------------------------------------------------------------------------------------------------
def registrar_productos(nombre, descripcion, cantidad, precio, categoria):
    ''' Permite registrar un producto con su nombre, descripción, cantidad, precio y categoria'''
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    query  = '''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()

# ------------------------------------------------------------------------------------------------------------
def mostrar_productos():
    """
    Muestra todos los productos registrados en la base de datos.
    """
    try:
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        query = 'SELECT * FROM productos'
        cursor.execute(query)
        productos = cursor.fetchall()
        conexion.close()

        if productos:
            print("\nProductos Registrados:")
            print("-" * 50)
            for producto in productos:
                id_producto, nombre, descripcion, cantidad, precio, categoria = producto
                print(f"ID: {id_producto}")
                print(f"Nombre: {nombre}")
                print(f"Descripción: {descripcion}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio: ${precio:.2f}")
                print(f"Categoría: {categoria}")
                print("-" * 50)
        else:
            print(Back.RED + Fore.WHITE + "No hay productos registrados en la base de datos.")
    except sqlite3.Error as e:
        print(Back.RED + Fore.WHITE + f"Error al acceder a la base de datos: {e}")

# ------------------------------------------------------------------------------------------------------------
def actualizar_producto(id_producto, nueva_cantidad):
    '''Permite actualizar la cantidad de un producto. '''
    try:
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        query = 'UPDATE productos SET cantidad = ? WHERE id = ?'
        cursor.execute(query, (nueva_cantidad, id_producto))
        conexion.commit()
        conexion.close()

        if cursor.rowcount > 0:
            print(Fore.GREEN + "Cantidad actualizada con éxito.")
        else:
            print(Fore.RED + "No se encontró un producto con el ID especificado.")
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al actualizar la cantidad del producto: {e}")


# ------------------------------------------------------------------------------------------------------------
def eliminar_producto(id_producto):
    '''Permite eliminar un producto indicando su número de ID'''
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    query = '''DELETE FROM productos WHERE id = ?'''
    cursor.execute(query, (id_producto, ))
    conexion.commit()
    conexion.close()

# ------------------------------------------------------------------------------------------------------------
def buscar_producto(termino, campo="nombre"):
    """Permite buscar los productos que esten registrados en la base de datos. El usuario puede buscar por 
    nombre o categoría. """
    try:
        if campo not in ["nombre", "categoria"]:
            print("Error: Campo de búsqueda inválido. Usa 'nombre' o 'categoria'.")
            return
        
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        query = f'SELECT * FROM productos WHERE {campo} LIKE ?'
        cursor.execute(query, (f'%{termino}%',))
        resultados = cursor.fetchall()
        conexion.close()

        if resultados:
            print(f"\nResultados de la búsqueda por {campo}:")
            print("-" * 50)
            for producto in resultados:
                id_producto, nombre, descripcion, cantidad, precio, categoria = producto
                print(f"ID: {id_producto}")
                print(f"Nombre: {nombre}")
                print(f"Descripción: {descripcion}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio: ${precio:.2f}")
                print(f"Categoría: {categoria}")
                print("-" * 50)
        else:
            print(Back.RED + Fore.WHITE + f"No se encontraron productos que coincidan con '{termino}' en el campo '{campo}'.")
    except sqlite3.Error as e:
        print(Back.RED + Fore.WHITE + f"Error al buscar productos en la base de datos: {e}")

# ------------------------------------------------------------------------------------------------------------
def reporte_bajo_stock(limite):
    """
    Genera un reporte de los productos con stock igual o menor al límite especificado.
    """
    try:
        conexion = sqlite3.connect('inventario.db')
        cursor = conexion.cursor()
        query = 'SELECT * FROM productos WHERE cantidad <= ?'
        cursor.execute(query, (limite,))
        resultados = cursor.fetchall()
        conexion.close()

        if resultados:
            print("\nReporte de productos con bajo stock:")
            print("-" * 70)
            print(f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 70)
            for producto in resultados:
                id_producto, nombre, descripcion, cantidad, precio, categoria = producto
                print(f"{id_producto:<5} {nombre:<20} {cantidad:<10} ${precio:<10.2f} {categoria:<15}")
            print("-" * 70)
        else:
            print(f"No hay productos con stock igual o menor a {limite}.")
    except sqlite3.Error as e:
        print(Back.RED + Fore.WHITE + f"Error al generar el reporte de bajo stock: {e}")

# ------------------------------------------------------------------------------------------------------------
def menu_interactivo():
    while True:
        print(Style.BRIGHT + Fore.BLUE + Back.WHITE + "Menú de Inventario")
        print(Style.BRIGHT + Fore.CYAN + "1. Registrar producto")
        print(Style.BRIGHT + Fore.CYAN + "2. Actualizar producto")
        print(Style.BRIGHT + Fore.CYAN + "3. Eliminar producto")
        print(Style.BRIGHT + Fore.CYAN + "4. Buscar producto")
        print(Style.BRIGHT + Fore.CYAN + "5. Generar reporte bajo stock")
        print(Style.BRIGHT + Fore.CYAN + "6. Mostrar productos")
        print(Style.BRIGHT + Fore.RED + "7. Salir")
        
        opcion = int(input("\nIngrese opción: "))
        
        if opcion == 1:
            nombre = input("Nombre: ")
            #validar input
            descripcion = input("Descripcion: ")
            cantidad = int(input("Cantidad: "))
            #validar tipo de dato para no crashear
            precio = float(input("Precio: "))
            #muestro diccionario y 
            categoria = input("Ingrese nombre de Categoría: ")
            #valido que el input coincida con el valor (consistencia)
            registrar_productos(nombre, descripcion, cantidad, precio, categoria)
            print(Fore.GREEN + "Producto registrado con éxito!")
            
        elif opcion == 2:
            try:
                id_producto = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                actualizar_producto(id_producto, nueva_cantidad)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")

        elif opcion == 3:
            id_producto = int(input("Ingrese ID del producto a eliminar: "))
            #agrego funcionalidad para verificar la existencia del producto   
            eliminar_producto(id_producto)
            print(Fore.GREEN + "Producto eliminado con éxito!")
            
        elif opcion == 4:
            print("\nBúsqueda de productos")
            print("1. Buscar por nombre")
            print("2. Buscar por categoría")
            opcion_busqueda = int(input("Ingrese una opción: "))
            
            if opcion_busqueda == 1:
                termino = input("Ingrese el nombre del producto a buscar: ")
                buscar_producto(termino, campo="nombre")
            elif opcion_busqueda == 2:
                termino = input("Ingrese la categoría del producto a buscar: ")
                buscar_producto(termino, campo="categoria")
            else:
                print(Back.RED + Fore.WHITE + "Opción inválida.")
        
        elif opcion == 5:
            try:
                limite = int(input("Ingrese el límite de stock: "))
                reporte_bajo_stock(limite)
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == 6:
            mostrar_productos()

                
        elif opcion == 7:
            print(Fore.RED + "Saliendo del programa !")
            break
            
        else:
            print("Ingrese opción válida!")   
            


if __name__ == "__main__":
    inicializar_bd()
    menu_interactivo()
