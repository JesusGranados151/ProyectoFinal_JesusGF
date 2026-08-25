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
    cantidad = int(input("Ingrese cantidad"))
    Producto = {
      "nombre" : nombre,
      "cantidad" : cantidad, }
    
    Productos.append(Producto)

    print("Producto agregado")

  elif opcion == "2":
    print("STOCK:")
    if len(Productos) == 0:
      print("Productos no encontrados")
    else:
      for Producto in Productos:
        print (f"{Producto['nombre']}: {Producto['cantidad']}")