n = int(input('Ingrese un entero: '))
m = str(n); a = int(2*m); b = int(3*m)
print('%s + %s%s + %s%s%s = ' %(m,m,m,m,m,m), end='')
print(n+a+b)

# Alternativa
print(n+n*11+n*111)
