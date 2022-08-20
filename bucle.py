def run():
    LIMITE = 1000
    BASE = 3
    
    contador = 0
    potencia_base = BASE**contador
    while potencia_base < LIMITE:
        print(str(BASE) + ' elevado a ' + str(contador) + ' es igual a: ' + str(potencia_base))
        contador+=1
        potencia_base = BASE**contador
    
if __name__ == "__main__":
    run()