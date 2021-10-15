def run():
    for contador in range(1,100):
        if contador % 2 != 0:
            continue
        print(contador)
    texto = input("introduce un texto: ")
    for caracter in texto:
        if caracter == 'o':
            break;
        print(caracter)

if __name__ == "__main__":
    run()