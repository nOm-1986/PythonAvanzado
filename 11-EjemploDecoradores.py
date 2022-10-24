""" Ejemplo de decorador
"""
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper


@execution_time
def random_func():
    # _ That mean that it isnt importan the varable
    for _ in range(1, 10000000):
        pass


@execution_time
def suma(a: int, b: int)->int:
    print(a + b)


@execution_time
def saludo(nombre="fabo"):
    print(f'Hola {nombre}')


suma(13, 21)
random_func()
saludo('María José')
