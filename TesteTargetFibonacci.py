'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 
e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
 onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
  avisando se o número informado pertence ou não a sequência.
'''

def fib(x):
    fibonacci = 0

    for i in range(x):
        if i == 0:
            fibonacci = 0
        if i < 3:
            fibonacci = 1
        else:
            fibonacci = fibonacci + fib(i - 1)
    return(fibonacci)

def main():
    numero = int(input("Digite um número (inteiro e maior que zero) e descubra se ele existe na sequência de Fibonacci: "))
    fibonacci = 0
    base = 0
    while fibonacci <= numero:
        fibonacci = fib(base)
        if numero == fibonacci:
            print("O numero escolhido está dentro da sequencia de Fibonacci!!")
            break
        else:
            base += 1
    if fibonacci > numero:
        print("O número escolhido não está dentro da sequencia de Fibonacci!!")
        



if __name__ == '__main__':
    main()