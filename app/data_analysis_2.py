import os
import sys
from utils.prints_custom import *
lista_caminho = ['s3:\\bucketA\pasta1\objeto9','s3:\\bucketA\pasta2\objeto8','s3:\\bucketB\pasta3\objeto7','s3:\\bucketB\pasta4\objeto6','s3:\\bucketC\pasta5\objeto7']

lista_buckets = []
lista_pastas = []
lista_objetos = []


for caminho in lista_caminho:
    caminho_lista = caminho.split('\\')
    lista_buckets.append(caminho_lista[1])
    lista_pastas.append(caminho_lista[2])
    lista_objetos.append(caminho_lista[3])

lista_buckets = list(set(lista_buckets))
lista_pastas = list(set(lista_pastas))
lista_objetos = list(set(lista_objetos))

lista_buckets.sort(reverse=True)
lista_pastas.sort()
lista_objetos.sort(reverse=True)

print_tamanho(lista_buckets,'Buckets')
print_lista(lista_buckets)

print_tamanho(lista_pastas,'Pastas')
print_lista(lista_pastas)

print_tamanho(lista_objetos,'Objetos')
print_lista(lista_objetos)