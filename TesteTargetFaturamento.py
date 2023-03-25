'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.'''

import json


def menorValor(lista):
    listaOrdenada = sorted(lista)
    while listaOrdenada[0] == 0:
        listaOrdenada.pop(0)
    return(listaOrdenada[0])

def maiorValor(lista):
    listaOrdenada = sorted(lista)
    while listaOrdenada[0] == 0:
        listaOrdenada.pop(0)
    return(listaOrdenada[-1])

def diasAcimaMedia(lista):
    listaOrdenada = sorted(lista)
    while listaOrdenada[0] == 0:
        listaOrdenada.pop(0)
    media = sum(listaOrdenada)/len(listaOrdenada)
    soma = 0
    for numero in listaOrdenada:
        if numero > media:
            soma += 1
    return(soma)


def main():
    with open("dados.json") as Base:
        Dados = json.load(Base)

    valores = []
    for i in range(len(Dados)):
        valores.append(Dados[i]["valor"])
    
    valorMinimo = round(menorValor(valores), 2)
    valorMaximo = round(maiorValor(valores), 2)
    somaDias    = round(diasAcimaMedia(valores), 2)

    print(f"Menor valor de faturamento occorido no mês: R${valorMinimo}")
    print(f"Maior valor de faturamento ocorrido no mês: R${valorMaximo}")
    print(f"Total de dias que tiveram faturamento acima da média do mês: {somaDias}")


if __name__ == '__main__':
    main()
