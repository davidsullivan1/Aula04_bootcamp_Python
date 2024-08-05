produto1: str = "Sapato"
produto2: str = "Camisa"
produto3: str = "Calça"
produto4: str = "Bota"

produtos = []
produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)
produtos.append(produto4)

print(produtos)

#Exclui o último elemento adicionado na lista
produtos.pop()
#Exclui indicando o item que quer remover
produtos.remove(produto1)
print(produtos)