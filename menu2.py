#Sistema de Autopartes
#clase Facturas
#Atributos
#-nro de factura
#-codigo autopartes
#-automotriz: chevrolet, peugeot, citroen
#-Precio unitario
#-Cantidad vendida
#-Precio total facturado
#Metodos:
#-constructor: en donde se cargan los datos
#-Estado(): imprime todos los datos de la factura

#Programar el siguiente menu, utilizando la clase Facturas, la cual esta en el paquete
#Funciones y modulo Autopartes
#1- Cargar factura
#2- Mostrar el promedio de cantidad vendida por factura
#3- Los datos de la factura con menor y mayor Precio total
#4- Automotriz que mas unidades compro
#5- Salir
class Facturas:
    def __init__(self):
        self.nrodefactura=int(input("Ingrese numero de Factura: "))
        self.codigoautopartes=int(input("Codigo de autoparte: "))
        self.marca=str(input("Marca: "))
        self.cantidadvendida=int(input("Cantidad vendida: "))
        self.total=int(input("Ingrese monto total: "))
    
    def Estado(self):  
        print('Nro Factura: ',fac01.nrodefactura,'\nCodigo de autoparte: ', fac01.codigoautopartes,'\nMarca: ',fac01.marca,'\nCantidad Vendida: ',fac01.cantidadvendida,'\nTotal vendido: ',fac01.total)

        
    
         
        
        
        

print("Bienvenido al sistema de autopartes")

fac01 = Facturas()
print(fac01.Estado())
#print('Nro Factura: ',fac01.nrodefactura,'\nCodigo de autoparte: ', fac01.codigoautopartes,'\nMarca: ',fac01.marca,'\nCantidad Vendida: ',fac01.cantidadvendida,'\nTotal vendido: ',fac01.total)
#print('Codigo de autopartes: ',fac01.codigoautopartes)

