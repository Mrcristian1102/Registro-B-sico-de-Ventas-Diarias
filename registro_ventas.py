while True:
    cliente = input("Nombre del cliente: ")
    precio = float(input("Precio unitario del producto: "))
    cantidad = int(input("Cantidad de productos comprados: "))
    cliente_VIP = input("El cliente tiene membresía VIP (si/no): ").lower()

    valor = precio * cantidad

    if cliente_VIP == "si":
        descuento = valor * 0.10
    else:
        descuento = 0.0

    total = valor - descuento

    print("\n---RESUMEN DE VENTA")
    print(f"Cliente: {cliente}")
    print(f"Subtotal: $ {valor}")
    print(f"Descuento aplicado: $ {descuento}")
    print(f"Total a pagar: $ {total}")

    continuar = input("\n¿Desea registrar otra venta? (si/no): ").lower()
    
    if continuar != "si":
        print("Muchas gracias.")
        break