def rafael(x, y):
    r = 0
    r = (3 * x) ** 2 + (y ** 2)
    return (r)





def beto(x, y):
    b = 0
    b = 2 * (x ** 2) + ((5 * y) ** 2)
    return (b)




def carlos(x, y):
    c = 0
    c = (-100 * x) + (y ** 3)
    return (c)



n=int(input())
for n in range(n):
    v = input().split()
    x = int(v[0])
    y = int(v[1])
    if rafael(x, y) > beto(x, y) and rafael(x, y) > carlos(x, y):
        print("Rafael ganhou")
    elif beto(x, y) > rafael(x, y) and beto(x, y) > carlos(x, y):
        print("Beto ganhou")
    elif carlos(x, y) > rafael(x, y) and carlos(x, y) > beto(x, y):
        print("Carlos ganhou")
