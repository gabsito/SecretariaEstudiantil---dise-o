import funciones as fn

dic = None
filename = 'alumnado.csv'
msg = '''
**************************************************
*                                                *
*                  Proyecto                      *
*                                                *
**************************************************

Opciones:

    1. Cargar datos.
    2. Agregar estudiante.
    3. Buscar estudiante.
    4. Mostrar los alumnos de un curso.
    5. Ayuda.
    
    Escriba "salir" para salir del programa
'''

print(msg)

while True:
    op = input('Opcion: ')

    if op == '1':
        if dic is None:
            dic = fn.leerArchivo(filename)
        else:
            print('Actualizando datos en el sistema.')
            dic = fn.leerArchivo(filename)
        print(dic)

    elif op == '2':
        if dic is None:
            print('No hay datos cargados en el sistema.')
        else:
            dic = fn.agregarEstudiante(filename)

    elif op == '3':
        if dic is None:
            print('No hay datos cargados en el sistema.')
        else:
            cedula = input('Ingrese cedula: ')
            fn.buscarEstudiante(cedula, dic)

    elif op == '4':
        if dic is None:
            print('No hay datos cargados en el sistema.')
        else:
            curso = input('Ingrese curso: ')
            fn.alumnos_curso(curso, dic)

    elif op == '5':
        fn.ayuda()

    elif op.lower() == 'salir':
        break

    else:
        print('Opcion no valida')

print('Fin del programa.')
