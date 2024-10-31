print(" ")
print("Gutierrez Torres Paola 3W")
print(" ")

#llenamos una lista con las materias
thislist = ["español", "matematicas", "ecosistemas", "ingles", "humanidades"]
print(thislist)
#pedimos al usuario ingresar sus calificaciones
print(input("Escribe tu calificacion en español:"))
print(input("Escribe tu calificacion en matematicas:"))
print(input("Escribe tu calificacion en ecosistemas:"))
print(input("Escribe tu calificacion en ingles:"))
print(input("Escribe tu calificacion en humanidades:"))

thislist = ["español", "matematicas", "ecosistemas", "ingles", "humanidades"]
del thislist[0] #se elimina el primer valor para que no se imprima
del thislist[2] #se elimina el segundo valor para que no se imprima
print(thislist) #imprimimos la lista sin esos dos valores 

print("Reprobaste matematicas, ecosistemas y humanidades, debes recursarlas.") #muestra mensaje
print(" ")