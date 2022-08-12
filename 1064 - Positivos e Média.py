lista={}
a=0
soma=0
positivos=0
positivossoma=0
while a < 6:
    lista[a]=float(input())
    b=lista[a]
    soma=soma+b
    if lista[a] > 0:
        positivos=positivos+1
        positivossoma=positivossoma+b
        a=a+1
    else:
        a = a + 1
media=positivossoma/positivos
print(positivos,"valores positivos")
print("%.1f"%media)
