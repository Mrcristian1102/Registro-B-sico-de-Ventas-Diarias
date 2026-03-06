while True:   #la condición siempre sera verdadera
    cliente = input("Nombre del cliente: ")
    
    try:   #Se usa para manejar errores, si ocurre un error, pasará al except
        precio = float(input("Precio unitario del producto: "))
        cantidad = int(input("Cantidad de productos comprados: "))
    except ValueError:   #Si el usuario escribe algo incorrecto por ejemplo ( letras en vez de numeros ) ocurre un ValueError
        print("Escribe un número, no una letra.")
        continue   #Hace que el ciclo vuelva a empezar, el programa vuelve al while true

    cliente_VIP = input("El cliente tiene membresía VIP (si/no): ").lower()

    valor = precio * cantidad

    if cliente_VIP == "si":
        descuento = valor * 0.10
    else:
        descuento = 0.0

    total = valor - descuento

    print("---RESUMEN DE VENTA")
    print(f"Cliente: {cliente}")
    print(f"Subtotal: $ {valor}")
    print(f"Descuento aplicado: $ {descuento}")
    print(f"Total a pagar: $ {total}")

    continuar = input("\n¿Desea registrar otra venta? (si/no): ").lower()   #Pregunta si quiere registrar otra venta (\n)=crea una linea en blanco antes del texto (.lower())= convierte todo en minuscula
    
    if continuar != "si":   #!= significa diferente de, si la respuesta no es (si), se ejecuta lo siguiente
        print("Muchas gracias.")
        break   #Rompe el ciclo del  while, el programa termina