print("")
print("Gutierrez Torres Paola 3W")
print(" ")
#llenamos diccionario
asignaturas = ['Matemáticas', 'español', 'ecosistemas', 'ingles']

notas = {}

#bucle for
for asignatura in asignaturas:
    nota = input(f"Escribe tu calificion en {asignatura}: ")
    notas[asignatura] = nota

for asignatura, nota in notas.items():
    print(f"En {asignatura} sacaste {nota}") #imprimimos mensaje 
