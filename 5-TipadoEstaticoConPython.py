""" Forzando a python a tipado estático
    Static Typing with pytho.
"""
from typing import Dict, List, Tuple
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

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 56
}

users2: Dict[str, Dict[str, int]] = {
    'Colombia': {
        'santander': 1,
        'cundinamarca': 2,
        'nariño': 3
    },

    'Colombia': {
        'santander': 1,
        'cundinamarca': 2,
        'nariño': 3
    },
}

countries: List[Dict[str, str]] = {
    {
        'name' : 'Argentina',
        'people': 45123
    },
    {
        'name' : 'Mexico',
        'people': 59842
    },
}

#Me encanta esta forma cuando son listas o diccionarios algo complejos
CoordinatesType = List[Dict[str, Tuple[int, int]]]
#Una vez creado el Alias de Tipo lo puedo referenciar en una variable.
coordinates: CoordinatesType = [
    {
        'coord1': (1, 2),
        'coord2': (3, 4)
    },
    {
        'coord1': (0, 2),
        'coord2': (5, 3)
    }
]
