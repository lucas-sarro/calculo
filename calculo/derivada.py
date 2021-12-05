def deriva(func):
    print(f'Derivou a função')


def leia_equacao(eq):
    eq = eq.replace(' ', '')
    for l in eq:
        print(l)


def deriva_ordem(func, quant):
    for c in range(0, quant):
        func = deriva(func)
    
    return func 