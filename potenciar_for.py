def f_potencia(potencia):
    print("2 elevado a " + str(potencia) + " es igual a " + str(2**potencia))
    return 2**potencia

def run():

    for contador in range(20):
        f_potencia(contador)

if __name__ == "__main__":
    run()