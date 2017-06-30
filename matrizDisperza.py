class nodoMatriz():
	"""docstring for nodoMatriz"""
	def __init__(self,dato):
		self.dato = dato
		self.left = None 
		self.right = None
		self.up = None 
		self.down = None
		self.front = None
		self.back = None
		self.x = 0 
		self.y =0
		self.z =0 

class matrizDisp():
	"""docstring for matrizDisp"""
	def __init__(self):
		self.cabecera = nodoMatriz(0)

	def buscarNodoColumna(self,columna):
	
		temporal = self.cabecera

		while temporal!= None:
			if temporal.x == columna:
				#print temporal.dato
				#print "entro if buscar columna"
				return temporal 
			temporal = temporal.right
		return None 

	def buscarNodoFila(self,fila):
		#print "entrabuscarnodoFila"
		temporal = self.cabecera
		while temporal!= None:
			if temporal.y == fila:
				#print temporal.dato
				#print "entro if buscar columna"
				return temporal 
			temporal = temporal.down
		return None
	def buscarNodoNivel(self,nivel):
		temporal = self.cabecera
		while temporal!=None:
			if temporal.z == nivel:
				return temporal
			temporal = temporal.back
		return None 
	def crearFilaColumna(self,x,y,z):

	
		temporal = self.cabecera	
		nuevo = nodoMatriz(x)
		nuevo.x = x
		nuevo.y=0
		nuevo.z=0

		if temporal!=None:

			if self.buscarNodoColumna(x)==None:

				while int(x) > temporal.x :
					if temporal.right==None:
						break
					else:
						if x < temporal.right.x:
							break
						temporal = temporal.right
				#print "estoy incertando x: " + str(x) + " nodo pasado = "+ str(temporal.x)
				if temporal.right!=None:
					temporal.right.left = nuevo
					nuevo.right = temporal.right
				temporal.right = nuevo
				nuevo.left = temporal
			
			#trabajando y__________________________________________________________
			temporal = self.cabecera
			nuevoY = nodoMatriz(y)
			nuevoY.x = 0
			nuevoY.y = y
			nuevoY.z = 0
			if self.buscarNodoFila(y)==None:
				while y > temporal.y:
					if temporal.down == None:
						break
					else:
						if y < temporal.down.y:
							break
						temporal = temporal.down
				if temporal.down!=None:
					temporal.down.up = nuevoY
					nuevoY.down = temporal.down
				temporal.down = nuevoY
				nuevoY.up = temporal
			#trabajando z ______________________________

					
				
	def BuscarXY(self,x,y,z):
		temp1 = self.cabecera
		while temp1 != None:
			temp2 = temp1
			while temp2 != None:
				if temp2.x == x and temp2.y == y:
					return temp2
				temp2 = temp2.right
			temp1 = temp1.down		

	def insertarMatriz(self,dato, x,y ,z):
		
		self.crearFilaColumna(x,y,z)
		nodofila = self.buscarNodoFila(y)
		nodocolumna = self.buscarNodoColumna(x)
		
		nuevoNodo = nodoMatriz(dato)
		NodoEnZ = nodoMatriz(dato)
		if z != 0:
			
			NodoEnZ.x = x
			NodoEnZ.y = y
			NodoEnZ.z = z
			nuevoNodo.dato = "Vacio";
	
				 
		ndo = self.BuscarXY(x,y,z)
		if ndo == None:
			# print "en z = " + str(z) 
			nuevoNodo.x = x 
			nuevoNodo.y = y
			nuevoNodo.z = 0 
			while int(x) > nodofila.x :
				if nodofila.right== None: 
					break
				else:
					if x < nodofila.right.x:
						break
					nodofila = nodofila.right
				
			# print("       		Estoy insertando : " + dato)
			#print "Encontre el nodo x = "+str(nodofila.x) + " y : " + str(nodofila.y)

			while int(y) > nodocolumna.y:
				if nodocolumna.down==None:	
					break
				else:
					if y <       nodocolumna.down.y:
						break
					nodocolumna = nodocolumna.down
							
			

			#print "Encontre el nodo x = "+str(nodocolumna.x) + " y : " + str(nodocolumna.y)

			if nodofila.right!= None:
				nodofila.right.left = nuevoNodo
				nuevoNodo.right = nodofila.right
			if nodocolumna.down!=None:
				nodofila.down.up = nuevoNodo
				nuevoNodo.down = nodofila.down
			

			nuevoNodo.left = nodofila
			nodofila.right=nuevoNodo

			nuevoNodo.up = nodocolumna
			nodocolumna.down = nuevoNodo
			ndo = nuevoNodo

		if z > 0 :
			while  ndo.z < z and ndo.front != None :
			 	if ndo.front.z < z :
			 		ndo = ndo.front
			 	else:
			 		break
			if ndo.front != None:
				ndo.front.back = NodoEnZ
				NodoEnZ.front = ndo.front			
			ndo.front = NodoEnZ
			NodoEnZ.back = ndo 				

		#en z trabajando ___________________
		



	
	def imprimir2(self):
		temporal2 = self.cabecera
		while temporal2 !=None:
			temp = temporal2
			while temp != None:
				tem = temp
				while tem != None:
					print str(tem.dato) + " x : " + str(tem.x) + " y : "  +  str(tem.y)+ " z : "  +  str(tem.z)
					tem = tem.front
				
				temp = temp.right
			temporal2 = temporal2.down	

	def ejecutar(self,nombre):
		import os
		print nombre
		dotPath = "dot"
		fileInputPath="matriz.txt"
		fileOutputPath="matriz.png"
		
		print dotPath
		print fileOutputPath
		print fileInputPath
		tParam = " -Tpng "
		tOParam = " -o "
		tuple = (dotPath +tParam+ fileInputPath+tOParam+fileOutputPath)
		os.system(tuple)

	def imprimirMatriz(self):
		archi=open('matriz.txt','w')
		archi.close()
	def escribir(self):
		

		archi=open('matriz.txt','a')
		archi.write('digraph G {')
		
		auxiliar2=self.cabecera 
		while auxiliar2!=None:
			print("LOCO")
			auxiliar=auxiliar2
			while auxiliar!=None:
				print "entra segundo while "
				if auxiliar.right!=None:
					archi.write('"'+str(auxiliar.dato)+'"->"'+str(auxiliar.right.dato)+'" ')
					print "derecha"
					print str(auxiliar.dato) +"->"+str(auxiliar.right.dato)
				if auxiliar.left!=None:
					print "izquierda"
					archi.write('"'+str(auxiliar.dato)+'"->"'+str(auxiliar.left.dato)+'" ')
					print str(auxiliar.dato)+"->"+str(auxiliar.left.dato)
				if auxiliar.up!=None:
					print "arriba"
					archi.write('"'+str(auxiliar.dato)+'"->"'+str(auxiliar.up.dato)+'" ')
					print str(auxiliar.dato)+"->"+str(auxiliar.up.dato)
				if auxiliar.down!=None:
					print "abajo"
					archi.write('"'+str(auxiliar.dato)+'"->"'+str(auxiliar.down.dato)+'" ')
					print str(auxiliar.dato)+"->"+str(auxiliar.down.dato)
				

				auxiliar=auxiliar.right 	
			auxiliar2=auxiliar2.down

			
		archi.write("}")
		archi.close()
		self.ejecutar("matriz")	
	     

	


mat = matrizDisp()
mat.insertarMatriz("guapo",1,1,0)
mat.insertarMatriz("como",2,2,3)
mat.insertarMatriz("estas",3,3,0)
mat.insertarMatriz("jfasdf",4,1,2)
#mat.insertarMatriz("estas",3,1,1)
nodo = mat.BuscarXY(4,1,2)
#mat.imprimir2()
mat.imprimirMatriz()
mat.escribir()
# print "Encontre dato= " + str(nodo.dato) +" en x= "+ str(nodo.x) +" en y= "+ str(nodo.y) + " en z= " + str(nodo.z)









		
		
		
		