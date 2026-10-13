#UN CAMBIO DE PRUEBA 

monto_total_diario = 0.0
caja_abierta = True

while caja_abierta:
    print("0. MENU PRINCIPAL.")
    print("1. REGISTRAR VENTA.")
    print("2. VER TOTAL ACUMULADO DEL DIA.")
    print("3. CERRAR CAJA Y SALIR.")

    opcion = int(input("Ingrese una opción: "))

    if(opcion == 1):
        print("REGISTRAR VENTA: ")
        subtotal_cliente = 0
        registro_de_venta = True

        while registro_de_venta:
            precio = input("Ingrese el precio de cada producto adquirido: ")
            if precio == ("0") or precio == ("fin"):
                registro_de_venta = False
            else:
                precio = float(precio)
                subtotal_cliente = subtotal_cliente + precio
        
        monto_iva = subtotal_cliente * 0.19
        total_iva_cliente = subtotal_cliente + monto_iva
        print("---BOLETA---")
        print("El sub total del cliente es: ", subtotal_cliente)
        print("Monto iva: ", monto_iva)
        print ("El monto total del cliente con iva es: ", total_iva_cliente)


        print("¿Ingrese el metodo de pago: ")
        print("1 Efectivo" , "2 Tarjeta")
        metodo_de_pago = input()

        descuento = 0.0
        if metodo_de_pago == "1":
            descuento = total_iva_cliente * 0.05
            print("Se aplico un descuento del 5% por metodo de pago.")

        total_final_cliente = total_iva_cliente - descuento
        print("Monto final es: ", total_final_cliente)

        if total_final_cliente > 15.000:
            print ("Venta alta")
        else:
            print("Venta habitual")

    if(opcion == 2):
        print("VER TOTAL ACUMULADO DEL DIA.")
        

    if(opcion == 3):
        print("CERRAR CAJA Y SALIR.")
        caja_abierta = False



