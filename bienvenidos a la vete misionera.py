def agregar_paciente(veterinaria, pacientes, paciente): #funcion para agregar nuevos pacientes
    pacientes.append(paciente)
    print("Ya tenemos un nuevo amiguito en la vete!")

def mostrar_pacientes(pacientes): #Muestra los pacientes de la lista
    if not pacientes:
        print("No hay pacientes registrados")
        return

    for paciente in pacientes:
        print(f"ID: {paciente['id']}, Nombre: {paciente['nombre']}, Especie: {paciente['especie']}, Nativo: {paciente['nativo']}")

def consultar_paciente(pacientes, id_paciente): #busca y recopila la informacion de un paciente por su ID
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            return paciente
    return None

def modificar_paciente(pacientes, id_paciente, nuevo_paciente): #modifica los datos de un paciente
    for i, paciente in enumerate(pacientes):
        if paciente['id'] == id_paciente:
            pacientes[i] = nuevo_paciente
            print("Modificaste los datos exitosamente")
            return True
    print("Paciente no encontrado.")
    return False

def eliminar_paciente(veterinaria, pacientes, pacientes_eliminados, id_paciente): #elimina todos los datos de un ID de una lista
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            pacientes.remove(paciente)
            pacientes_eliminados.append(paciente)
            print("Registro eliminado con éxito.")
            return True
    print("Paciente no encontrado.")
    return False

def mostrar_reportes(pacientes, pacientes_eliminados): #Muestra un resumen de cuantos pacientes se registro y cuantos se eliminaron
    print(f"\nReporte de la Veterinaria:")
    print(f"Número de pacientes registrados: {len(pacientes)}")
    print(f"Número de pacientes eliminados: {len(pacientes_eliminados)}")

def main(): #Esta funcion controla y coordina las siguientes funciones de carga de datos de los pacientes
    veterinaria = None
    pacientes = []
    pacientes_eliminados = []

    while True:
        print("\nBienvenidos a la vete misionera")
        print("1. Registrar Paciente")
        print("2. Consultar Pacientes")
        print("3. Modificar Paciente")
        print("4. Eliminar Paciente")
        print("5. Mostrar Reportes")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            sexo = input("Sexo del paciente: ")
            edad = input("Edad aproximada del paciente: ")
            especie = input("Especie del paciente (perro/gato/yaguareté/tucán/coati/mono): ")
            nativo = input("¿Es nativo de la provincia de Misiones? (si/no): ")
            raza = ""
            if especie in ['perro', 'gato']:
                raza = input("Raza del paciente: ")
            enfermedad = input("Enfermedad del paciente: ")
            nombre_dueno = input("Nombre del dueño: ")
            contacto_dueno = input("Número de contacto del dueño: ")

            nuevo_paciente = {
                'id': len(pacientes) + 1,
                'nombre': nombre,
                'sexo': sexo,
                'edad': edad,
                'especie': especie,
                'nativo': nativo.lower() == 'si',
                'raza': raza,
                'enfermedad': enfermedad,
                'nombre_dueno': nombre_dueno,
                'contacto_dueno': contacto_dueno
            }

            agregar_paciente(veterinaria, pacientes, nuevo_paciente)

        elif opcion == "2":
            mostrar_pacientes(pacientes)

        elif opcion == "3":
            id_modificar = int(input("Ingrese el ID del paciente a modificar: "))
            paciente_existente = consultar_paciente(pacientes, id_modificar)
            if paciente_existente:
                nuevo_nombre = input("Nuevo nombre del paciente: ")
                nuevo_sexo = input("Nuevo sexo del paciente: ")
                nuevo_edad = input("Nueva edad aproximada del paciente: ")
                nuevo_especie = input("Nueva especie del paciente (perro/gato/yaguareté/tucán/coati/mono): ")
                nuevo_nativo = input("¿Es nativo de la provincia de Misiones? (si/no): ")
                nuevo_raza = ""
                if nuevo_especie in ['perro', 'gato']:
                    nuevo_raza = input("Nueva raza del paciente: ")
                nuevo_enfermedad = input("Nueva enfermedad del paciente: ")
                nuevo_nombre_dueno = input("Nuevo nombre del dueño: ")
                nuevo_contacto_dueno = input("Nuevo número de contacto del dueño: ")

                nuevo_paciente = {
                    'id': id_modificar,
                    'nombre': nuevo_nombre,
                    'sexo': nuevo_sexo,
                    'edad': nuevo_edad,
                    'especie': nuevo_especie,
                    'nativo': nuevo_nativo.lower() == 'si',
                    'raza': nuevo_raza,
                    'enfermedad': nuevo_enfermedad,
                    'nombre_dueno': nuevo_nombre_dueno,
                    'contacto_dueno': nuevo_contacto_dueno
                }

                modificar_paciente(pacientes, id_modificar, nuevo_paciente)
            else:
                print("Paciente no encontrado.")

        elif opcion == "4":
            id_eliminar = int(input("Ingrese el ID del paciente a eliminar: "))
            eliminar_paciente(veterinaria, pacientes, pacientes_eliminados, id_eliminar)

        elif opcion == "5":
            mostrar_reportes(pacientes, pacientes_eliminados)

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main()