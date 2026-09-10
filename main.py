print("Version nueva")

def registrar_candidato(nombre, edad):

    if edad >= 18:
        candidatos.append(nombre)
        return "Candidato " + nombre + " registrado correctamente. "
    else: 
           
        return nombre + " no cumple con la edad miníma. " 

candidatos = []


while True:

    print("\n===== JOBHUB =====")
    print("1. Registrar candidato")
    print("2. Ver candidatos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "3":
        break 

    elif opcion == "1":

        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        resultado = registrar_candidato(nombre,edad)

        print(resultado) 

    elif opcion == "2":
        if len(candidatos) == 0:
            print("No hay candidatos registrados.")
        else:
            for candidato in candidatos: 
                print(candidato)
    else:
        print("Opción no válida. Intente nuevamente.")