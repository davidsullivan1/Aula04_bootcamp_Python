listanumeros = [40,50,60,70,0,-40568,1,51]



def ordenacaoListaNumeros(numeros: list) -> list:
    listaordenada: list = numeros

    for i in range(len(listaordenada)):
        for j in range(i+1, len(listaordenada)):
            if listaordenada[i] > listaordenada[j]:
                listaordenada[i], listaordenada[j] = listaordenada[j], listaordenada[i]

    return listaordenada




listaOrdenada = ordenacaoListaNumeros(listanumeros)


print(listaOrdenada)
