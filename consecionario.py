import csv #módulo que nos deja manipular archivos csv

def ingresar_cliente():

  d={"Nombre":"","Apellido":"","Cédula":"","Teléfono":"","Dirección":""}  
  for ele in d:
    d[ele]=input("Ingrese {0}: ".format(ele))


  with open("clientes.csv","a",newline="") as clientes:
      lapiz = csv.writer(clientes)
      lapiz.writerow([d[ele] for ele in d])

#%%
       
       
      #ingresar vehículo  
def ingresar_vehiculo():
    d={"Placa":"","Marca":"","Modelo":"","Cilindraje":"","Color":"","Tipo de sercivio":"","Tipo de compustible":"",
        "Número de pasajeros":"","Capacidad de Carga":"","Número de chasis":"","Número de motor":""}
    for ele in d:
        d[ele]=input("Ingrese {0}: ".format(ele))    
    
    
    with open("carros.csv","a",newline="") as carros:
      lapiz = csv.writer(carros)
      lapiz.writerow([d[ele] for ele in d])



    
#%%    
    
    #ingresar servicios
def ingresar_servicio():
    d={"Código del servicio":"","Nombre del servicio":"","Precio unitario":"","Horas de Servicio":""}
    
    for ele in d:
        d[ele]=input("Ingrese {0}: ".format(ele))

    with open("servicios.csv","a",newline="") as servicios:
        lapiz = csv.writer(servicios)
        lapiz.writerow([d[ele] for ele in d])
        

#%%
      
def selec_servicio():
    f = "*"*20
    s= ""
    lista_servicios=[]
            
    while s!= "0":
        print(f+"\n SELECCIONE UN SERVICIO \n"+f)
        mostrar_servicios()
        s = input("Ingrese Código de servicio: ")
        lista_servicios.append(s)
        s = input("Desea seleccionar algún otro servicio?\n 1.Sí \n 0.No \n")
        
    
    return lista_servicios
 
    
def selec_carro(): # retorna el carro seleccionado, primero muestra los carros en la BD
    mostrar_carros()
    return input("ingrese la placa de su vehículo: ")
    

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
def mostrar_servicios(): #muestra los servicios para que los puedan seleccionar posteriormente
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
        print(Tabla)  
        
       
#%%
        

def solicitar_servicio():

    cliente_id=input("\n Ingrese número identidad: ")
    nombre_cliente= encontrar_nombre(cliente_id)
    
    vehiculo = selec_carro()
    
    lista_servicios=selec_servicio() #toca pasar esta lista a una funcion que genere facturas
    
    generar_factura(cliente_id,nombre_cliente,vehiculo, lista_servicios)
    
  #%% 
    
def encontrar_nombre(cliente_id): #de acuerdo a la cedula ingresada se asocia al nombre del cliente para su facturación
    
    with open("clientes.csv") as clientes:
        lector= csv.reader(clientes)
        
        for linea in lector: # recorre la base de datos de clientes, linea por linea hasta encontrar el numero que coincida con el nombre
            if linea[2]==cliente_id:
                cadena_nombre =linea[0]+" "+linea[1] #crea un cadena con el nombre y el apellido del cliente y la retorna
                return cadena_nombre
            
    
#%%
            
            
def generar_factura(cliente_id,nombre_cliente,vehiculo,l_servicios):
    total = 0
    s="" #el string que va a tener los nombres de los servicios pedidos
    
    
    for ele in l_servicios: #l_servicios es una lista con los codigos de los servicios seleccionados
        with open ("servicios.csv","r") as servicios:
            lector= csv.reader(servicios)
            
            for row in lector:
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
def id_factura(): #cuenta el numero de lineas en la base de datos facturas y lo retorna
    facturas=open("facturas.csv")
    lineas= len(facturas.readlines())
    return lineas+1
           
#%%

  
def imprimir_factura():
     

    with open("facturas.csv") as nuevo:
        lector= csv.reader(nuevo)
        
        for linea in lector: # tabla es el formato con el que se imprime, luego recorre todas las facturas imprimiendo una por una
            Tabla = """\
+-----------------------------------------------+
|                CONSECIONARIO UNAL             |
|-----------------------------------------------|
|    FACTURA Nro: {0}                             |
|    CEDULA: {1}                                |
|    CLIENTE: {2}                      |
|    PLACA VEHÍCULO: {3}                       |
|    SERVICIOS: {4}                       |   
|    PRECIO TOTAL: {5}                          | 
+------------------------------------------------+\
""" 
            Tabla = Tabla.format(*linea)  
            print(Tabla)

#%%


solicitar_servicio()
