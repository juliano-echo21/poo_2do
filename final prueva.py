import csv # módulo que nos deja manipular archivos csv, csv es un tipo de archivo que organiza datos en filas, y columnas son separadas por comas
import os# aunque cuenta con muhas carcteristicas solo sera usada para borrar pantalla de la consola y no hay que instalar ningun paquete por aparte
def buscar_carros(): #funcion que permite buscar y ordenar los carros
    os.system("cls")  # limpia la consola
    mostrar_busqueda("v")
    
    parametro= entrada('el parametro: ',int) # toma el parametro a ordenar la lista
    Tabla = """\
+----------------------------------------------------------------------------------------------------------------------------------------+
| Placa   Marca    Modelo   Cilindraje   Color    Tipo de Servicio  Tipo de combustible | # Pasajeros | C. de Carga |# Chasis |  # Motor |
|----------------------------------------------------------------------------------------------------------------------------------------|
{}
+----------------------------------------------------------------------------------------------------------------------------------------+\
"""  
#es el formato con el que se imprimiran los datos

    with open("carros.csv", "r") as carros:
        lector = csv.reader(carros) 
        lista =list(lector) #el objeto lector lo convierte en una lista para posteiormente orndenarla 
        orden = (sorted(lista,key=lambda x: x[parametro-1]))
        Tabla = (Tabla.format('\n'.join("| {:<7} {:<9} {:<9} {:<9} {:<9} {:>11} {:>17} {:>15} {:>12} {:>15} {:>10} |".format(*row)
                                    for row in orden)))
        os.system("cls")
        print(Tabla)
        os.system("pause")#detiene el programa
#%%
def mostrar_busqueda(p): #de acuerdo al parametro que se le envia imprime una tabla que muestra por cual parámetro organizar
    if p=="v":
        menu = """\
+-----------------------------+
|     SELECCIONE PARÁMETRO    |
|-----------------------------|
|1. PLACA                     |
|2. MARCA                     |
|3. MODELO                    |
|4. CILINDRAJE                |
|5. COLOR                     |
|6. SERVICIO                  |       
|7. COMBUSTIBLE               |
|8. Nro PASAJEROS             |
|9. CAPACIDAD DE CARGA        |
|10. Nro CHASIS               |              
|11. Nro MOTOR                |
+-----------------------------+\
"""     
        
    elif p=="s":
        menu = """\
+-----------------------------+
|     SELECCIONE PARÁMETRO    |
|-----------------------------|
|1. CÓDIGO                    |
|2. NOMBRE DEL SERVICIO       |
|3. PRECIO                    |
|4. HORAS DE SERVICIO         |
+-----------------------------+\
    """
    elif p=="c":
        menu = """\
+-----------------------------+
|     SELECCIONE PARÁMETRO    |
|-----------------------------|
|1. NOMBRE                    |
|2. APELLIDO                  |
|3. CÉDULA                    |
|4. TELÉFONO                  |
|5. DIRECCIÓN                 |
+-----------------------------+\
    """  
    print(menu)
    
  
def buscar_cliente():  # funcion busca y ordena los clientes por cualquier parámetro
    os.system("cls")  # limpia la consola
    mostrar_busqueda("c")
    parametro=entrada('el parametro: ',int)
    Tabla = """\
+----------------------------------------------------------------------+
| NOMBRE        APELLIDO        CÉDULA      TELÉFONO      DIRECCIÓN    |
|----------------------------------------------------------------------|
{}
+----------------------------------------------------------------------+\
""" 

    with open("clientes.csv", "r") as clientes:
        lector = csv.reader(clientes)
        lista =list(lector)
        orden = (sorted(lista,key=lambda x: x[parametro-1])) #ordena la lista de acuerdo al parámetro ingresado
               
        Tabla = (Tabla.format('\n'.join("| {:<14} {:8} {:>10} {:>14} {:>14}     |".format(*row)
                                    for row in orden)))
        os.system("cls")
        print(Tabla)
        os.system("pause")  # detiene el programa
         #va añadiendo a tabla line apor linea de manera ordenada           
            
#%%
def buscar_servicio(): # funcion busca y ordena los servicios por cualquier parámetro
    os.system("cls")  # limpia la consola
    mostrar_busqueda("s")
    parametro=entrada('el parametro',int)
    Tabla = """\
+------------------------------------------------------------------+
| CÓDIGO         NOMBRE           PRECIO c/u      HORA DE SERVICIO |
|------------------------------------------------------------------|
{}
+------------------------------------------------------------------+\
""" 
    with open("servicios.csv", "r") as servicios:
        lector = csv.reader(servicios)
        lista =list(lector)
        orden = (sorted(lista,key=lambda x: x[parametro-1]))
        
        Tabla = (Tabla.format('\n'.join("| {:<8} {:^18} {:>10} {:>19}       |".format(*row)
                                    for row in orden)))
        os.system("cls")
        print(Tabla)
        os.system("pause")  # detiene el programa
