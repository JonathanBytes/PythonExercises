from datetime import date

def datos():
    year = int(input('Año: '))
    month = int(input('Mes: '))
    day = int(input('Día: '))
    return date(year,month,day) 

def difdates():
    print ('Ingrese la primera fecha.')
    date1 = datos()
    print ('Ingrese la segunda fecha.')
    date2 = datos()
    print((date2 - date1).days)

difdates()

# # Fecha y hora
# x = datetime(2020,1,1,2,1,0)
# # Solo fecha
# x = date(2020,1,1)
# # Solo hora
# x = time(14,2,0)
# print(x)
