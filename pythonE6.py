# numbers = input("Hola qué hace, separe con erres: ")
# list = numbers.split("r")
# tupla = tuple(list)
# print(tupla,list)
#
# lista1 = [2,3,4,5,6,7,8,9,10,11,12]
# lista2 = [lista1, 'Santiago', 'Estupiñán']
# print(lista2)
#
from datetime import datetime

diasMeses = tuple([0,31,28,31,30,31,30,31,31,30,31,30,31])

def quitarGuiones(fecha):
    return fecha.split("-")

def diasTrans(fecha):
# Días transcurridos hasta hoy
    diasdelmes = 0
    
    for i in range(1,int(fecha[1])):
        diasdelmes = diasMeses[int(fecha[1])-i] + diasdelmes
   
    return (int(fecha[2]) + diasdelmes)

fechayHora = str(datetime.today())
list = fechayHora.split(" ")
fecha = quitarGuiones(list[0]) 
print("Día:",fecha[2],"\nMes:",fecha[1],"\nAño:",fecha[0])
print("Días transcurridos hasta hoy:",diasTrans(fecha))

cumple = input("Cumpleaños separado con guiones (MM-DD): ")
cumpleaños = "2022-"+cumple
cumpleLista = quitarGuiones(cumpleaños)
print("Día:",cumpleLista[2],"\nMes:",cumpleLista[1],"\nAño:",cumpleLista[0])
if diasTrans(cumpleLista) < diasTrans(fecha):
    print("Días faltantes para mi cumpleaños:",365+diasTrans(cumpleLista)-diasTrans(fecha))
else:
    print("Días faltantes para mi cumpleaños:",diasTrans(cumpleLista)-diasTrans(fecha))
