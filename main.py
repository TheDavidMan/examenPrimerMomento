import openpyxl

estudiantes = {}

for i in range(3):
    nombre = input("Introduce el nombre del estudiante: ")
    nota = float(input(f"Introduce la nota de {nombre}: "))
    estudiantes[nombre] = nota

libro = openpyxl.Workbook()

hoja = libro.active

hoja['A1'] = 'Estudiante'
hoja['B1'] = 'Clasificación'

fila = 2

for nombre, nota in estudiantes.items():
    hoja[f'A{fila}'] = nombre
    if nota > 70:
        hoja[f'B{fila}'] = 'Bueno'
    else:
        hoja[f'B{fila}'] = 'Regular'
    fila += 1

libro.save("ejercicio3.xlsx")

print("¡Ejercicio 3 guardado en ejercicio3.xlsx!")