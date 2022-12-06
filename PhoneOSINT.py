import phonenumbers
from phonenumbers import geocoder

def main():
	
	print("\n\nCreado por: RedLineFB")
	print("\nInstagram: facundo_betancur97\n")
	
	num= input("Ingrese un numero con el(+) incluido: ")
	funcionnum= phonenumbers.parse(num)	#Se convierte al formato de número de teléfono
	ubigeo=geocoder.description_for_number(funcionnum,"es") #Para obtener ubicación del número de teléfono
	print("\nLa geolocalizacion del numero es de: ", ubigeo)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
