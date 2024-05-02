def ex10():
    valor = float(input("Digite o valor do carro: "))
    entrada = float(input("Digite a entrada: "))
    p = int(input("Digite a quantidade de parcelas: "))

    vf = valor * 1.65

    if(p > 0 and valor > 0  and entrada > 0):
        p = (vf - entrada) / p
        print("O Valor final do carro é", vf)
        print("Valor da parcela: ", p)
    else:
        print("Digite um valor valido")

def ex11():
    valor = float(input("Digite o valor para conversão: "))
    moeda = str(input("Informe a moeda que deseja converter (Dolar,Euro,Libra ou Peso): "))

    if(moeda == "dolar" or moeda == "Dolar"):
        valor = valor * 5.08
        print("Conversão em Dolar = ", valor)
    elif(moeda == "euro" or moeda == "Euro"):
        valor = valor * 5.45
        print("Conversão para Euro = ", valor)
    elif(moeda == "libra" or moeda == "Libra"):
        valor = valor * 6.37
        print ("Conversão em Libra =", valor)
    elif(moeda == "peso" or moeda == "Peso"):
        valor = valor * 0.059
        print ("Conversão em Peso = ", valor)


ex11()