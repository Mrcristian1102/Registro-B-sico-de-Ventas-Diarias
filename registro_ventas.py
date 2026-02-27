cliente = input("Nombre del cliente: ")
precio = float(input("Precio unitario del producto: "))
cantidad = int(input("Cantidad de productos comprados: "))
cliente_VIP = input("El cliente tiene membresia VIP (si/no)")

valor = precio * cantidad

if cliente_VIP == "si":
    descuento = valor * 0.10
else:
    descuento = 0.0

total = valor - descuento

print ("-------RESUMEN DE VETA-------")
print (f"cliente: {cliente}")
print (f"precio: $ {precio}")
print (f"cantidad: {cantidad}")
print (f"descuento aplicado: $ {descuento}")
print (f"total a pagar: $ {total}")