class ganado:
	def __init__(self):
		while True:
			self.raza = input("Ingrese la raza del ganado \n 1- Angus Argentina \n 2- Holando Argentina \n 3- Hereford \n -:")
			if self.raza in ("1","2","3"):
				break
			else:
				print("La opcion ingresada no es correcta")

		while True:
			edad = input("Ingrese la edad del animal: ")
			try:
				self.edad = int(edad)
				break
			except:
				print("Edad ingresada en formato erroneo")

		while True:
			peso = input("Ingrese el peso del animal: ")
			try:
				self.peso = float(peso)
				break
			except:
				print("Peso ingresado en formato erroneo")

		while True:
			self.genero = input("Ingreso el genero del animal  \n 1- Macho \n 2- Hembra \n -: ")
			if self.genero in ("1","2"):
				break
			else:
				print("La opcion ingresada no es correcta")

	def estado(self):
		if self.raza == '1':
			print("Raza: Angus Argentina")
		elif self.raza == '2':
			print("Raza: Holando Argentina")
		elif self.raza == '3':
			print("Raza: Hereford")
		print("Edad: ",self.edad)
		print("Peso: ",self.peso)
		if self.genero == '1':
			print("Genero: Macho")
		else:
			print("Genero: Hembra")


def menu():
	print("***********************************************")
	print("************** Sistema de Ganado **************")
	print("***********************************************")
	print("")
	print("1= Agregar Animal")
	print("2= Mostrar promedio de edad del ganado")
	print("3= Mostrar datos del animal mas liviano y pesado")
	print("4= Mostrar cantidad de animales por raza")
	print("5= Salir")
	print("")
	while True:
		opcion = input("Ingrese opcion: ")
		if opcion in ("1","2","3","4","5"):
			break
		else:
			print("Opcion incorrecta")
	return(opcion)

lista = []

while True:
	opcion = menu()
	if opcion == "1":
		animal = ganado()
		lista.append(animal)
	elif opcion == "2":
		suma = 0
		for i in range(len(lista)):
			suma = suma + lista[i].edad
		promedio = suma / len(lista)
		print("El promedio de edad del ganado es: ",promedio)

		print("")
		seguir = input("Apriete enter para continuar")

	elif opcion == "3":
		for i in range(len(lista)):
			if i == 0:
				min = lista[i].peso
				posmin = i
				max = lista[i].peso
				posmax = i
			else:
				if  lista[i].peso < min:
					min = lista[i].peso
					posmin = i
				if  lista[i].peso > max:
					max = lista[i].peso
					posmax = i
		print("Datos del animal mas liviano")
		lista[posmin].estado()

		print("Datos del animal mas pesado")
		lista[posmax].estado()

		print("")
		seguir = input("Apriete enter para continuar")

	elif opcion == "4":
		Angus = 0
		Holando = 0
		Hereford = 0
		for i in range(len(lista)):
			if lista[i].raza == "1":
				Angus = Angus + 1
			elif lista[i].raza == "2":
				Holando = Holando + 1
			elif lista[i].raza == "3":
				Hereford = Hereford + 1

		print("Cantidad de Angus Argentina: ",Angus)
		print("Cantidad de Holando Argentina: ",Holando)
		print("Cantidad de Hereford: ",Hereford)
		print("")
		seguir = input("Apriete enter para continuar")
	else:
		print("Sistema terminado")
		break