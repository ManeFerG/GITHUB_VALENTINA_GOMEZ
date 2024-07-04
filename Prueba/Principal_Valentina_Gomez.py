import funciones_valentina_gomez as fn
listanombre={}
listadireccion={}
listahospital={}
listainsumos={}
listabono={}
listatotal={}



while(True):
    print("1.-Registrar Cobro")
    print("2.-Lista Cobros Registrados")
    print("3.-Definir Sector Despacho")
    print("4.-Salir del Programa")
    opcion=int(input("Ingrese su opcion 1-4: "))

    if opcion==1:
        fn.registro(listanombre,listadireccion,listahospital,listainsumos,listabono,listatotal)

    if opcion==2:
        fn.cobros(listanombre,listadireccion,listahospital,listainsumos,listabono,listatotal)

    if opcion==3:
        print()

    if opcion==4:
        break
