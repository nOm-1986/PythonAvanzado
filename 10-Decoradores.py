"""Decoradores:
    Función que recibe como parámetro otra función, le añade cosas,
    y retorna una función diferente.
    Es una función que le añade superpoderes a otra función. ->
    Retorna una función diferente.

    Al ser un patrón común lo podemos mejorar con azucar sintactico.

    CUALIDAD DE UN DECORADOR:
        * - Que le añade cosas a una función original.
"""

def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura


# def saludo():
#     print('Hola')

@decorador
def saludo():
    print('Hola')


#saludo = decorador(saludo)
saludo()


def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje' 

print(mensaje('fabián'))