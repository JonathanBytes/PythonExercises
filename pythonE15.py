from math import pi

def eVolume(r):
    return round(4*pi*r**3/3,2)

r = int(input('Radio de la esfera: '))
print('El volumen de la esfera es:',eVolume(r))
