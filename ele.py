class ganado:
    def __init__(self, raza,edad,peso,genero):
        self.raza=raza
        self.edad=edad
        self.peso=peso
        self.genero=genero
        
        
        
        
        
    def estado(self):
        print("La raza es: ",self.raza)        
        print("La edad es: ",self.edad)
        print("La peso es: ",self.peso)
        print("La genero es: ",self.genero)
        
        
lista=[]




while True:
    print('Bienvenido a EL PELIGRO')
    print('Sistema de Ganado')
    print('1-Agregar animal: ')
    print('2-Promedio edad: ')
    print('3-Mostrar mas pesado y mas liviano: ')
    print('4-Mostrar cantidad de animales por raza: ')
    print('5-Salir ')
    while True:
        opcion=input('Ingrese Opcion')
        if opcion in ('1','2','3','4','5'):
            break
        else: 
            print('ingrese una opcion correcta')
    
    if opcion == "1":
        while True:
            raza=input('Ingrese Raza: Angus Argentina, Holando Argentina, Hereford')
            if raza.lower() in ("angus argentina","holando argentina", "hereford"):
                    break
            else:
                print("Nombre Incorrecto")
                
        edad=int(input('Ingrese edad del ganado: '))
        peso=float(input('Ingrese peso'))
        while True:
            genero=input('Ingrese genero: Macho o Hembra')
            if genero.lower() in ('macho', 'hembra'):
                    break
            else: 
                print('Sexo incorrecto')
            
        animal=ganado(raza,edad,peso,genero)   
        lista.append(animal)
                
    if opcion == '2':
        suma = 0
        for i in range(len(lista)):
            suma = suma + lista[i].edad
        promedio = suma / len(lista)
        print("El promedio de edad es : ",promedio)
        seguir = input('Oprimir enter para continuar: ')
        
    if opcion == '3':
        min = lista[0].peso
        minpos = 0
        max = lista[0].peso
        maxpos = 0
        for i in range(len(lista)):
            if lista[i].peso > max:
                max = lista[i].peso
                maxpos = i
            if lista[i].peso < min:
                min = lista[i].peso
                minpos = i
        print('Los datos del mas pesado ')
        lista[maxpos].estado()
        print('')
        print('Los datos del del mas liviano ')
        lista[minpos].estado()
        print('')
        seguir = input('Oprimir enter para continuar: ')
        
    if opcion == '4':
        angus = 0
        holando = 0
        hereford = 0
        for i in range(len(lista)):
            if lista[i].raza == "angus argentina":
                angus = angus + 1
            elif lista[i].raza == "holando argentina":
                holando = holando + 1
            elif lista[i].raza == "hereford":
                hereford = hereford + 1

        print("Cantidad de Angus Argentina: ",angus)
        print("Cantidad de Holando Argentina: ",holando)
        print("Cantidad de Hereford: ",hereford)
        print("")
        seguir = input("Apriete enter para continuar")
    

    
            
       
    