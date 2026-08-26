productos = []
while True:
  print()
  print("Bienvenido a StockHub")
  print()
  print("1. Agregar Producto")
  print("2. Ver Stock")
  print("3. Buscar Producto")
  print("4. Eliminar Producto")
  print("5. Salir")
  print()

  opcion = input("Ingrese el número de la acción que desea hacer: ")
  print()

  if opcion == "1":
    nombre = input("ingrese el nombre del producto: ")
    print()
    cantidad = int(input("Ingrese cantidad: "))
    producto = {
      "nombre" : nombre,
      "cantidad" : cantidad, }

    productos.append(producto)

    print("Producto agregado.")

  elif opcion == "2":
    print("---STOCK---")
    print()

    if len(productos) == 0:
      print("Productos no encontrados.")
    else:
      for Producto in productos:
        print (f"{Producto['nombre']}: {Producto['cantidad']}")

  elif opcion == "3":
    nombre = input("Ingrese el producto que desea buscar: ")
    print()

    encontrado = False

    for Producto in productos:
      if Producto ["nombre"].lower() == nombre.lower():
        print(f"Producto encontrado: {Producto['nombre']}")
        print(f"Cantidad disponible: {Producto['cantidad']}")
        encontrado = True

    if not encontrado:
      print("Producto no encontrado.")

  elif opcion == "4":
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    print()

    encontrado = False

    for Producto in productos:
      if producto ["nombre"].lower() == nombre.lower():
        productos.remove(Producto)
        print("Producto Eliminado.")
        encontrado = True
        break
    if not encontrado:
      print("Producto no encontrado.")
  elif opcion == "5":
    print("Gracias por utilizar el programa.")
    break
  else:
    print("Opción no válida,intente nuevamente.")
