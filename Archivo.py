import sys
import arbolBinario
class Archivo():
	"""docstring for Archivo"""
	def __init__(self):
		valor="hola"
		
	datos=[]
	def leerUsuarios(self, cadena):
		arbol = arbolBinario.Binario()
		infile = open(cadena, 'r')
		contenido = infile.read()
		contenedor = contenido.splitlines()
		
		for l in contenedor:
			cont = l.split(',')
			print "usuarios: "+str(cont[0])
			print "contrasena: "+str(cont[1])
			print "estadoConectado: "+str(cont[2])
			if str(cont[0])!="Usuario":
				print "___________________________"
				arbol.agregar(str(cont[0]),str(cont[1]),"desconectado")
		arbol.preOrden(arbol.getRaiz())
		arbol.grafica = arbol.grafica + "}"
		arbol.ejecutar(arbol.grafica , "arbol")
		arbol.grafica ="digraph G {"
		arbol.preOrden2(arbol.getRaiz())
		arbol.grafica = arbol.grafica + "}"
		arbol.ejecutar(arbol.grafica,"arbol2")

	def leerNaves(self, cadena):
	 	infile = open(cadena, 'r')
		contenido = infile.read()
		contenedor = contenido.splitlines()
		for l in contenedor:
			cont = l.split(",")
			print "jugador: "+ str(cont[0])
			print "columna: "+ str(cont[1])
			print "fila: "+ str(cont[2])
			print "nivel: "+ str(cont[3])
			print "modo: "+ str(cont[4])
			print "direccion: "+ str(cont[5])
			print "________________"

	
	def leerJuegos(self , cadena):
		infile = open(cadena, 'r')
		contenido = infile.read()
		contenedor = contenido.splitlines()
		for l in contenedor:
			cont = l.split(",")
			print "Usuario base: "+str(cont[0])+" oponente: " +str(cont[1])+" Tiros realizados: "+str(cont[2])+" Tiros Acertados: "+str(cont[3])+" Tiros fallados: "+str(cont[4])+" gano o no: "+str(cont[5]) 
		print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
	def leerjuegoActual(self, cadena):
		infile = open(cadena, 'r')
		contenido = infile.read()
		contenedor = contenido.splitlines()
		for l in contenedor:
			cont = l.split(",")
			print "usuario1: "+str(cont[0])+" usuario2: " +str(cont[1])+" tamanox: "+str(cont[2])+" tamanoy : "+str(cont[3])+" variante: "+str(cont[4])+" tiempo: "+str(cont[5])+" disparo: "+str(cont[6])+" #rafaga: "+str(cont[7])      

		
arc =Archivo()
arc.leerUsuarios("C:\Users\jose_\Documents\universidad\proyecto_edd\\archivosEntradaPrueba\Usuarios.csv")
#arc.leerNaves("C:\Users\jose_\Documents\universidad\proyecto_edd\\archivosEntradaPrueba\\naves.csv")
#arc.leerJuegos("C:\Users\jose_\Documents\universidad\proyecto_edd\\archivosEntradaPrueba\juegos.csv")
#arc.leerjuegoActual("C:\Users\jose_\Documents\universidad\proyecto_edd\\archivosEntradaPrueba\juegoActual.csv")