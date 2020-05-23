import operator

def leerArchivo(BD):
    #leyendo desde archivo
    with open(BD) as baseDatos:
        ind01=baseDatos.read(1)
        val01=baseDatos.read(2)
        ind02=baseDatos.read(1)
        val02=baseDatos.read(2)
        ind03=baseDatos.read(1)
        val03=baseDatos.read(2)
        ind04=baseDatos.read(1)
        val04=baseDatos.read(2)
        c0=ind01+str(val01)+ind02+str(val02)+ind03+str(val03)+ind04+str(val04)
        print("cad leida alterna ",c0)
        albumMusical={ind01:val01, ind02:val02, ind03:val03, ind04:val04}
        print("albumMusical alterno como diccionario: ",albumMusical)       

def ingresarPorTeclado():
    #ingreso por teclado
    ind1=input("ind1:")
    val1=eval(input("val1:"))
    ind2=input("ind2:")
    val2=eval(input("val2:"))
    ind3=input("ind3:")
    val3=eval(input("val3:"))
    ind4=input("ind4:")
    val4=eval(input("val4:"))
    baseDatos=open("BD.txt","a") 
    almacenarEnArchivo(ind1,val1,ind2,val2,ind3,val3,ind4,val4,baseDatos)
    crearDiccionario(ind1,val1,ind2,val2,ind3,val3,ind4,val4,baseDatos)
        
def almacenarEnArchivo(ind1,val1,ind2,val2,ind3,val3,ind4,val4,baseDatos):
    #almaceno la cadena en el archivo
    c=ind1+str(val1)+ind2+str(val2)+ind3+str(val3)+ind4+str(val4)
    print("cad ",c)
    baseDatos.write(ind1+str(val1)+ind2+str(val2)+ind3+str(val3)+ind4+str(val4))

def crearDiccionario(ind1,val1,ind2,val2,ind3,val3,ind4,val4,baseDatos):
    #creo la lista por con los valores ingresados por teclado ordenada por clave
    albumMusical={ind1:val1, ind2:val2, ind3:val3, ind4:val4}
    print("album Musical como diccionario: ", albumMusical)
    imprimirDiccionario(albumMusical,baseDatos)

def imprimirDiccionario(albumMusical,baseDatos):
    #imprimir el diccionario como una cadena
    st=""
    for key,val in albumMusical.items():
        st = st + key + str(val)
    print ("El diccionario como cadena es ",st)
    baseDatos.write(st)
    ordenarPorClave(albumMusical)
    ordenarPorValor(albumMusical)
    baseDatos.close()
    baseDatos=open("BD.txt","r") 
    print("Final, lo que leyo: ",baseDatos.read(None))
    baseDatos.close()
    print("bye ")

def ordenarPorClave(albumMusical):
    #ordenado por clave
    resultado = sorted(albumMusical.items(), key=operator.itemgetter(0))
    print ("ordenado por clave "+str(resultado))

def ordenarPorValor(albumMusical):
    # ordenado por su valor
    resultado = sorted(albumMusical.items(), key=operator.itemgetter(1))
    print ("ordenado por valor "+str(resultado))
    ordenarAlContrario(resultado)

def ordenarAlContrario(resultado):
    # ordenado al contrario
    resultado.reverse()
    print ("ordenado al contrario "+str(resultado))

def main():
    BD=input("Nombre de la BasedeDatos: ")
    leerArchivo(BD)
    ingresarPorTeclado()

main()
