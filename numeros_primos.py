def es_divisible(numero, divisor):
    return numero % divisor == 0


def es_primo(numero):
    for contador in range(2,numero):
        if es_divisible(numero, contador):
            return False
    return True


def run():
    primos = []
    limite = int(input("Introduce el límite de número primos a estudiar: "))
    for contador in range(2,limite):
        if es_primo(contador):
            print(str(contador) + " 'es primo'")
            primos.append(contador)
        else:
            print(str(contador))
    print ("Se han encontrado " + str(len(primos)) + " números primos en total")
    print (str(primos))

if __name__ == "__main__":
    run()