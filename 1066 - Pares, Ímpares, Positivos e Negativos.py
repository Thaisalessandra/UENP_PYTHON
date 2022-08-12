pares = 0
impar = 0
cont = 0
positivos = 0
negativo = 0
while cont < 5:
    n = int(input())
    if n % 2 == 0:
        pares = pares + 1
        if n > 0:
            positivos = positivos + 1
            cont = cont + 1
        elif n < 0:
            negativo = negativo + 1
            cont = cont + 1

    if n % 2 != 0:
        impar = impar + 1
        if n > 0:
            positivos = positivos + 1
            cont = cont + 1
        elif n < 0:
            negativo = negativo + 1
            cont = cont + 1
    elif n == 0:
        cont = cont + 1
print(pares, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
