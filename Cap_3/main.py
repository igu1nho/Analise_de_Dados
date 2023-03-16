# Exercicio 1
print("Exercício 1:")
# Criando uma tupla com o ranking entre os 5 melhores times de cs
times = ['G2', 'Heroic', 'Liquid', 'Faze', 'Navi']
# Ordem de colocação
print(times)

# a) Apenas os 3 primeiros colocados
print("Os 3 primeiros colocados são: " + times[0] + "," + times[1] + " e " + times[2])

# b) Os ultimos 2 colocados
print("Os 2 ultimos colocados são: " + times[3] + " e " + times[4])

# c) Uma lista com os times em ordem alfabetica
print("Times em ordem alfabetica: ")
print(sorted(times))

# d) Em qual posição da tabela está a Liquid
print("Posicao do Liquid na tabela: ")
print(times.index('Liquid'))
print("-----------------------------------------------------------------")
print()

# Exercicio 2
print("Exercício 2:")
# Criando dois conjuntos para uma loja Da Xiaomi e uma da Samsung
loja_Igor = {'Readmi 10', 'Readmi 11', 'Readmi 12', 'Readmi 13', 'Iphone 13'}
loja_Luiz = {'Samsung S10', 'Samsung S11', 'Samsung S12', 'Samsung S13', 'Iphone 13'}

# Identificando os modelos separados que cada uma vende
print("Aparelhos vendidos pela loja do Igor: ")
print(set(loja_Igor))
print("Aparelhos vendidos pela loja do Luiz: ")
print(set(loja_Luiz))

# Modelos disponiveis caso visite ambas as lojas
Todos_Modelos = loja_Igor | loja_Luiz
print("Total de modelos disponiveis para venda em ambas as lojas: ")
print(Todos_Modelos)

# Modelos disponiveis em ambas as lojas
interseccao = loja_Igor & loja_Luiz
print("Mesmo modelo disponivel para venda em ambas as lojas: ")
print(interseccao)
print("-----------------------------------------------------------------")
print()

# Exercicio 3
print("Exercício 3: ")
# Entrando com a quantidade de alunos que se deseja cadastrar
dados_alunos = {}

# Lendo os dados dos alunos
nome = input("Nome do aluno: ")
media = float(input("Media do aluno: "))

# Verificando a media do aluno
if media < 60:
    s = 'RP'
else:
    s = 'AP'

dados_alunos['nome'] = nome
dados_alunos['media'] = media
dados_alunos['situacao'] = s

# Mostrando os dados da biblioteca
print(dados_alunos)
print("-----------------------------------------------------------------")