#%%
# Funcion para aceptar o negar entradas
#valida las entradas, de acuerdo a su tipo
def entrada(men, tipo):
    v = 0
    a = False
    while not a:
        try:
            v = tipo(input("Ingrese " + str(men)))
            a = True
        except:
            print("Entrada inválida, por favor intente de nuevo.")
    return v
#%%

# Funcion para ingresar clientes a la base de datos
def ingresar_cliente():
    os.system("cls")  # limpia la consola
    d = {"Nombre": "", "Apellido": "", "Cédula": "", "Teléfono": "", "Dirección": ""}
    #se tiene un diccionrario que va a ser llenado con los datos ingresados

    for ele in d:
        if ele == "Cédula" or ele == "Teléfono": #para estos dos parametros los valida con la funcion entrada
            d[ele] = entrada(ele, int)
        else:
            d[ele] = entrada(ele, str)

    with open("clientes.csv", "a", newline="") as clientes:
        lapiz = csv.writer(clientes)
        lapiz.writerow([d[ele] for ele in d]) #escribe una linea con los datos que estan en el diccionario
                                              #escribe una linea que es una lista
# ingresar vehículo a la base de datos

#%%
def ingresar_vehiculo():
    os.system("cls")  # limpia la consola
    d = {"Placa": "", "Marca": "", "Modelo": "", "Cilindraje": "", "Color": "", "Tipo de sercivio": "",
         "Tipo de compustible": "",
         "Número de pasajeros": "", "Capacidad de Carga": "", "Número de chasis": "", "Número de motor": ""}
         #en un diccionario se guardan todas las caracteristicas de un carro
    for ele in d: #recorre cada llave del diccionario, y el valor va a ser e ingresado por el usuario
        if ele == "Número de pasajeros" or ele == "Capacidad de Carga" or ele == "Número de chasis" or ele == "Número de motor":
            d[ele] = entrada(ele, int)
        else:
            d[ele] = entrada(ele, str)

    with open("carros.csv", "a", newline="") as carros:
        lapiz = csv.writer(carros)
        lapiz.writerow([d[ele] for ele in d]) #escribe una liena en el csv que es una lista, donde cada elemento es el valor
                                              #ingresado por el usuario

#%%
# ingresar los servicios a manejar
def ingresar_servicio():
    os.system("cls")  # limpia la consola
    d = {"Código del servicio": "", "Nombre del servicio": "", "Precio unitario": "", "Horas de Servicio": ""}
  #en undiccionario se guardan las características de un servicio
  #el usuario ingresa uno a uno
    for ele in d:
        if ele == "Nombre del servicio":
            d[ele] = entrada(ele, str)
        else:
            d[ele] = entrada(ele, int)

    with open("servicios.csv", "a", newline="") as servicios:
        lapiz = csv.writer(servicios)
        lapiz.writerow([d[ele] for ele in d])
#%%

def mostrar_servicios(): #es la funcion que permite ver los servicio en el orden en el que esten en el documento
    Tabla = """\
+------------------------------------------------------------------+
| CÓDIGO         NOMBRE           PRECIO c/u      HORA DE SERVICIO |
|------------------------------------------------------------------|
{}
+------------------------------------------------------------------+\
"""    
    with open ("servicios.csv") as nuevo:
        l= csv.reader(nuevo)
     
        Tabla = (Tabla.format('\n'.join("| {:<8} {:^18} {:>10} {:>19}       |".format(*row)
                                    for row in l)))  
        #cada linea tiene un formato, los numeros son la cantidad de caracteres a la derecha o a la izquierda
        print(Tabla) 
#%%

def mostrar_carros(): #funcion que muestra los carros (placa y marca puede ser algo más)
    Tabla = """\
+----------------------------------------------------------------------------------------------------------------------------------------+
| Placa   Marca    Modelo   Cilindraje   Color    Tipo de Servicio  Tipo de combustible | # Pasajeros | C. de Carga |# Chasis |  # Motor |
|----------------------------------------------------------------------------------------------------------------------------------------|
{}
+----------------------------------------------------------------------------------------------------------------------------------------+\
"""  
    with open ("carros.csv") as nuevo:
        l= csv.reader(nuevo)
     
        Tabla = (Tabla.format('\n'.join("| {:<7} {:<9} {:<9} {:<9} {:<9} {:>11} {:>17} {:>15} {:>12} {:>15} {:>10} |".format(*row)
                                    for row in l)))  

        print(Tabla)         
