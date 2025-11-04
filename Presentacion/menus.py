import os
#import Persistencia.DAO.CRUDCliente
from Persistencia.DAO.CRUDCliente import mostrarTodosTiposUsuarios,agregar,mostrarTodos,consultaParticular,consultaParcial,eliminar,editar
from Dominio.DTO.Cliente import Cliente
#Construimos las funciones para los MEnus
def menuPrincipal():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("            Menu Principal")
    print("***************************************")
    print("      1. (C) Ingresar")
    print("      2. (R) Mostrar")
    print("      3. (U) Actualizar")
    print("      4. (D) Eliminar")
    print("      5. (E) Salir")
    print("***************************************")

def mostrarMenus():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("            Menú Mostrar")
    print("***************************************")
    print("      1. Mostrar Todos")
    print("      2. Mostrar Uno")
    print("      3. Mostrar Parcial")
    print("      4. Volver")
    print("***************************************")

def ingresarDatos():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("        Ingresar DAtos Cliente")
    print("***************************************")
    #Solicitamos los datos del cliente
    run=input("Ingrese su RUN: ")
    nombre=input("Ingrese su Nombre: ")
    apellidos=input("Ingrese su Apellido: ")
    direccion=input("Ingrese su Dirección: ")
    fono=int(input("Ingrese su N° Telefónio: "))
    correo=input("Ingrese su Correo: ")
    #Solicitar el tipo de Usuario
    #Solicitaremos que se traigan los datos de la tabla Tipo_Usuario
    datos=mostrarTodosTiposUsuarios()
    #Iteramos a Datos para recorrer el contenido
    print("****** Tipos de Usuarios ********")
    print("Id Usuario\t\tDescripción")
    for dato in datos:
        print("{}\t\t{}".format(dato[0],dato[1]))

    print("*********************************")
    tipo_usuario=int(input("Ingrese el Id Tipo de Usuario: "))
    monto=int(input("Ingrese Monto: $"))
    #Crear el Objeto de Tipo Cliente
    cliente1=Cliente(run,nombre,apellidos,direccion,fono,correo,tipo_usuario,monto)
    #Ahora solicitaremos el ingreso de los datos a la BD
    agregar(cliente1)

#Función para Mostrar todos los registros
def mostrarTodosClientes():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("       Mostrar Todos los Cliente")
    print("***************************************")
    #Solicitar el envío de todos los registros
    datos=mostrarTodos()
    #Iterar a Datos para mostrar la información de cada registro
    print("Id Cliente\tRUN\tNombre\tApellidos\tDirección\tFono\tCorreo\tMonto Credito\tDeuda\tTipo Usuario")
    for dato in datos:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],
                                                              dato[6],dato[7],dato[8],dato[9]))
    print("*************************Fin de los Registros*************************************")

#Función para mostrar Un Registro
def mostrarUnClientes():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("       Datos del Cliente")
    print("***************************************")
    #Cargar a todos los cllientes existentes
    mostrarTodosClientes()
    id_cliente=int(input("Ingrese el Id del Cliente a consultar: "))
    dato=consultaParticular(id_cliente)
    datosTipoCliente=mostrarTodosTiposUsuarios()   

    #Mostrar el contenido del registro rescatado
    print("ID Cliente           :{}".format(dato[0]))
    print("RUN Cliente          :{}".format(dato[1]))
    print("Nombre Cliente       :{}".format(dato[2]))
    print("Apellidos Cliente    :{}".format(dato[3]))
    print("Dirección Cliente    :{}".format(dato[4]))
    print("Fono Cliente         :{}".format(dato[5]))
    print("Correo Cliente       :{}".format(dato[6]))
    #for d in datosTipoCliente():
    #    if dato[9]==d[0]:
    #        print("Tipo Cliente         :{}".format(d[1]))
    print("Tipo Cliente         :{}".format(dato[9]))
    print("Monto Crédito        :${}".format(dato[7]))
    print("Deuda                :${}".format(dato[8]))
    print("************* Fin Registro ****************")    
    input("Presione enter para continuar.....")


#Función para mostrar Parcial o parte de los registros
def mostrarAlgunosClientes():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("       Mostrar Algunos Clientes")
    print("***************************************")
    #Debemos solicitar al usuario la cantidad de registros a mostrar
    cantidad=int(input("Ingrese Cantidad de registros a mostrar: "))
    #Solicitar el envío de todos los registros
    datos=consultaParcial(cantidad)
    #Iterar a Datos para mostrar la información de cada registro
    print("Id Cliente\tRUN\tNombre\tApellidos\tDirección\tFono\tCorreo\tMonto Credito\tDeuda\tTipo Usuario")
    for dato in datos:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],
                                                              dato[6],dato[7],dato[8],dato[9]))
    print("*************************Fin de los Registros*************************************")
    input("Presione enter para continuar.....")
