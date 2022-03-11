x = []
i= 0
while True:
    x.append(input(': '))
    if x[i] == 'listo':
        x.remove('listo')
        break
    i = i + 1

print(x)
