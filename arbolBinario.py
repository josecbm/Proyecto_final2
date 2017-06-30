import lista_doblemente_Enlazada
class NodoBinario():
	def __init__(self, usuario , passw,lista,estado ):
		self.usuario = usuario 
		self.passw = passw
		self.izq = None
		self.der = None
		self.lista = lista
		self.estado = estado
class Binario():
	
	def __init__(self):
		self.raiz = None
		self.grafica = "digraph G {"

	def agregar(self, usuario,passw,estado):
		lista = lista_doblemente_Enlazada.lista()
		lista.add(20,20,43,"true","damage")

		nodo = NodoBinario(usuario,passw,lista,estado)
		if self.raiz == None:
			
			self.raiz = nodo
		else:
			aux = self.raiz
			padre = None 
			while aux !=None:
				padre = aux
				if nodo.usuario >= aux.usuario:
					aux = aux.der
				else:
					aux = aux.izq
			if nodo.usuario >= padre.usuario:
				padre.der = nodo
			else:
				padre.izq = nodo
		return True

	# def buscarPreOrden(self,nodo , usuario):
	def proO(self,nodo,usr,passw):
		if nodo!=None:
			if nodo.usuario==usr and nodo.passw==passw:
				print True
			# print nodo.usuari
			self.proO(nodo.izq,usr,passw)
			self.proO(nodo.der,usr,passw)
	# def comparador(self,usr , passw):



	def preOrden(self, nodo):
			#print "padre"+nodo.usuario
		if nodo !=None:
			
			if nodo.izq !=None:
				#self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"'+str(nodo.izq.usuario) +","+str(nodo.izq.passw)+","+str(nodo.izq.lista.recorrer().tiros)+","+str(nodo.izq.lista.recorrer().tirosAcertados)+","+str(nodo.izq.lista.recorrer().tirosFallados)+","+str(nodo.izq.lista.recorrer().bandera)+","+str(nodo.izq.lista.recorrer().damage)+'"'

				self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) +","+str(nodo.lista.recorrer().tiros)+","+str(nodo.lista.recorrer().tirosAcertados)+","+str(nodo.lista.recorrer().tirosFallados)+","+str(nodo.lista.recorrer().bandera)+'"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+","+str(nodo.izq.lista.recorrer().tiros)+","+str(nodo.izq.lista.recorrer().tirosAcertados)+","+str(nodo.izq.lista.recorrer().tirosFallados)+","+str(nodo.izq.lista.recorrer().bandera)+'"'
			if nodo.der !=None:
				#self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"'+str(nodo.der.usuario) +","+str(nodo.der.passw)+","+str(nodo.der.lista.recorrer().tiros)+","+str(nodo.der.lista.recorrer().tirosAcertados)+","+str(nodo.der.lista.recorrer().tirosFallados)+","+str(nodo.der.lista.recorrer().bandera)+","+str(nodo.der.lista.recorrer().damage)+'"'
				self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) +","+str(nodo.lista.recorrer().tiros)+","+str(nodo.lista.recorrer().tirosAcertados)+","+str(nodo.lista.recorrer().tirosFallados)+","+str(nodo.lista.recorrer().bandera)+'"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+","+str(nodo.der.lista.recorrer().tiros)+","+str(nodo.der.lista.recorrer().tirosAcertados)+","+str(nodo.der.lista.recorrer().tirosFallados)+","+str(nodo.der.lista.recorrer().bandera)+'"'

			#print nodo.passw
			self.preOrden(nodo.izq)
			self.preOrden(nodo.der)
	def preOrden2(self, nodo):
			#print "padre"+nodo.usuario
		if nodo !=None:
			
			if nodo.izq !=None:
				self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) +","+str(nodo.lista.recorrer().tiros)+","+str(nodo.lista.recorrer().tirosAcertados)+","+str(nodo.lista.recorrer().tirosFallados)+","+str(nodo.lista.recorrer().bandera)+'"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+","+str(nodo.der.lista.recorrer().tiros)+","+str(nodo.der.lista.recorrer().tirosAcertados)+","+str(nodo.der.lista.recorrer().tirosFallados)+","+str(nodo.der.lista.recorrer().bandera)+'"'
				#self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+","+str(nodo.izq.lista) +'"'
				#self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+'"'
			if nodo.der !=None:
				self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) +","+str(nodo.lista.recorrer().tiros)+","+str(nodo.lista.recorrer().tirosAcertados)+","+str(nodo.lista.recorrer().tirosFallados)+","+str(nodo.lista.recorrer().bandera)+'"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+","+str(nodo.izq.lista.recorrer().tiros)+","+str(nodo.izq.lista.recorrer().tirosAcertados)+","+str(nodo.izq.lista.recorrer().tirosFallados)+","+str(nodo.izq.lista.recorrer().bandera)+'"'
				#self.grafica = self.grafica+'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+","+str(nodo.der.lista) +'"'
				#self.grafica = self.grafica+'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+'"'

			#print nodo.passw
			self.preOrden(nodo.izq)
			self.preOrden(nodo.der)
	def postOrden(self, nodo ):
		print "entra"
		if nodo !=None:
			
			self.preOrden(nodo.izq)
			self.preOrden(nodo.der)

			if nodo.izq !=None:
				#self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+","+str(nodo.izq.lista) +'"'
				self.grafica =self.grafica +'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.izq.usuario) +","+str(nodo.izq.passw)+'"'
			if nodo.der !=None:
				#self.grafica = self.grafica+'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+","+str(nodo.der.lista) +'"'
				self.grafica = self.grafica+'"' + str(nodo.usuario) +","+str(nodo.passw) + '"->"' + str(nodo.der.usuario) +","+str(nodo.der.passw)+'"'
	def orden(self, nodo):
		print "entra"
		if nodo !=None:
			
			self.preOrden(nodo.izq)
			return nodo
			self.preOrden(nodo.der)
	def getRaiz(self):
		return self.raiz

	def ejecutar(self,doc,nombreArchivo):
		import os
		print doc
		archivo=open(nombreArchivo+'.txt','w')
		archivo.write(str(doc))
		archivo.close()
		dotPath = "dot"
		fileInputPath=nombreArchivo+".txt"
		fileOutputPath=nombreArchivo+".png"
		
		print dotPath
		print fileOutputPath
		print fileInputPath
		tParam = " -Tpng "
		tOParam = " -o "
		tuple = (dotPath +tParam+ fileInputPath+tOParam+fileOutputPath)
		os.system(tuple)

	def imprimirMatriz(self):

		archivo=open('arbol.txt','w')
		archivo.write('digraph G{')
		nod = self.orden(self.getRaiz())
		archivo.write(str(nod.usuario +","+nodo.passw+","+nodo.lista.tiros+","+nodo.lista.tirosAce+","+nodo.lista.damage)+'->'+str(nod.izq.usuario +","+nodo.izq.passw+","+nodo.izq.lista.tiros+","+nodo.izq.lista.tirosAce+","+nodo.izq.lista.damage)+';'+str(nod.usuario)+'->'+str(nod.der.usuario +","+nodo.der.passw+","+nodo.der.lista.tiros+","+nodo.der.lista.tirosAce+","+nodo.der.lista.damage))
		archivo.write("}")
		archivo.close()
		self.ejecutar("arbol")	

		
# b = Binario()
# b.agregar("jose","123","desconectado")
# b.agregar("miguel","123","desconectado")
# b.agregar("juan","123","desconectado")
# b.agregar("nowell","123","desconectado")
# b.agregar("ximena","123","desconectado")
# b.agregar("Tatiana","123","desconectado")
# b.agregar("goku","123","desconectado")
# b.preOrden(b.getRaiz())
# b.grafica = b.grafica + "}"
# b.ejecutar(b.grafica,"arbol")
# b.grafica ="digraph G {"
# b.preOrden2(b.getRaiz())
# b.grafica = b.grafica + "}"
# b.ejecutar(b.grafica,"arbol2")