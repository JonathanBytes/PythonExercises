def trisuma(a,b,c):
    # a = eval(input('Primer número: '))
    # b = eval(input('Segundo número: '))
    # c = eval(input('Tercer número: '))

    suma = a + b + c

    if a == b == c:
       suma = suma * 3 

    print('%i + %i + %i ='%(a,b,c),suma)

trisuma(1,2,3)
trisuma(3,3,3)
