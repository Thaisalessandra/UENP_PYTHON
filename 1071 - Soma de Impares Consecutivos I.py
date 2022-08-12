x = int(input())
y = int(input())
cont = 0
impar = cont
if x < y:
    cont = x
    while cont < y:

        if cont % 2 != 0:
            impar = cont
            impar = impar + cont
            cont = cont + 1
            print(impar)
        else:
            cont = cont + 1


elif y < x:
    cont = y+1
    while cont < x:
        if cont % 2 != 0:
            impar = impar + cont

            cont = cont + 1
        else:
            cont = cont + 1
print(impar)
