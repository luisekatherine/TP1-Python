#EX1
def quadrados(nums):
  return [num ** 2 for num in nums]

entrada = input("Digite os números separados por espaço: ")

numeros = list(map(int, entrada.split()))

resultado = quadrados(numeros)

print("Os quadrados dos números são:", resultado)

#EX2
def processar_numeros(nums):
  return [0 if num < 10 else num for num in nums]

entrada = input("Digite os números separados por espaço: ")

numeros = list(map(int, entrada.split()))

resultado = processar_numeros(numeros)

print("Resultado após o processamento:", resultado)

#EX3
def contar_palavras(historia):
  frases = historia.split('.')
  
  quantidade_palavras = [len(frase.split()) for frase in frases if frase.strip()]
  
  return quantidade_palavras

historia = input("Digite uma história com múltiplas frases: ")

resultado = contar_palavras(historia)

print("O número de palavras em cada frase é:", resultado)

#EX4
def contar_vogais(frase):
  #incluí com os acentos utilizados no Brasil para passar em todos casos de teste
  vogais = "aeiouáéíóúãâêôàAEIOUÁÉÍÓÚÃÂÊÔÀ"
  return sum(1 for letra in frase if letra in vogais)

frases = [
  "Preciso voltar a treinar Inglês.",
  "Quero ir no cinema olhar o filme da Fernanda Torres.",
  "Hoje tomei banho de chuva com meu cão.",
  "QUERO SER RICAAAAAAaa."
]

quantidade_vogais = [contar_vogais(frase) for frase in frases]

print("Número de vogais em cada frase:", quantidade_vogais)


###########################################################################3

#EX1:
idades_geral = {
    "Gonzaguinha": 17,
    "Maria Gadu": 22,
    "Armandinho": 16,
    "Ana Carolina": 30,
    "James Lima": 18,
    "Kiko": 15
}

maiores_de_idade = {nome: idade for nome, idade in idades_geral.items() if idade >= 18}

print("As pessoas maiores de idade são:", maiores_de_idade)

#EX2
def remover_palavras_indesejadas(texto, palavras_indesejadas):
  palavras = texto.split()
  
  palavras_filtradas = [palavra for palavra in palavras if palavra not in palavras_indesejadas]
  
  nova_string = ' '.join(palavras_filtradas)
  
  return nova_string

texto = "Meu gosto musical é uma salada de fruta"
palavras_indesejadas = ["gosto", "de", "fruta"]

resultado = remover_palavras_indesejadas(texto, palavras_indesejadas)
print("Texto atualizado:", resultado)

#EX3
def alternar_maiusculas_minusculas(texto):
  resultado = ""
  
  for i, letra in enumerate(texto):

    if i % 2 == 0:
      resultado += letra.upper()
    else:
      resultado += letra.lower()
  
  return resultado

entrada = "desenvolvendo habilidades"
saida = alternar_maiusculas_minusculas(entrada)
print("Resultado:", saida)

#EX4
def elementos_unicos(lista_de_listas):
  elementos_unicos = []
  
  for sublista in lista_de_listas:
    for elemento in sublista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
  
  return sorted(elementos_unicos)

lista = [[2, 4, 6], [4, 5, 1, 6], [2, 2, 6]]
resultado = elementos_unicos(lista)
print("Resultado:", resultado)

#EX5
def intercalar_listas(lista1, lista2):

  resultado = []
  
  comprimento_minimo = min(len(lista1), len(lista2))
  
  for i in range(comprimento_minimo):
    resultado.append(lista1[i])
    resultado.append(lista2[i])
  
  resultado.extend(lista1[comprimento_minimo:])
  resultado.extend(lista2[comprimento_minimo:])
  
  return ' '.join(resultado)

lista1 = ["Caetano Veloso", "Gilberto Gil", "Gal Costa", "Elis Regina"]
lista2 = ["Chico Buarque", "Marisa Monte", "Tom Jobim"]

resultado = intercalar_listas(lista1, lista2)
print(resultado)


#EX6:
def separar_palavras_por_comprimento(palavras, n):
  menor_ou_igual_n = [palavra for palavra in palavras if len(palavra) <= n]
  
  maior_que_n = [palavra for palavra in palavras if len(palavra) > n]
  
  return [menor_ou_igual_n, maior_que_n]

palavras = ["Skank", "Fresno", "Ana Carolina", "Gonzaga", "Osvaldo Montenegro", "Anavitoria"]
n = 6

resultado = separar_palavras_por_comprimento(palavras, n)

print("Palavras com comprimento menor ou igual a", n, ":", resultado[0])
print("Palavras com comprimento maior que", n, ":", resultado[1])

#EX7
def inserir_palavra(lista, nova_palavra):
  if len(lista) < 3:
    lista.append(nova_palavra)
  else:
    while True:
        try:
          posicao = int(input(f"Digite a posição, de 0 a {len(lista)}: "))
          if 0 <= posicao <= len(lista):
            break
          else:
            print(f"A posição deve estar entre 0 e {len(lista)}.")
        except ValueError:
          print("Por favor, insira um número válido.")
      
    lista.insert(posicao, nova_palavra)
  
  return lista

lista = ["Gal", "Chico", "Ana"]
nova_palavra = "Caetano"

lista_atualizada = inserir_palavra(lista, nova_palavra)
print("Lista atualizada:", lista_atualizada)

#EX8
def combinar_listas(lista1, lista2):

  lista_combinada = lista1.copy()
  
  lista_combinada.extend(lista2)
  
  return lista_combinada

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista_resultado = combinar_listas(lista1, lista2)
print("Lista combinada:", lista_resultado)

#EX9
def remover_duplicatas(lista):
  lista_sem_duplicatas = []
  
  for palavra in lista:
    if palavra not in lista_sem_duplicatas:
      lista_sem_duplicatas.append(palavra)
  
  return lista_sem_duplicatas

lista = ["kiwi", "pessego", "kiwi", "laranja", "banana", "abacaxi"]

lista_sem_duplicatas = remover_duplicatas(lista)
print("Lista sem duplicatas:", lista_sem_duplicatas)

#EX10
def gerenciar_compras(lista_compras):
  if lista_compras:
    item_removido = lista_compras.pop()
    print(f"O item '{item_removido}' foi removido da lista de compras.")
  else:
    print("Não há mais itens para remover. A lista está vazia.")
  
  print("Lista de compras atualizada:", lista_compras)

compras = ["arroz", "feijão", "macarrão", "leite"]

gerenciar_compras(compras)
gerenciar_compras(compras)
gerenciar_compras(compras)
gerenciar_compras(compras)
# Simulei a remoção para o caso da lista estar vazia
gerenciar_compras(compras)