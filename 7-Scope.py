"""
Scope: alcance de las variables
    Una variable solo está disponible dentro de la región donde fue creada.
"""

x = 6

def my_func():
    #local Scope
    y = 5
    print(y)


def my_func():
    print(x)


my_func()
