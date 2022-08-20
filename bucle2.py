def f_potencia(potencia):
    BASE = 2
    potencia_base = BASE**potencia
    print(str(BASE) + " elevado a " + str(potencia) + " es igual a " + str(potencia_base))
    return potencia_base


def run():
    LIMITE = 1000
    contador = 0
    while f_potencia(contador) < LIMITE:
        contador += 1


if __name__ == "__main__":
    run()