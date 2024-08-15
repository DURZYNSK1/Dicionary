#AUEMNTE OS PREÇOS DOS PRODUTO A SEGUIR EM 10%
#GERAR NOVOS PRODUTOS POR DEEP COPY
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}, 

]
#AUMENTRA EM 10% OS VALORES
for produto in produtos:
    produto['preco'] = (produto['preco'] * 1.10)
    print(f'O {produto['nome']} com adição de 10% seria de {produto['preco']:.2f}')


# ORDENAR OS PRODUTOS EM ORDEM DECRESCENTE PELO NOME
produtos.sort(key=lambda x: x['nome'], reverse=True)
print("Produtos ordenados decrescentemente pelo nome:", produtos)

# GERAR NOVOS PRODUTOS POR DEEP COPY
novo_produtos = copy.deepcopy(produtos)
print("Cópia profunda dos produtos:", novo_produtos)

# ORDENAR OS PRODUTOS EM ORDEM CRESCENTE PELO PREÇO
produtos.sort(key=lambda x: x['preco'], reverse=False)
print("Produtos ordenados crescentemente pelo preço:", produtos)