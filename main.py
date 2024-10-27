# Lista que contiene el alfabeto en mayúsculas para referencia en el cifrado y descifrado.
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
"P","Q","R","S","T","U","V","W","X","Y","Z"]

# Cadena con caracteres especiales que no se modificarán en el cifrado.
caracteres_especiales = " ,.()/;:!¡?¿)"

# Texto que será utilizado como prueba para el cifrado y descifrado.
texto_de_prueba = "Hola Mundo! Este es el cifrado Cesar."

# Desplazamiento utilizado para el cifrado (número de posiciones a desplazar).
desplazamientos = 7


# Función que aplica el cifrado César al texto dado.
def cifrarTexto(texto, desplazamiento):
	texto_en_mayuscula = texto.upper()
	texto_cifrado =""

	for letra in texto_en_mayuscula:
		if letra in alfabeto:
			#indice_original = alfabeto.index(letra)
			#print(f"Indice original de {letra}: {indice_original}")
			indice_nuevo = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
			texto_cifrado += alfabeto[indice_nuevo]
		elif letra in caracteres_especiales:
			texto_cifrado += letra
		else: 
			texto_cifrado += letra

	
	return texto_cifrado
			
    

# Ciframos el texto de prueba y lo imprimimos.
cifrado_de_prueba = cifrarTexto(texto_de_prueba,desplazamientos)
print(f"{cifrado_de_prueba}")


# Función que descifra un texto cifrado utilizando el mismo desplazamiento.
def descifrarTexto(texto, desplazamiento):
	texto_en_mayuscula = texto.upper()
	texto_descifrado = ""
	for letra in texto_en_mayuscula:
		if letra in alfabeto:
			indice_nuevo = (alfabeto.index(letra) - desplazamiento) % len(alfabeto)
			texto_descifrado += alfabeto[indice_nuevo]
		elif letra in caracteres_especiales:
			texto_descifrado += letra
		else:
			texto_descifrado += letra


	return texto_descifrado


# Desciframos el texto previamente cifrado y lo imprimimos.
print(f"{descifrarTexto(cifrado_de_prueba,desplazamientos)}")



