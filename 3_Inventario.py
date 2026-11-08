print("\n--- SOFTWARE INVENTARIO ---\n")

inventario = []

while True:

    print("Escoge una de las siguientes opciones: ")
    print("1.Agregar producto")
    print("2.Agregar lote de productos")
    print("3.Eliminar producto del inventario")
    print("4.Eliminar producto del inventario mas reciente")
    print("5.Ordenar productos alfabeticamente")
    print("6.Mostar numero total de productos")
    print("7.Salir\n")

    opcion = int(input("Escoge una accion del MENU que desees realizar: "))

    if opcion == 1:

        agregar_producto = input("\nIngresa el producto que deseas agregar: ")
        inventario.append(agregar_producto)
        print(f"Producto {agregar_producto} agregado satisfactoriamente")
        print("Seras redireccionado nuevamente al menu\n")
        print(f"Tu inventario actual:{inventario}")

    elif opcion ==2:

        agregar_lote_productos = input("Ingresa los productos que deseas agregar separados por una coma: ")
        nuevos_productos = [producto.strip() for producto in agregar_lote_productos.split(",")]
        inventario.extend(nuevos_productos)
        print(f"Productos ({agregar_lote_productos}) agregados satisfactoriamente")
        print("Seras redireccionado nuevamente al menu\n")

    elif opcion ==3:

        eliminar_producto = input("Escoge el producto que deseas eliminar: ")

        if eliminar_producto in inventario:
            inventario.remove(eliminar_producto)
            print(f"El producto {eliminar_producto}, ha sido eliminado del inventario")
            print(f"Tu inventario actual:{inventario}")
            print("Seras redireccionado nuevamente al menu\n")
        else:
            print(f"\nEl producto {eliminar_producto} ,que deseas eliminar no esta en el inventario")
            print("Seras redireccionado nuevamente al menu, puedes agregarlo o elegir un producto que este en el inventario\n")


    elif opcion ==4:

        print("\nEscogiste la opcion #4 por lo cual se borrara el producto mas reciente")
        if len(inventario)>0:
            producto_eliminado = inventario.pop()
            print(f"El producto mas reciente es ({producto_eliminado}) y se ha borrado con exito\n")
            print(f"Tu inventario actual:{inventario}")
        else:
            print("El inventario esta vacio, debes tener productos en el inventario para poder eliminar")
            print("Seras redireccionado nuevamente al menu\n")

    elif opcion ==5:

        print("\nEscogiste la opcion #5 por lo cual los productos se ordenaran por orden alfabetico")
        if len(inventario) >0:
            inventario.sort()
            print("\nInventario ordenado alfabeticamente con exito")
            print(f"Tu inventario ordenado es:{inventario}")
            print("Seras redireccionado nuevamente al menu\n")

        else:
            print("El inventario esta vacio, debes tener productos en el inventario para poder ordenarlos")
            print("Seras redireccionado nuevamente al menu\n")

    elif opcion == 6:

        print("\nEscogiste la opcion #6")
        cantidad = len(inventario)
        print(f"El numero total de productos es: {cantidad}\n")

    elif opcion == 7:
        print("\nEscogiste la opcion #7, por lo cual se cierra el programa")
        print("!!Nos vemos pronto!!\n")
        break
    else:
        print("\nEscoge una opcion valida del menu\n")
