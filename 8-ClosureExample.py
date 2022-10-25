
from __future__ import division


def make_repeater_of(n: int):
    def repeter(string: str):
        #Si nos ingresa un parámetro que no sea string
        assert type(string) == str, "Solo puedes utilizar cadenas de texto"
        return string * n

    return repeter


def make_division_by(divisor: int):
    assert type(divisor) != int, "You have to add an int number"
    def make_dividendo(dividendo: int) -> int:
        #return int(dividendo / divisor)
        return dividendo // divisor #Recuerda que la // me devuelve solo en int
    
    return make_dividendo


def run():
    #repeat_5 = make_repeater_of(5)
    #print(repeat_5('Fabian '))
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run()
