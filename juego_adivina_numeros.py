# Juego que adivina el número que estás pensando

numPensado = 0
numAProbar = 0
vecesPreguntadas = 0
maxVecesPreguntadas = 6

numLimiteInferior = 1
numLimiteSuperior = 10

tempLimiteInferior = numLimiteInferior # sirve para los cálculos
tempLimiteSuperior = numLimiteSuperior # sirve para los cálculos 

print('Piensa un número entre ' + str(numLimiteInferior) + ' y ' + str(numLimiteSuperior))
print('Voy a intentar adivinarlo en menos de ' + str(maxVecesPreguntadas) + ' veces')
print('DEBUG: Introduce el número que estás pensando')
numPensado = input()
print('DEBUG: El número a adivinar es: ' + str(numPensado))

numAProbar = numLimiteSuperior // 2 # Hacemos siempre la división entera
ultNumAProbar = 0 # Esta variable nos va a permitir verificar si estamos repitiendo el número a probar

while vecesPreguntadas < maxVecesPreguntadas:

    print('Creo que es el ' + str(numAProbar))
    print('Si es el número correcto, escribe ok, si tu número es mayor escribe M y si es menor escribe m')
    opcion = input()
    if opcion == 'ok':
          break
    elif opcion == 'M':
          tempLimiteInferior = numAProbar
          print('Le vamos a sumar: ' + str(int((tempLimiteSuperior - tempLimiteInferior)// 2)))
          numAProbar = numAProbar + ((tempLimiteSuperior - tempLimiteInferior)// 2) # le sumamos al número a probar la mitad de lo que falta para el límite superior
          if ultNumAProbar == numAProbar:
              numAProbar = numAProbar + 1
    else:
          tempLimiteSuperior = numAProbar
          print('Le vamos a restar: ' + str(int((tempLimiteSuperior - tempLimiteInferior)// 2)))
          numAProbar = numAProbar - ((tempLimiteSuperior - tempLimiteInferior)// 2) # le restamos al número a probar la mitad de lo que falta para el límite superior
          if ultNumAProbar == numAProbar:
              numAProbar = numAProbar - 1

    ultNumAProbar = numAProbar
    vecesPreguntadas = vecesPreguntadas +1

if opcion == 'ok':
    print('He acertado tu número, es el ' + str(numAProbar) + ' :)')
else:
    print('No he podido acertar tu número...')

