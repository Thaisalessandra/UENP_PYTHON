import math

v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])

delta = ((b**2)-4*a*c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1=(- b + math.sqrt(delta) )/(2 * a)
    R2=(- b - math.sqrt(delta) )/(2 * a)
    print("R1 =","%.5f" % R1)
    print("R2 =", "%.5f" % R2)
