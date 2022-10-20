""" Forzando a python a tipado estático
    Static Typing with pytho.
"""
from typing import Dict, List
# a: int = 5
# b: str = 'Hola mundo'
# c: bool = True
# d: list = [4,]
# e: tuple = ('uno','dos')
# c = 9
# print(type(c))

def suma(a: bool, b: int) -> int:
    return a + b

print(suma(2, 2))