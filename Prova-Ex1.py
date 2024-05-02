vlr = float(input("Digite o valor do produto: "))
ds = int(input("Digite o departamento do produto: "))
cr = input("Digite a cor da etiqueta do produto: ")

dp = [
    [1, ["azul", "branca", "verde", "preta",], [0.06, 0.07, 0.08, 0.09]],
    [2, ["azul", "branca", "verde", "preta",], [0.063, 0.074, 0.082, 0.091]],
    [3, ["azul", "branca", "verde", "preta",], [0.056, 0.067, 0.078, 0.109]]
]

def get_desconto(departamento, cor):
    for item in dp:
        if item[0] == departamento and cor in item[1]:
            indice_cor = item[1].index(cor)
            return item[2][indice_cor]
    return None 

desconto = get_desconto(ds,cr)

if desconto is not None:
    valord = vlr * desconto
    valorf = vlr - valord
    print(f"Desconto aplicado: {desconto * 100:.2f}%")
    print(f"Preço com desconto: R$ {valorf:.2f}")        
else:
    print("Você digitou algum parâmetro errado!")