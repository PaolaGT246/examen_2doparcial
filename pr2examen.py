print(" ")
print("Gutierrez Torres Paola 3W")
print(" ")

#llenamos diccionario
creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

#total por ahora
total_creditos = 0

#agregamos for para crear un bucle con el diccionario
for asignatura, creditos in creditos_asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos")
    total_creditos += creditos #se realiza la suma

print(f"Número total de créditos del curso: {total_creditos}") #imprime mensaje
