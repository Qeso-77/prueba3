class Procesador():
	def __init__ (self, marca):
		self.marca = marca



class Memoria():
	def __init__ (self, capacidad):
		self.capacidad = capacidad


class Computadora():
	def __init__ (self, marca_c, procesador, memoria):
		self.marca_c = marca_c
		self.procesador = Procesador(procesador)
		self.memoria = Memoria(memoria)

	def ficha_tecnica (self):
		print ('Marca de la computadora: ', self.marca_c)
		print ('Marca del procesador: ', self.procesador.marca)
		print ('Memoria: ', self.memoria.capacidad,'G')



mi_computadora = Computadora('BHG', 'Intel', 250)
mi_computadora.ficha_tecnica()

