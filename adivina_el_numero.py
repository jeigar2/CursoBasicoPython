import random

def run ():
    min = 1
    max = 100
    intentos = 0
    numero = 0
    numero_aletorio = random.randint(min, max)
    while numero != numero_aletorio:
        intentos += 1
        numero = int(input("Escoge un número entre " + str(min) + " y " + str(max) + ": "))
        if (numero < numero_aletorio):
            min = numero
            print ("mayor")
        else:
            max = numero
            print ("menor")
    print ("¡Ganaste! el número era: '" + str(numero_aletorio) + "'. Total intentos: " + str(intentos))


if __name__ == "__main__":
    run()

