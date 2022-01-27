from math import pi

def circleArea(radius):
    return round(pi*radius**2,2)

radius=eval(input("Ingrese el radio del círculo el cual quiere conocer su área: "))
print("El área del círculo es:",circleArea(radius))
