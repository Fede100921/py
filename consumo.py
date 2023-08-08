class Consumo:
    def __init__(self):
        self.nrousuario=int(input("Ingrese numero de usuario"))
        self.consuno=int(input("Ingrese consumo"))
        self.origen=int(input("Elegir origen\n1-Solar\n2-eolica\nhidrica"))
        self.precio=int(input("Ingrese precio"))
        self.opcion=int
        
        
    def estado(self):
        print("Numero de usuario: ",con.nrousuario,'\nConsumo: ',con.consuno,'\nOrigen: ',con.origen,'\nPrecio: ',con.precio)        
    
    def origen(self):
        while True:
            
            self.opcion==self.origen
            if self.origen==1:
                print("Energia solar")
            elif self.origen==2 :
                print('Energia eolica')   
            elif self.origen==3:
                print("Energia hidrica")    
            
        
        
con = Consumo()  
print(con.estado()) 
print (con.origen())     