vlr = float(input("Digite o valor do produto: "))
ds = int(input("Digite o departamento do produto: "))
cr = input("Digite a cor da etiqueta do produto: ")

dp = [
    [1, ["azul", "branca", "verde", "preta",], [0.6, 0.7, 0.8, 0.9]],
    [2, ["azul", "branca", "verde", "preta",], [0.63, 0.74, 0.82, 0.91]],
    [3, ["azul", "branca", "verde", "preta",], [0.56, 0.67, 0.78, 1.09]]
]

def get_desconto(departamento, cor):
    for item in dp:
        if item[0] == departamento and cor in item[1]:
            indice_cor = item[1].index(cor)
            return item[2][indice_cor]
        