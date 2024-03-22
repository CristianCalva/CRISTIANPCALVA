 # Diccionario
datos_personales = {
    "Nombre":"Cristian Calva",
    "Edad":"28",
    "Ciudad":"Lago Agrio",
    "Sexo":"Masculino",
    "Celular":"0967816221",
    "Correo electronico":"cp.calvaa@uea.edu.ec"
}

print(datos_personales)

# Modificar ciudad
datos_personales["Ciudad"] = "Manabi"
print(datos_personales)

# Agregar profecion
datos_personales["Profecion"] = "Estudiante Univercitario de la UEA"
print(datos_personales)

if "telefono" in datos_personales:
    print("telefono existe en el diccionario")
else:
    print("telefono NO existe en el diccionario")

# Eliminar correo
datos_personales.pop("Correo electronico")
print(datos_personales)