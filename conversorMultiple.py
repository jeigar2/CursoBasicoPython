menu = """
Bienvenido al conversor de monedas

1 - Euros a Dolares
2 - Dolares a Euros
3 - Bitcoin a Euros

Elige una opción (1,2,3): 

"""
opcion = int(input(menu))

if opcion == 1: #Euros a Dolares
    moneda = input('¿Cuántos Euros tienes? ')
    moneda = float(moneda)
    conversor = 1.1597
    prefijo = "$"
    sufijo = ""
elif opcion == 2: #Dolares a Euros
    moneda = input('¿Cuántos Dolares tienes? ')
    moneda = float(moneda)
    conversor = 0.8623
    prefijo = ""
    sufijo = "€"
elif opcion == 3: #Bitcoin a Euros
    moneda = input('¿Cuántos Bitcoin tienes? ')
    moneda = float(moneda)
    conversor = 49387.466
    prefijo = ""
    sufijo = "€"
else: 
    print('Escribe una opción correcta, por favor (1,2,3) ')

cambio = moneda * conversor
print('Tienes '+ prefijo + str(round(cambio, 2)) + sufijo)