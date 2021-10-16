def conversion(nombre_moneda, conversor, prefijo, sufijo):
    moneda = input('¿Cuántos ' + nombre_moneda + ' tienes? ')
    moneda = float(moneda)
    cambio = moneda * conversor
    print('Tienes '+ prefijo + str(round(cambio, 2)) + sufijo)


menu = """
Bienvenido al conversor de monedas

1 - Euros a Dolares
2 - Dolares a Euros
3 - Bitcoin a Euros

Elige una opción (1,2,3): 

"""
opcion = int(input(menu))

if opcion == 1: #Euros a Dolares
    conversion('Euros', 1.1597,'$','')
elif opcion == 2: #Dolares a Euros
    conversion('Dolares', 0.8623,'','€')
elif opcion == 3: #Bitcoin a Euros
    conversion('Bitcoin', 49387.466,'','€')
else: 
    print('Escribe una opción correcta, por favor (1,2,3) ')
