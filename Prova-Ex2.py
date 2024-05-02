vlr = float(input("Digite o valor da operação: "))
op = input("Digite a operação (Soma, Subtração, Divisão e Multiplicação): ")
vlr2 = float(input("Digite o valor 2 da operaçã: "))

match op.lower():

    case "soma":
        valor = vlr + vlr2
        print(f"Resultado: {valor}")

    case "subtração":
        valor = vlr - vlr2
        print(f"Resultado: {valor}")

    case "divisão":
        valor = vlr / vlr2
        print(f"Resultado: {valor}")
        
    case "multiplicação":
        valor = vlr * vlr2
        print(f"Resultado: {valor}")


    


