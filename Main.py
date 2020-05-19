cantCasos= int(input("Ingrese la cantidad de casos a resolver: "))
lista =[]
bandera = False
bandera2 = False

for x in range(cantCasos):
    print("Ingrese el caso: ",x+1)
    numeroIngreso = int(input("Intruducir un numero que sea de 4 dígitos y que tenga al menos 2 digitos diferentes: "))
    if numeroIngreso == 6174:
        bandera = True
    if numeroIngreso == 1111 or numeroIngreso == 2222 or numeroIngreso == 3333 or numeroIngreso ==4444 or numeroIngreso ==5555 or numeroIngreso == 6666 or numeroIngreso ==7777 or numeroIngreso == 8888 or numeroIngreso ==9999 or numeroIngreso == 0000:
        bandera2 =True
    numeroResta =0



