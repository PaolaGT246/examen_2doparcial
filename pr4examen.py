print(" ")
print("Gutierrez Torres Paola 3W")
print(" ")

#pedimos al usuario llenar sus datos
nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
direccion = input("ingrese su direccion: ")
numero = input("ingrese su numero: ")

#creamos diccionario con los datos
datos = {"nombre":nombre, "edad":edad, "direccion":direccion, "numero":numero}
print(f"{datos ['nombre']} tiene {datos ['edad' ]} años, su direccion es {datos ['direccion']} y su numero de telefono es {datos ['numero']}")
#mensaje en pantalla
print(" ")