#Función para Mostrar
def mostrar():
    while(True):
        mostrarMenus()
        op2=int(input("Ingrese una Opción: "))
        if op2==1:
            mostrarTodosClientes()
            input("Presione enter para continuar.......")
        elif op2==2:
            mostrarUnClientes()
        elif op2==3:
            mostrarAlgunosClientes()
        if op2==4:
            break
        else:
            print("Opción ingresada esta Fuera de Rango :(")

#Función para modificar a un Cliente
def modificarCliente():
    os.system('cls')#Esta linea permite borrar la terminal
    #Crear una Lsiat para almacenar los nuevos Datos
    listaDatosCliente=[]
    print("***************************************")
    print("  Modificación de Datos del Cliente")
    print("***************************************")
    #Cargar a todos los cllientes existentes
    mostrarTodosClientes()
    #Solicitar el ID del Cleinet a modificar
    id_cliente_mod=int(input("Ingrese el Id del Cleinte a Modificar: "))
    dato=consultaParticular(id_cliente_mod)
    #Ahora preguntamos por lo que se desea modificar
    print("ID Cliente       :{}".format(dato[0]))
    #Inicamos el almacenamiento de datos nuevos y NO modificados en una lista
    listaDatosCliente.append(dato[0])
    print("RUN Cliente       :{}".format(dato[1]))
    listaDatosCliente.append(dato[1])
    opm=input("Desea Cambiar el Nombre: {} - [SI/NO]".format(dato[2]))
    if opm.lower()=="si":
        nuevoNombre=input("Ingrese Nuevo Nombre: ")
        listaDatosCliente.append(nuevoNombre)
    else:
        listaDatosCliente.append(dato[2])
    
    opm=input("Desea Cambiar el Apellido: {} - [SI/NO]".format(dato[3]))
    if opm.lower()=="si":
        nuevoApellido=input("Ingrese Nuevo Apellido: ")
        listaDatosCliente.append(nuevoApellido)
    else:
        listaDatosCliente.append(dato[3])

    opm=input("Desea Cambiar la Dirección: {} - [SI/NO]".format(dato[4]))
    if opm.lower()=="si":
        nuevaDireccion=input("Ingrese Nueva Direccion: ")
        listaDatosCliente.append(nuevaDireccion)
    else:
        listaDatosCliente.append(dato[4])

    opm=input("Desea Cambiar el Telefon: {} - [SI/NO]".format(dato[5]))
    if opm.lower()=="si":
        nuevoFono=input("Ingrese Nuevo Fono: ")
        listaDatosCliente.append(nuevoFono)
    else:
        listaDatosCliente.append(dato[5])

    opm=input("Desea Cambiar el Correo: {} - [SI/NO]".format(dato[6]))
    if opm.lower()=="si":
        nuevoCorreo=input("Ingrese Nuevo Correo: ")
        listaDatosCliente.append(nuevoCorreo)
    else:
        listaDatosCliente.append(dato[6])

    opm=input("Desea Cambiar el Monto Credito: {} - [SI/NO]".format(dato[7]))
    if opm.lower()=="si":
        nuevoMontoCredito=input("Ingrese Nuevo Monto Credito: ")
        listaDatosCliente.append(nuevoMontoCredito)
    else:
        listaDatosCliente.append(dato[7])

    opm=input("Desea Cambiar la Deuda: {} - [SI/NO]".format(dato[8]))
    if opm.lower()=="si":
        nuevaDeuda=input("Ingrese Nueva Deuda: ")
        listaDatosCliente.append(nuevaDeuda)
    else:
        listaDatosCliente.append(dato[8])

    opm=input("Desea Cambiar el Tipo Usuario: {} - [SI/NO]".format(dato[9]))
    if opm.lower()=="si":
        #Cargar los Tipos de Usuarios Existentes
        datos=mostrarTodosTiposUsuarios()
        print("ID Tipo Usuario\t\tDescripción")
        #Iteramos a Datos para mostrar los registros
        for dato in datos:
            print("{}\t\t\t{}".format(dato[0],dato[1]))
        print("*********************************")
        nuevoTipoUsuario=input("Ingrese Nuevo Tipo Usuario: ")
        listaDatosCliente.append(nuevoTipoUsuario)
    else:
        listaDatosCliente.append(dato[9])
    #Solicitamos la modificación al CRUD
    editar(listaDatosCliente)

#Función para Eliminar un Cliente
def eliminarCliente():
    os.system('cls')#Esta linea permite borrar la terminal
    print("***************************************")
    print("       Eliminar a un Cliente")
    print("***************************************")
    #Solicitar el envío de todos los registros
    mostrarTodosClientes()  
    id_cliente_elim=int(input("Ingrese el Id del Cliente a Eliminar: "))
    #Hacemos el llamdo al CRUD para eliminar
    eliminar(id_cliente_elim)