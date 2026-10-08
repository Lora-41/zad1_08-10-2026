import math

r = float(input("Въведи радиус "))

area = r * r * math.pi
perimetur = 2 * r * math.pi

print (f"Лицето е  {area:.3f}")
print (f"Периметъра е {perimetur:.3f}")