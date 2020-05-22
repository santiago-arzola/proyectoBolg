del  matraz de  importación  Frasco
desde la  importación de frasco  render_template 

aplicación  =  Frasco ( __nombre__ )

@ app . ruta ( "/" )
def  url_principal ():
	return  render_template ( "index.html" )
	#return "<h1> Hola mundo </h1>"

@ app . ruta ( "/ café" )
def  url_coffee ():
 	tipos  = [
 		"Americano" ,
 		"Latté"
 	]
 	return  render_template ( "coffee.html" , tipos = tipos , nombre = "Café" )

if  __name__  ==  "__main__" :
	aplicación . ejecutar ( depurar = verdadero )
