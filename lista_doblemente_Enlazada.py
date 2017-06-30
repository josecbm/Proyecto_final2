class nodolista():
	def __init__(self,tiros,tirosAcertados,tirosFallados , bandera , damage):
		self.tiros = tiros
		self.tirosAcertados = tirosAcertados
		self.tirosFallados = tirosFallados
		self.bandera = bandera 
		self.damage = damage
class lista():

	
	def __init__(self):
		self.cabeza = None
	def add(self, tiros , tirosAcertados , tirosFallados , bandera , damage):
		
		

		nuevoNodo = nodolista(tiros,tirosAcertados,tirosFallados , bandera , damage) 

		if self.cabeza == None:
			nuevoNodo.siguiente = nuevoNodo
			nuevoNodo.anterior = nuevoNodo
			self.cabeza = nuevoNodo
			bandera = True
			
		else:
			nodoTemporal = self.cabeza.anterior

			self.cabeza.anterior = nuevoNodo
			nuevoNodo.anterior = nodoTemporal
			nuevoNodo.siguiente = self.cabeza
			nodoTemporal.siguiente =nuevoNodo

		return True
	
	

	def recorrer(self):
		temporal = self.cabeza
		if temporal!=None:
			return temporal
		# while temporal!=self.cabeza:
		# 	print temporal.tiros
		# 	print temporal.tirosFallados
		# 	print temporal.tirosAcertados
		# 	print temporal.bandera
		# 	print temporal.damage
			
			
		# 	temporal = temporal.anterior
		# print self.cabeza.tiros
		# print self.cabeza.tirosFallados
		# print self.cabeza.tirosAcertados
		# print self.cabeza.bandera
		# print self.cabeza.damage

		
	
# listanueva = lista()
# listanueva.add("34","43","22","True","bueno")
# print listanueva.recorrer().tiros
# print listanueva.recorrer().tirosAcertados
# print listanueva.recorrer().tirosFallados
# print listanueva.recorrer().bandera
# print listanueva.recorrer().damage
# listanueva.add("nowell2","34","43","22","True","bueno")
# listanueva.add("nowell3","34","43","22","True","bueno")
# listanueva.add("nowell4","34","43","22","True","bueno")
# listanueva.add("nowell5","34","43","22","True","bueno")

# listanueva.recorrer()
#print listanueva.buscarUsuarios("nowell4").passw