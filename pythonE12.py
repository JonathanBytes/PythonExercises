import calendar
from datetime import datetime

today = str(datetime.today()).split(" ")
date = today[0].split('-')
hour = today[1]

userChoice = "Y" 
print('Obtenga los días de un mes específico de un año y mes dado por el usuario. (Si desea puede obtener el mes actual)\n')
userChoice = input('¿Desea ingresar un año y mes personalizado? (Y/n): ')

if userChoice == "Y" or userChoice == "y" or userChoice == "":
    year = eval(input('\n\tIngrese el año: '))
    month = eval(input('\tIngrese el mes: '))
    print("\n",calendar.month(year,month))
else:
    print("\n",calendar.month(int(date[0]),int(date[1])))
