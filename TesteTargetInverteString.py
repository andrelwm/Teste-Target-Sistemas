'''
5) Escreva um programa que inverta os caracteres de um string.
'''

def inverteString(texto):
    return(texto[::-1])
    
def main():
    texto = input("Digite qualquer palavra e veja como ela fica quando invertida: ")

    textoInvertido = inverteString(texto)

    print(f"Você escreveu: '{texto}'")
    print(f"\nTexto invertido: '{textoInvertido}'")

if __name__ == '__main__':
    main()