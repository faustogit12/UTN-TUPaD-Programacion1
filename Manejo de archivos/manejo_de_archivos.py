import os

nombre_del_archivo = "productos.txt"

def crear_archivo_inicial():
    # productos.txt con 3 productos

    if not os.path.exists(nombre_del_archivo):
        ejemplo = [
            "Lapicera,120.5,30\n",
            "Cuaderno,350.0,50\n",
            "Mochila,4500.75,10\n"
        ]
        with open(nombre_del_archivo, "w", encoding="utf-8") as f:
            f.writelines(ejemplo)
        print(f"Se creó '{nombre_del_archivo}' con 3 productos de ejemplo.\n")

def leer_productos():
    #Lee el archivo y devuelve una lista de diccionarios [{nombre, precio, cantidad}
    productos = []
    try:
        with open(nombre_del_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                if len(partes) != 3:
                    print(f"Aviso: línea ignorada (formato inválido): {linea}")
                    continue
                nombre = partes[0].strip()
                try:
                    precio = float(partes[1].strip())
                except ValueError:
                    print(f"Aviso: precio inválido en '{linea}', se usa 0.0")
                    precio = 0.0
                try:
                    cantidad = int(float(partes[2].strip()))
                except ValueError:
                    print(f"Aviso: cantidad inválida en '{linea}', se usa 0")
                    cantidad = 0
                productos.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })
    except FileNotFoundError:
        print(f"Aviso: '{nombre_del_archivo}' no encontrado. Se creará al guardar.")
    return productos

def mostrar_productos(productos):
    """Muestra en pantalla la lista de productos en el formato pedido."""
    if not productos:
        print("No hay productos para mostrar.\n")
        return
    print("Productos en archivo:")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print()

def agregar_producto_interactivo(productos):

    # Pide al usuario un nuevo producto y lo agrega

    print("Agregar productos (deja vacío el nombre para terminar).")
    while True:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            break
        precio_input = input("Precio (ej: 120.5): ").strip()
        cantidad_input = input("Cantidad (ej: 30): ").strip()
        try:
            precio = float(precio_input)
        except ValueError:
            print("Precio inválido, se asigna 0.0.")
            precio = 0.0
        try:
            cantidad = int(float(cantidad_input))
        except ValueError:
            print("Cantidad inválida, se asigna 0.")
            cantidad = 0

        linea = f"{nombre},{precio},{cantidad}\n"
        try:
            with open(nombre_del_archivo, "a", encoding="utf-8") as f:
                f.write(linea)
        except Exception as e:
            print(f"No se pudo escribir en {nombre_del_archivo}: {e}")
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto '{nombre}' agregado.\n")

def buscar_producto(productos):

    #Pide un nombre y busca (case-insensitive) en la lista.

    if not productos:
        print("No hay productos para buscar.\n")
        return
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    if not nombre_buscar:
        print("Búsqueda cancelada.\n")
        return
    nombre_buscar_lower = nombre_buscar.lower()
    encontrados = [p for p in productos if p['nombre'].lower() == nombre_buscar_lower]
    if encontrados:
        for p in encontrados:
            print("Producto encontrado:")
            print(f"  Nombre: {p['nombre']}")
            print(f"  Precio: ${p['precio']}")
            print(f"  Cantidad: {p['cantidad']}\n")
    else:
        print(f"Error: el producto '{nombre_buscar}' no existe.\n")

def guardar_productos_sobrescribiendo(productos):
    #Sobrescribe productos.txt con los productos de la lista.
    try:
        with open(nombre_del_archivo, "w", encoding="utf-8") as f:
            for p in productos:
                f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
        print(f"'{nombre_del_archivo}' sobrescrito con {len(productos)} productos.\n")
    except Exception as e:
        print(f"No se pudo guardar en {nombre_del_archivo}: {e}")

def main():
    crear_archivo_inicial()
    productos = leer_productos()
    mostrar_productos(productos)
    agregar_producto_interactivo(productos)
    mostrar_productos(productos)
    buscar_producto(productos)
    guardar_productos_sobrescribiendo(productos)
    print("Fin del programa.")

    input("Presioná ENTER para salir...")

if __name__ == "__main__":
    main()