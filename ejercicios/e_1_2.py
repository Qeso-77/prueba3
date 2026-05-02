# ejercicio 1.2
class CuentaBancaria():
	def __init__ (self, titular, saldo):
		self.titular = titular
		self._saldo = saldo

	def depositar(self, monto):
		if 0 >= monto:
			print ('Monto incompatible.')
		else:
			self._saldo += monto
			print ('Ha depositado dinero.')

	def extraer(self, monto):
		if monto > self._saldo:
			print ('El monto exede el saldo.')
		else:
			self._saldo -= monto
			print (f'Ha retrado dinero.')

	def consultar_saldo(self):
		print ('Su saldo es: ', self._saldo)

mi_usuario = CuentaBancaria('Juan Perez', 100)
mi_usuario.depositar(20)
mi_usuario.consultar_saldo()

### Enconsultar_saldo(), se está apĺicando el pilar de
### Encapsulamiento, ya que no se puede acceder desde fuera
### a self_saldo, si no que solo se puede visualizar con ese
### método.
