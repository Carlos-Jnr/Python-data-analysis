###################################
## Exemplo de trabalho com lista ##
###################################

lista = ['House','Wilson','Cuddy']
lista_2 = []

for nome in lista:
    print (nome)
    if ((nome == 'House') or (nome == 'Wilson')):
        lista_2.append(nome)



print (lista_2)

