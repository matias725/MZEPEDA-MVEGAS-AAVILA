from Presentacion.menus import menuPrincipal,ingresarDatos,mostrar,modificarCliente,eliminarCliente
while(True):
    menuPrincipal()
    op=int(input("Ingrese una Opción: "))
    if op==1:
        ingresarDatos()
    elif op==2:
        mostrar()
    elif op==3:
        modificarCliente()
    if op==4:
        eliminarCliente()
    if op==5:
        op2=input("Desea Salir [Si/No]: ")
        if op2.upper()=="SI":
            exit()
    else:
        print("La opción ingresada está fuera de Rango :( .....")

