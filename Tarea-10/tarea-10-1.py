

paises = []
cantidad = int(input("Cuantos paises va a ingresar?: "))

for i in range(cantidad):
    pais = input("Ingrese el pais:")


    if not paises.count(pais):
        paises.append(pais)
    
    
    paises.sort()


print(paises)