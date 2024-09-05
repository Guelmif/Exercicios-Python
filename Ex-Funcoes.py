#Exer1-Programa - Calculadora simples : O usuário escolhe a 
#operação desejada e o programa calcula o resultado:
#As funções recebem os operadores, executa a operação e
#imprime o resultado, portanto, não tem retorno.
#Funções : menu(), somar(), subtrair(), multiplicar() e
#dividir()

def soma(x,y):
    print("Resultado da Soma = " , x+y)

def sub(x,y):
    print("Resultado da Subtração = " , x-y)

def mult(x,y):
    print("Resultado da Multiplicação = " , x*y)

def div(x,y):
    print("Não é possivel realizar divisão com 0 !!" if x == 0 or y == 0 else f"Resultado da Divisão: {x/y}")


def menu():
    nmr1 = float(input("Digite o primeiro numero:\n"))
    nmr2 = float(input("Digite o segundo numero:\n"))
    op = int(input("01.Somar | 02.Subtrair | 03.Multiplicar | 04.Dividir\n"))

    match op:
        case 1:
            soma(nmr1, nmr2)
        case 2:
            sub(nmr1, nmr2)
        case 3:
            mult(nmr1, nmr2)
        case 4:
            div(nmr1, nmr2)
                 

print("Escolha uma das operações abaixo:")
menu()
    