def f_potencia(potencia):
    print("2 elevado a " + str(potencia) + " es igual a " + str(2**potencia))
    return 2**potencia


def run():
    i = 0
    while f_potencia(i) < 1000:
        i += 1


if __name__ == "__main__":
    run()