def es_divisible(numero, divisor):
    return numero % divisor == 0

def es_primo(numero):
    for contador in range(2,numero):
        if es_divisible(numero, contador):
            return False
    return True

def run():
    limite = int(input("introduce el límite de número primos ha estudiar: "))
    for contador in range(2,limite):
        if es_primo(contador):
            print(str(contador) + " es primo")
        else:
            print(str(contador))

if __name__ == "__main__":
    run()