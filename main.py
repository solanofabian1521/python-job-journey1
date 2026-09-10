def registrar_candidato(nombre, edad):

    if edad >= 18:
        candidatos.append(nombre)
        return "Candidato " + nombre + " registrado correctamente. "
    else: 
           
        return nombre + " no cumple con la edad miníma. " 

candidatos = []

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

resultado = registrar_candidato(nombre,edad)

print(resultado) 

print("\n===== CANDIDATOS REGISTRADOS =====")

for candidato in candidatos: 
    print(candidato)

    