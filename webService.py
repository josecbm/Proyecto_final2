from flask import Flask , request
import arbolBinario


app = Flask("servidorBatle")

arbol  = arbolBinario.Binario()
@app.route('/metodoprueba',methods=['POST']) 
def hello():
	parametro = str(request.form['dato'])
	dato2 = str(request.form['dato2'])
	return "Hola " + str(parametro) + "!"+str(dato2)
	
@app.route('/serveltLogin',methods=['POST']) 
def serveltLogin():
	usuario = str(request.form['usuario'])
	passw = str(request.form['passw'])
	if arbol.proO(arbol.getRaiz(),usuario,passw)!=None:
		print "true"
		return "true"
	else: return "False" 

@app.route('/serviceCrearUsuario',methods=['POST']) 
def crearUsuario():
	usuario = str(request.form['usuario'])
	print usuario
	passw = str(request.form['passw'])
	print passw
	conexion = str(request.form['conexion'])
	print conexion
	print arbol.agregar(usuario,passw,conexion)
	return "True"

	#arbolBinario.Binario().agregar(usuario,passw,conexion)
	

@app.route('/ServicePrueba',methods=['POST']) 
def prueba():
	
	return "gola"
@app.route('/serviceImagen1',methods=['POST']) 
def prueba():
	arbol.preOrden(b.getRaiz())
	arbol.grafica = b.grafica + "}"
	arbol.ejecutar(b.grafica,"arbol")
	return True
	
@app.route("/")
def hello2():
    return "Hello hueco!"

if __name__ == "__main__":
    app.run()


