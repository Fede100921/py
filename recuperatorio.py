class jugador:
    def __init__(self,nombre,edad,funcion,cantidadkm):
        self.nombre=nombre
        self.edad=edad
        self.funcion=funcion
        self.cantidadkm=cantidadkm
        
    def estado(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Funcion: ",self.funcion)
        print("Cantidad de Kilometros corridos: ",self.cantidadkm)
        
lista=[]


while True:
    
    print('Analisis de jugadores de la seleccion argentina')
    print('1-Agregar jugador: ')
    print('2-Promedio edad: ')
    print('3-Mostrar quien corrio mas y quien corrio menos: ')
    print('4-Mostrar cantidad de kilometros recorridos: ')
    print('5-Salir ')
    while True:
        opcion=input('Ingrese opcion: ')
        if opcion in ("1","2","3","4","5"):
            break
        else:
            print("Ingrese opcion correcta")
            
    if opcion == "1":
        nombre=input("Ingrese nombre del jugador: ")
        edad=int(input("Ingrese edad: "))
        while True:
            funcion=input("Ingrese funcion (ARQUERO,DEFENSOR,VOLANTE,DELANTERO): ")
            if funcion.lower() in ("arquero","defensor","volante","delantero"):
                break
            else:
                print("Ingrese funcion correcta")
        cantidadkm=float(input("Ingrese cantidad de kilometros: "))
        
        seleccion=jugador(nombre,edad,funcion,cantidadkm)   
        lista.append(seleccion)
        
    if opcion == '2':
        suma = 0
        for i in range(len(lista)):
            suma = suma + lista[i].edad
        promedio = suma / len(lista)
        print("El promedio de edad es : ",promedio)
        seguir = input('Oprimir enter para continuar: ')
        
    if opcion == '3':
        min = lista[0].cantidadkm
        minpos = 0
        max = lista[0].cantidadkm
        maxpos = 0
        for i in range(len(lista)):
            if lista[i].cantidadkm > max:
                max = lista[i].cantidadkm
                maxpos = i
            if lista[i].cantidadkm < min:
                min = lista[i].cantidadkm
                minpos = i
        print('Los datos del que mas corrio: ')
        lista[maxpos].estado()
        print('')
        print('Los datos del que menos corrio: ')
        lista[minpos].estado()
        print('')
        seguir = input('Oprimir enter para continuar: ')
        
    if opcion == '4':
        arq = 0
        defe = 0
        vol = 0
        delan=0
        
        for i in range(len(lista)):
            if lista[i].funcion == "arquero":
                arq = arq + lista[i].cantidadkm
            elif lista[i].funcion == "defensor":
                defe=defe + lista[i].cantidadkm
            elif lista[i].funcion == "volante":
                vol=vol + lista[i].cantidadkm
            elif lista[i].funcion == "delantero":
                delan=delan + lista[i].cantidadkm

        print("Cantidad de km recorridos por arqueros: ",arq)
        print("Cantidad de km recorridos por defensores: ",defe)
        print("Cantidad de km recorridos por volantes: ",vol)
        print("Cantidad de km recorridos por delanteros: ",delan)
        print("")
        seguir = input("Apriete enter para continuar")
        
    if opcion == '5':
        print('Programa terminado')
        break
    