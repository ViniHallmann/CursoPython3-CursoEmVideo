def aumentar(preco=0, taxa=0, formato = False):
    res = preco + (preco*taxa/100)
    return res if formato is False else moeda(res)
def diminuir(preco=0, taxa=0, formato = False):
    res = preco - (preco*taxa/100)
    return res if formato is False else moeda(res)
def dobro(preco=0, formato = False):
    res = preco*2
    return res if formato is False else moeda(res)
def metade(preco=0, formato = False):
    res =  preco/2
    return res if formato is False else moeda(res)
def moeda(preco = 0, moeda = 'R$', formato = False):
    res = f'{moeda}{preco}'.replace('.',',')
    return res if formato is False else moeda(res)

def resumo(preco = 0, taxaa = 20, taxad=12):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30)) 
    print('-'*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco,True)}')
    print(f'Metade do preco: \t{metade(preco,True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco,taxaa,True)}')
    print(f'{taxad}% de reducao: \t{diminuir(preco,taxad,True)}')
    print('-'*30)