
def leerArchivo(filename):  # Lee el archivo y lo carga en un diccionario.
    file = open(filename, 'r')
    dic = {}
    file.readline()
    for line in file:
        line = line.strip().split(',')
        dic[line[0]] = {'nombre': line[1] + ' ' + line[2], 'edad': line[3], 'curso': line[4]}
    file.close()
    print('Datos cargados en el sistema')
    return dic


def agregarEstudiante(filename):  # Permite agregar un estudiante al archivo
    op = ''
    while op.upper() != 'S':
        cedula = input('Ingrese numero de cedula: ')
        name = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        edad = input('Ingrese edad: ')
        curso = input('Ingrese curso: ')
        print('Los datos ingresados son:\n\n')
        print('\t\tCedula:', cedula)
        print('\t\tNombre:', name)
        print('\t\tApellido:', apellido)
        print('\t\tEdad:', edad)
        print('\t\tCurso:', curso)
        op = input('Desea guardar los datos? S/N: ')

    file = open(filename, 'a')
    add = f'\n{cedula},{name},{apellido},{edad},{curso}'
    file.writelines(add)
    file.close()
    print('Estudiante agregado con exito!')
    dic = leerArchivo(filename)
    return dic


def buscarEstudiante(cedula, dic: dict):  # Busca un estudiante y lo imprime
    for estudiante, data in dic.items():
        if estudiante == cedula:
            print('nombre:', data['nombre'])
            print('Edad:', data['edad'])
            print('Curso:', data['curso'])


def alumnos_curso(curso, dic):  # Imprime todos nombres y apellidos de los estudiantes de un curso
    cont = 0
    for cedula, data in dic.items():
        if data['curso'] == curso:
            print('nombre:', data['nombre'])
            cont += 1
    print(f'En {curso} hay {cont} alumnos.')


def ayuda():
    print('''Opciones:

    1. Cargar datos:              Carga los datos en el sistema.
    2. Agregar estudiante:        Nos permite agregar un estudiante.
    3. Buscar estudiante:         Busca un estudiante por su cedula.
    4. Mostrar Alumnos:           Muestra todos los alumnos de un curso ingresado. 
    5. Ayuda:                     Imprime este mensaje.
    Escriba "salir" para salir del programa
''')
