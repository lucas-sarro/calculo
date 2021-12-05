def deriva(func):
    print(f'Derivou a função {func}')


def leia_equacao(msg):
    eq = input(msg)
    eq = eq.replace(' ', '')
    for l in eq:
        if not l.isalpha() and not l.isnumeric() and l not in '+-/*':
            print('Equação inválida...')
        else:
            return eq


def deriva_ordem(func, quant):
    for c in range(0, quant):
        func = deriva(func)
    
    return func 