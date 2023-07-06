import funciones_restaurant as fn

while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
        fn.ver_restaurant()
    elif opcion==2:
        fn.reservar()
    elif opcion==3:
        fn.ver_carta()
    elif opcion==4:
        fn.pagar()
    elif opcion==5:
        fn.cancelar_reserva()
    else:
        print("GRACIAS, ADIOS!")
        break