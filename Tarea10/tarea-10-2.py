def suma(elementos):
    resultado = []
    suma = 0
    for e in elementos:
        if not e % 2 == 0:
            resultado.append(e)
            suma +=e
    
    return resultado,suma


lista = [3,1,4,10,9,6,15]
re,su = suma(lista)
print(re,su)
        