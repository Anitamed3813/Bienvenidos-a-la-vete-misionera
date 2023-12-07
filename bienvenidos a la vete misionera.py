#(Deberá crear una aplicación de consola que simulara un “sistema de gestión de
#pacientes de una veterinaria”, que permita:
#- Registrar un paciente detallando su nombre, sexo, edad aproximada,
#especie(canino/felino), rasgos, enfermedad, nombre dueño,
#numero de contacto.
#- Consultas de registros.
#- Modificar el registro de un paciente.
#- Eliminar el registro de un paciente.
#- Al finalizar, el programa deberá mostrar reportes de la cantidad de pacientes registrados y eliminados.)

def agregar_paciente( pacientes, paciente): #defino pacientes a aagregar
    pacientes.append(paciente)
    print("¡Nuevo amiguito registrado en la vete!")

def mostrar_pacientes(pacientes): #defino los pacientes en la lista
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    for paciente in pacientes:
        print(f"ID: {paciente['id']}, Nombre: {paciente['nombre']}, Especie: {paciente['especie']}, Nativo: {paciente['nativo']}")

def consultar_paciente(pacientes, id_paciente): #define la consulta de pacientes
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            return paciente
    return None

def modificar_paciente(pacientes, id_paciente, nuevo_paciente): #define el paciente a modificar
    for i, paciente in enumerate(pacientes):
        if paciente['id'] == id_paciente:
            pacientes[i] = nuevo_paciente
            print("Registro modificado con éxito.")
            return True
    print("Paciente no encontrado.")
    return False

def eliminar_paciente( pacientes, pacientes_eliminados, id_paciente): #define el paciente a eliminar, si existe
    for paciente in pacientes:
        if paciente['id'] == id_paciente:
            pacientes.remove(paciente)
            pacientes_eliminados.append(paciente)
            print("Registro eliminado con éxito.")
            return True
    print("Paciente no encontrado.")
    return False

def mostrar_reportes(pacientes, pacientes_eliminados): #define la muestra de reporte
    print(f"\nReporte de la Veterinaria:")
    print(f"Número de pacientes registrados: {len(pacientes)}")
    print(f"Número de pacientes eliminados: {len(pacientes_eliminados)}")

def main(): # inicia la funcion de gestion de todas las demas funciones
    veterinaria = None
    pacientes = []
    pacientes_eliminados = []

    while True: #funcion de inicio de ingreso de datos
        print("\nBienvenidos a la vete de la selva misionera")
        print("1. Registrar Paciente")
        print("2. Consultar Pacientes")
        print("3. Modificar Paciente")
        print("4. Eliminar Paciente")
        print("5. Mostrar Reportes")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":  #si se elige introducir un nuevo paciente, se debe rellenar los siguientes datos
            nombre = input("Nombre del paciente: ")
            sexo = input("Sexo del paciente: ")
            edad = input("Edad aproximada del paciente: ")
            especie = input("Especie del paciente (perro/gato/yaguareté/tucán/coati/mono): ")
            nativo = input("¿Es nativo de la provincia de Misiones? (si/no): ")
            raza = ""
            if especie in ['perro', 'gato']: #si el paciente es perro o gato, debera especificar la raza del mismo
                raza = input("Raza del paciente: ")
            enfermedad = input("Enfermedad del paciente: ")
            nombre_dueno = input("Nombre del dueño: ")
            contacto_dueno = input("Número de contacto del dueño: ")

            nuevo_paciente = { #se guarda nuevo paciente
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

            agregar_paciente( pacientes, nuevo_paciente)

        elif opcion == "2": # si se elige la opcion 2, se mostrara el registro 
            mostrar_pacientes(pacientes)

        elif opcion == "3": # si se elige la opcion 3, se accede a modificar el registro, en caso de existir
            id_modificar = int(input("Ingrese el ID del paciente a modificar: "))
            paciente_existente = consultar_paciente(pacientes, id_modificar)
            if paciente_existente: #si el ID es correcto, permite modificar los datos
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

                nuevo_paciente = { #guarda los datos modificados del paciente
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
                print("Paciente no encontrado.") #si se equivoca de ID o no existe, se imprime que no se encuentra

        elif opcion == "4": # la opcion 4 permite eliminar el regidtro del ID solicitado
            id_eliminar = int(input("Ingrese el ID del paciente a eliminar: "))
            eliminar_paciente( pacientes, pacientes_eliminados, id_eliminar)

        elif opcion == "5": #la opcion 5 muestra el reporte de los registros nuevos y los eliminados
            mostrar_reportes(pacientes, pacientes_eliminados)

        elif opcion == "6": #salir del sistema
            mostrar_reportes(pacientes, pacientes_eliminados)
            print("Gracias por visitar la vete, nos vemos pronto!")
            break

        else: #si se introduce una opcion incorrecta, se imprime por pantalla
            print("Opción no válida. Por favor, ingrese una opción válida.")


if __name__ == "__main__":
    main() #fin del programa de control
