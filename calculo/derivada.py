def deriva(func):
    print(f'Derivou a função')


def leia_equacao():
    pass


def deriva_ordem(func, quant):
    for c in range(0, quant):
        func = deriva(func)
    
    return func 