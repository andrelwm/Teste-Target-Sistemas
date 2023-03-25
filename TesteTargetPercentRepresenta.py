'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
'''

def main():
    faturamento = {"SP" : 67836.43, "RJ" : 36678.66, "MG" : 29229.88, "ES" : 27165.48, "OUTROS" : 19849.53}
    estados = list(faturamento.keys())
    valores = list(faturamento.values())

    faturamentoTotal = sum(valores)
    percentRepresenta = []
    for valor in valores:
        percent = round((valor/faturamentoTotal) * 100, 2)
        percentRepresenta.append(percent)
    
    print("Porcentagem de Represetação por Estado:")
    for i in range(len(percentRepresenta)):
        print(f"{estados[i]} --> {percentRepresenta[i]}%")

if __name__ == '__main__':
    main()
