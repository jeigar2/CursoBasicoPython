def palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    cadena_invertida = cadena[::-1]
    return cadena == cadena_invertida

def run():
    texto = input("introduce un texto:")
    if palindromo(texto):
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == "__main__":
    run()