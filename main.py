productos = []


# Función para ver el stock
def ver_stock(productos):
    print("--- STOCK ---")
    print()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("---------------------")


while True:
    print()
    print("---------------------")
    print("   Bienvenido a StockHub")
    print("---------------------")
    print("1. Agregar Producto")
    print("2. Ver Stock")
    print("3. Buscar Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    print()

    opcion = input("Ingrese el número de la acción que desea ejecutar: ")
    print()

    # AGREGAR PRODUCTO
    if opcion == "1":

        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre == "":
            print("El nombre del producto no puede estar vacío.")
            continue

        try:
            cantidad = int(input("Ingrese cantidad: "))

            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        producto = {
            "nombre": nombre,
            "cantidad": cantidad
        }

        productos.append(producto)

        print("Producto agregado correctamente.")

    # VER STOCK
    elif opcion == "2":
        ver_stock(productos)

    # BUSCAR PRODUCTO
    elif opcion == "3":

        if len(productos) == 0:
            print("No hay productos registrados.")
            continue

        nombre = input("Ingrese el producto que desea buscar: ").strip()

        encontrado = False

        for producto in productos:

            if producto["nombre"].lower() == nombre.lower():
                print()
                print("Producto encontrado:")
                print(f"Nombre: {producto['nombre']}")
                print(f"Cantidad disponible: {producto['cantidad']}")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")

    # ELIMINAR PRODUCTO
    elif opcion == "4":

        if len(productos) == 0:
            print("No hay productos registrados.")
            continue

        nombre = input("Ingrese el nombre del producto que desea eliminar: ").strip()

        encontrado = False

        for producto in productos:

            if producto["nombre"].lower() == nombre.lower():
                productos.remove(producto)
                print("Producto eliminado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado.")

    # SALIR
    elif opcion == "5":
        print("Gracias por utilizar StockHub.")
        break

    # OPCIÓN INCORRECTA
    else:
        print("Opción no válida. Intente nuevamente.")