#%%
def mostrar_clientes():       
    Tabla = """\
+---------------------------------------+
| NOMBRE        APELLIDO        CÉDULA  |
|---------------------------------------|
{}
+---------------------------------------+\
"""         
    with open ("clientes.csv") as nuevo:
        l= csv.reader(nuevo)
     
        Tabla = (Tabla.format('\n'.join("| {:<14} {:8} {:>10}    |".format(*row)
                                    for row in l)))  
        print(Tabla)

        #%%
def selec_servicio(): #uncion que permite ver y seleccionar los servicios deseados,
    s = ""
    lista_servicios = [] #en esta lista se guardaran los codigos de los servicios 

    while s != "0":
        mostrar_servicios()

        while True:
            codigo= input("Ingrese Código de servicio: ")
        
            if servicio_existe(codigo): #llama a la funcion servicio_existe que valida si efectivamente el servicio esta registrado
                break
            else:
                print("\n EL SERVICIO CON CÓDIGO {0} NO ESTÁ REGISTRADO, INTENTE OTRA VEZ".format(codigo))
                #no permitirá avanzar hasta que el servicio que digite sea correcto
        lista_servicios.append(codigo) #añade el codigo delservicio a la lista
        s = input("Desea seleccionar algún otro servicio?\n 1.Sí \n 0.No \n")
        #hasta que el usuario no desee seleccionar más
    return lista_servicios



def servicio_existe(codigo): #verifica si el codigo existe

    with open("servicios.csv") as servicios:
        lector=csv.reader(servicios)
        lista_codigos=[i[0] for i in lector ] #crea una lista con los codigos de cada servicio
        
        return codigo in lista_codigos #retorna true o false de acuerdo si el codigo se encentra en una lista de codigos

#%%
def selec_carro():  # retorna el carro seleccionado, primero muestra los carros en la BD  
    while True:
        
        mostrar_carros()
        placa= input("ingrese la placa de su vehículo: ")
        
        if carro_existe(placa):
            break
        else:
            print("\n EL CARRO CON PLACA {0} NO ESTÁ REGISTRADO, INTENTE OTRA VEZ".format(placa))
        
    return placa

def carro_existe(entrada): #verifica si el carro está registrado
    with open("carros.csv") as carros:
        lector=csv.reader(carros)
        lista_placas=[i[0] for i in lector ] #crea una lista con las placas de los carros
        
        return entrada in lista_placas #si la placa ingresa está registra retorna verdadero, de lo contrario, retorna falso
    
#%%
def cliente_existe(entrada): #verifica si el cliente está registrado
    with open("clientes.csv") as clientes:
        lector=csv.reader(clientes)
        lista_id=[i[2] for i in lector ] #crea un alista con los id de los clientes registrados
        
        return entrada in lista_id #si el id existe retorna verdadero
        
            
#%%
def solicitar_servicio(): #funcion que permite solicitar un servicio
    os.system("cls")  # limpia la consola
    while True: #hasta que no se ingrese un cliente que este registrado no avanza
        
        mostrar_clientes() #muestra todos los clientes para poder ver los ids
        cliente_id=input("\n Ingrese número identidad: ")
        
        if cliente_existe(cliente_id): #llama a la funcion cliente_existe para saber si el cliente esta registrado
            break
        else:
            print("EL CLIENTE CON ID {0} NO ESTÁ REGISTRADO, INTENTE OTRA VEZ".format(cliente_id))
        
    nombre_cliente= encontrar_nombre(cliente_id) #llama a la funcion encontrar_nombre para asociar el nombre y el id
    
   # cliente = entrada("Ingrese número identidad: ", int)

    vehiculo = selec_carro() #llama a la funcion selec_carro para guardar el carro seleccionado 

    lista_servicios = selec_servicio()  #con la lista de codigos de servicios que retorna selec_servicio se crea la variable
                                        #lista_servicio
    
    generar_factura(cliente_id,nombre_cliente,vehiculo, lista_servicios) #ahora se tiene, el nombre, su id, su vehiculo, y los codigos de los servicios 


#%%
    
