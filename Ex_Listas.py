#Exercicio3 - Cálculo de estatísticas de acidentes de 
#trânsito em várias cidades. 
#Vamos utilizar duas listas: 
#Uma lista de strings para armazenar os nomes das cidades.
#Uma lista de numeros para armazenar o número de acidentes 
#em cada cidade. 

import os
os.system('cls')

# Lista de nomes de cidades 
nomes_cidades = ["Araraquara","São Carlos","Jau","Monte Alto","Ibaté"]

# Lista de números de acidentes correspondentes
numero_acidentes = [55, 65, 60, 65,55]

# Calcula o total de acidentes (sum())
total_acidentes = sum(numeros_acidentes)

# Calcula a média de acidentes por cidade (len())
media_acidentes = total_acidentes/len(numeros_acidentes)

# Encontra o maior número de acidentes (max())
max_acidentes = max(numeros_acidentes)

# Encontra o menor número de acidentes (min())
min_acidentes = min(numeros_acidentes)

# Encontra todas as cidades com o maior número de acidentes
cidade_mais_acidentes = []
for i in range(len(numeros_acidentes)):
    if numeros_acidentes[i] == max_acidentes:
        cidade_mais_acidentes.append(nomes_cidades[i])

# Encontra todas as cidades com o menor número de acidentes
cidade_menos_acidentes = []
for i in range(len(numeros_acidentes)):
    if numeros_acidentes[i] == min_acidentes:
        cidade_menos_acidentes.append(nomes_cidades[i])

# Exibe o total de acidentes
print(f"Total de acidentes = {total_acidentes}")
input()

# Exibe a média de acidentes por cidade com duas casas decimais
print(f"Média de acidentes = {media_acidentes:.2f}")
input()

# Exibe as cidades com mais acidentes e o número de acidentes
print(f"Cidades com mais acidentes ({max_acidentes})")
for cidades in cidade_mais_acidentes:
    print(cidades)
input()

# Exibe as cidades com menos acidentes e o número de acidentes
print(f"Cidade com menos acidentes ({min_acidentes})")
for cidades in cidade_menos_acidentes:
    print(cidades)

print("\n")