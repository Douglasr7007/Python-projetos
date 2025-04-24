#Criando uma lista vazia. Fazendo loop for e inserindo os valores na lista com o metodo input 
# e inserindo na lista atraves da função .append

#Organizando a lista em ordem crescente, usando a função sorted

#Len verifica a quantidade de elementos dentro de uma lista 

lista_vazia = []

for n in range(5):
    lista_vazia.append(input("Digite um número inteiro:")) 
print(lista_vazia)

print(sorted(lista_vazia))

print(len(lista_vazia))


#Usando o fatiamento de str [] para acessar os elementos dentro da lista 

#O índice inicial é incluído, o final é excluído
#Se não colocar início, ele assume o começo da string
#Se não colocar fim, ele vai até o final


lista_vazia = [1,2,3,4,5,6,7,8,9,12,26,53,22]
print(lista_vazia[7:10])


#A função CLEAR limpa a lista 
print(lista_vazia)
lista_vazia.clear()
print(lista_vazia)


# Função INSERT serve para fazer a inserção de elementos em qualquer posição especificada

lista_test = [5,6,7,8,9,2,3]
print(sorted(lista_test))
lista_test.insert(4, 0)
print(lista_test)


# Função EXTEND é como se fosse uma concatenação das listas 
lista_1 = [1,2,3,4,5]
lista_2 = [6,7,8,9]
lista_1.extend(lista_2)
print(lista_1)


# Função REMOVE faz a remoção de um determinado elemento 
lista_1.remove(3)
print(lista_1)


# Função POP faz a remoção de um determinado elemento através da índice do mesmo
lista_3 = [5,6,7,8,9]
lista_3.pop(3)
print(lista_3) 


#Função COPY faz uma copia mantendo a integritade da lista original 

lista_original = lista_3.copy()
lista_original.insert(5, 0)
print(lista_original)


# Função INDEX procura qual é a posição de um elemento dentro da lista
print(lista_original.index(6))





