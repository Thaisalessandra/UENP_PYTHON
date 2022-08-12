x=0
alcool=0
gasolina=0
diesel=0

while x != 4:
    x=int(input())

    if x == 1:
        alcool = alcool+1

    elif x ==2:
        gasolina = gasolina + 1

    elif x == 3:
        diesel=diesel+1

if x == 4:
    print("MUITO OBRIGADO")
    print("Alcool:", alcool)
    print("Gasolina:", gasolina)
    print("Diesel:", diesel)
