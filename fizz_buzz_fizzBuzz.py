def es_divisible(numero, divisor):
    return numero % divisor == 0


def es_divisible2(numero, divisor1, divisor2):
    return numero % divisor1 == 0  and numero % divisor2 == 0


def filtrarNumero(numero):
    if es_divisible2(numero, 3, 5):
        return "'fizzBuzz'"
    elif es_divisible(numero, 3):
        return "'fizz'"
    elif es_divisible(numero, 5):
        return "'buzz'"
    else:
        return str(numero)


def run():
    contador = 0
    LIMITE = int(input("introduce el número límite del juego: "))
    while (contador < LIMITE):
        contador += 1
        if contador == 42:
            print ("cuarenta y dos")
            break
        elif contador % 7 == 0:
            continue
        print(filtrarNumero(contador))


if __name__ == "__main__":
    run()