def generar_factura(cliente_id,nombre_cliente,vehiculo,l_servicios): #con los parametros suministrados se genera una factura
                                                                    #en un archivo exclusivo para facturas
    total = 0
    s="" #el string que va a tener los nombres de los servicios pedidos
    
    
    for ele in l_servicios: #l_servicios es una lista con los codigos de los servicios seleccionados
        with open ("servicios.csv","r") as servicios:
            lector= csv.reader(servicios)
            
            for row in lector: #si el codigo del servicio coincide con el codigo en la linea en el archivo
                              #añade a la cadena el nombre del servicio
                if row[0]==ele:
                    s+=row[1]+", " #añade a la cadena el nombre del servicio
                    total+=int(row[2]) #el valor 2 de la fila corresponde al precio
                    break #encuentr el servicio y sale del bucle
   
                    
    with open ("facturas.csv","a",newline="") as facturas:
        lapiz=csv.writer(facturas)# abre la base de datos de las facturas y escribe escribe un linea
                                  # con el numero de factura, el id del cliente, el nombre, el vehículo, los servicios
                                    # y el precio total
        
        lapiz.writerow([id_factura(),cliente_id,nombre_cliente,vehiculo,s,total]) 
        #en la BD de las facturas se guarda la factura con nombre de cliente, vehiculo y servicios

#%%
def imprimir_factura():
    os.system("cls")  # limpia la consola
    try: #si el archivo no existe o esta vacio, genera excepcion y devuelve al menu principal
        with open("facturas.csv") as nuevo:
            lector= csv.reader(nuevo)
            
            for linea in lector: # tabla es el formato con el que se imprime, luego recorre todas las facturas imprimiendo una por una
                Tabla = """\
    +-----------------------------------------------+
    |                CONSECIONARIO UNAL             |
    |-----------------------------------------------|
        FACTURA Nro: {0}                             
        CEDULA: {1}                                
        CLIENTE: {2}                      
        PLACA VEHÍCULO: {3}                       
        SERVICIOS: {4}                          
        PRECIO TOTAL: {5}                          
    +------------------------------------------------+\
    """ 
                Tabla = Tabla.format(*linea)  
                print(Tabla)   
    except:
        print("\n NO EXISTE NINGUNA FACTURA \n")  
                        
#%%
def encontrar_nombre(cliente_id): #de acuerdo a la cedula ingresada se asocia al nombre del cliente para su facturación
    
    with open("clientes.csv") as clientes:
        lector= csv.reader(clientes)
        
        for linea in lector: # recorre la base de datos de clientes, linea por linea hasta encontrar el numero que coincida con el nombre
            if linea[2]==cliente_id:
                cadena_nombre =linea[0]+" "+linea[1] #crea un cadena con el nombre y el apellido del cliente y la retorna
                return cadena_nombre        
 
    
def id_factura(): #cuenta el numero de lineas en la base de datos facturas y lo retorna, así sabe que id va a ser la siguiente factura
    facturas=open("facturas.csv")
    lineas= len(facturas.readlines())
    return lineas+1   
