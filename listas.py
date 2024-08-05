# produto1: str = "Sapato"
# produto2: str = "Camisa"
# produto3: str = "Calça"
# produto4: str = "Bota"

# produtos = []
# produtos.append(produto1)
# produtos.append(produto2)
# produtos.append(produto3)
# produtos.append(produto4)

# print(produtos)

# #Exclui o último elemento adicionado na lista
# produtos.pop()
# #Exclui indicando o item que quer remover
# produtos.remove(produto1)
# print(produtos)



import json

from typing import Dict


produto01: Dict[str, any] = {
    "nome":"Sapato",
    "Quantidade":10,
    "Valor": 20.50
}


produto02: Dict[str, any] = {
    "nome":"Camisa",
    "Quantidade":5,
    "Valor": 10.50
}


carrinho: list = []


carrinho.append(produto01)
carrinho.append(produto02)
carrinho_json = json.dumps(carrinho)



for produto in carrinho:
    print(produto)
