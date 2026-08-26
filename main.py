Productos = []
while True:
  print()
  print("Bienvenido a StockHub")
  print()
  print("1. Agregar Producto")
  print("2. Ver Stock")
  print("3. Buscar Producto")
  print("4. Eliminar Producto")
  print("5. Salir")
  opcion = input("Ingrese el número de la acción que desea hacer:")
  print()

  if opcion == "1":
    nombre = input("ingrese el nombre del producto:")
    cantidad = int(input("Ingrese cantidad:"))
    Producto = {
      "nombre" : nombre,
      "cantidad" : cantidad, }

    Productos.append(Producto)

    print("Producto agregado.")

  elif opcion == "2":
    print("STOCK:")
    if len(Productos) == 0:
      print("Productos no encontrados.")
    else:
      for Producto in Productos:
        print (f"{Producto['nombre']}: {Producto['cantidad']}")

  elif opcion == "3":
    nombre = input("Ingrese el producto que desea buscar:")

    encontrado = False

    for Producto in Productos:
      if Producto ["nombre"].lower() == nombre.lower():
        print(f"Producto encontrado: {Producto['nombre']}")
        print(f"Cantidad disponible: {Producto['cantidad']}")
        encontrado = True

        if not encontrado:
          print("Producto no encontrado.")

  elif opcion == "4":
    nombre = input("Ingrese el nombre del producto que desea eliminar:")

    encontrado = False

    for Producto in Productos:
      if Producto ["nombre"].lower() == nombre.lower():
        Productos.remove(Producto)
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
