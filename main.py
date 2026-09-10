def registrar_candidato(nombre, edad):

    if edad >= 18:
        return "Candidato " + nombre + " registrado correctamente. "
    else: 
        return nombre + " no cumple con la edad miníma. " 

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))

resultado = registrar_candidato(nombre,edad)

print(resultado)