#%%
import csv    
def buscar():
     menu = """\
+------------------------------------------------------------+
|                         BÚSQUEDA                           |
|------------------------------------------------------------|
|                ¿EN QUÉ MÓDULO DESEA BUSCAR?                |
|1. CLIENTES                                                 |
|2. VEHÍCULOS                                                |
|3. SERVICIOS                                                |
|4. FACTURAS                                                 |
+------------------------------------------------------------+\
"""
     os.system("cls")
     print(menu)
     opcion=input(("\n DIGITE: "))
    
     while opcion not in ["1","2","3","4"]:
         
        print("ENTRADA INVALIDA INTENTE DE NUEVO")
        opcion=input(("\n DIGITE: "))    
    
    
     if opcion=="1":
         menu = """\
+-------------------------------------------------+
|                  DATOS CLIENTE                  |
|-------------------------------------------------|
| NOMBRE: {0}
| APELLIDO: {1}
| CEDULA: {2} 
| TELEFONO: {3}
| DIRECCION: {4} 
+-------------------------------------------------|
"""
         identificacion = input("INGRESE CÉDULA: ")
        
         with open("clientes.csv") as clientes:
            lector = csv.reader(clientes)
            
            lista_ids= [i[2] for i in lector]
            
            if identificacion not in lista_ids:
                print("LA CÉDULA {0} NO ESTA REGISTRADA".format(identificacion))
            
            else:
                 with open("clientes.csv") as clientes:
                     lector = csv.reader(clientes)
                     for ele in lector:
                    
                         if ele[2]== identificacion:
                             print(menu.format(ele[0],ele[1],ele[2],ele[3],ele[4]))
                             break
                    
                
     
     elif opcion =="2":
          menu = """\
+-------------------------------------------------+
|                  DATOS VEHICULO                  |
|-------------------------------------------------|
| PLACA: {0}
| MARCA: {1}
| MODELO: {2} 
| CILINDRAJE: {3} 
| COLOR : {4}
+-------------------------------------------------|
"""
          placa = input("INGRESE PLACA: ")
        
          with open("carros.csv") as carros:
            lector = csv.reader(carros)
            lista_placas= [i[0] for i in lector]
            
            if placa not in lista_placas:
                print("LA PLACA {0} NO ESTA REGISTRADA".format(placa))
            
            else:
                with open("carros.csv") as carros:
                    lector = csv.reader(carros)
                    
                    for ele in lector:
                        if ele[0]== placa:
                            print(menu.format(ele[0],ele[1],ele[2],ele[3],ele[4]))
                            break
    
    
    
    
     elif opcion =="3":
       menu = """\
+-------------------------------------------------+
|                  DATOS SERVCIO                  |
|-------------------------------------------------|
| CODIGO: {0}
| NOMBRE: {1}
| PRECIO: {2} 
| HORAS: {3} 
+-------------------------------------------------|
"""

       codigo = input("INGRESE CODIGO SERVICIO: ")
        
       with open("servicios.csv") as servicios:
            lector = csv.reader(servicios)
            lista_codigos= [i[0] for i in lector]
            
            if codigo not in lista_codigos:
                print("EL COGIDO {0} NO ESTA REGISTRADO".format(codigo))
            else:
                with open("servicios.csv") as servicios:
                    lector = csv.reader(servicios)
                    for ele in lector:
                        if ele[0]== codigo:
                            print(menu.format(ele[0],ele[1],ele[2],ele[3]))
    
     
    
     elif opcion =="4":
        menu = """\
+-------------------------------------------------+
|                  DATOS SERVCIO                  |
|-------------------------------------------------|
| FACTURA Nro: {0}
| CC CLIENTE: {1}
| NOMBRE CLIENTE: {2} 
| PLACA CARRO: {3} 
| SERVICIOS : {4}
| PRECIO TOTAL: {5}
+-------------------------------------------------|
"""
        num = input("INGRESE Nro DE FACTURA: ")
        try:  
         with open("facturas.csv") as facturas:
                lector = csv.reader(facturas)
                lista_num= [i[0] for i in lector]
                
                if num not in lista_num:
                    print("LA FACTURA {0} NO EXISTE".format(num))
                else:
                     with open("facturas.csv") as facturas:
                         lector = csv.reader(facturas)
                         for ele in lector:
                             if ele[0]== num:
                                 print(menu.format(ele[0],ele[1],ele[2],ele[3],ele[4],ele[5]))
        except:
            print("NO EXISTE NINGUNA FACTURA")
        
        


#%%
def mostrar_menu(): #cuando se llama a esta funcion muestra todas las funcionalidades del programa en formato de menu
    menu = """\
+------------------------------------------------------------+
|               BIENVENID@ AL CONCESIONARIO UNAL             |
|------------------------------------------------------------|
|                   ESTE ES NUESTRO MENÚ                     |
|1. REGISTRAR UN CARRO                                       |
|2. REGITRAR UN CLIENTE                                      |
|3. REGISTRAR UN SERVICIO                                    |
|4. BUSCAR Y ORDENAR CARROS                                  |
|5. BUSCAR Y ORDENAR CLIENTES                                |
|6. BUSCAR Y ORDENAR SERVICIOS                               |
|7. SOLICITAR SERVICIOS                                      |
|8. IMPRIMIR FACTURAS                                        |
|9. BUSCAR EN MODULO                                         |
|0. SALIR                                                    |
+------------------------------------------------------------+\
"""
    os.system("cls")
    print(menu)
#%%        
        
def menu_de_base_de_datos(): #es la función en donde de acuerdo a la entred del usuario se hace lo que se pide
                              #por medio de llamar a la funcion correspondiente
    while True:    
        mostrar_menu()
        d = {
            1: ingresar_vehiculo,
            2: ingresar_cliente,
            3: ingresar_servicio,
            4: buscar_carros,
            5: buscar_cliente,
            6: buscar_servicio,
            7: solicitar_servicio,
            8: imprimir_factura,
            9: buscar
            }
        
        opcion = entrada('una opción: ', int)
        
        if opcion==0: #si la entrada es cero el programa termina de ejecutarse
            print("GRACIAS POR ELEGIRNOS, VUELVA PRONTO")
            break
        
        f = d.get(opcion, None)   #se obtiene la funcion y se ejecuta, si la entrada es errónea
                                  #se pide que se ingrese nuevamente   
        if f:
            f()
        else:
            print("ENTRADA INCORRECTA")         
            
            
if __name__=="__main__":

    menu_de_base_de_datos()
