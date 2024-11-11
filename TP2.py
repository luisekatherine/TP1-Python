'''
Crie um dicionário com as idades de várias pessoas e retorne um novo dicionário que contenha apenas as pessoas maiores de idade (Ex: idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16} deve retornar {'Alice': 22, 'Carol': 19}).

Crie duas tuplas e verifique se elas possuem os mesmos elementos, independente da ordem (Ex: tupla1 = (1,3,5) e tupla2 = (5, 1, 3) possuem SIM os mesmos elementos).

Crie uma lista que possua números repetidos e conte a frequência de cada elemento nessa utilizando um dicionário (Ex: lista = [4, 1, 5, 2, 3, 2, 4, 4] deve retornar dicionario = {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}).

Crie dois dicionários (com 2 ou mais elementos) e verifique se um é subconjunto de outro.

Crie um dicionário que mapeia alunos e suas notas e retorne um novo dicionário que classifique os alunos em "Aprovado" (nota >= 7) e "Reprovado" caso contrário (Ex: notas = {'Ana': 8.5, 'Pedro': 6.0, 'Maria': 7.5, 'José': 5.5} deve retornar {'Aprovado': ['Ana', 'Maria'], 'Reprovado': ['Pedro', 'José']}).

Crie uma lista (maior que 5 elementos) e encontre os dois números cuja soma seja o mais próximo possível de zero.

Crie um programa que permita ao usuário registrar as notas de uma turma de estudantes. O usuário deve inserir os nomes dos alunos e suas respectivas notas. O programa deve continuar solicitando entradas até que o usuário digite "fim". Após o término, o programa deve exibir os nomes dos alunos junto com suas notas.

Número Mágico: Crie um código para adivinhar um número aleatório entre 1 e 20 com um limite de 4 tentativas (ou seja, o programa recebe essas tentativas do usuário e verifica se o número que o usuário escreveu é o número mágico). OBS: Para cada número digitado, informe se ele está abaixo ou acima do número mágico.

Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo. OBS: Non-case sensitive e sem contar os espaços (Ex: "A mala nada na lama" é um palíndromo).

Crie uma lista de dicionários (de 4 ou mais elementos), em que cada elemento possui o nome e a nota dos alunos e ordene a lista de maneira decrescente por nota. OBS: Faça o exercício utilizando apenas estruturas básicas, sem chamar funções de sort ou algo do tipo.

Crie uma lista (de 4 ou mais elementos) e um programa que permita ao usuário acessar os elementos desta lista. O usuário deve inserir um índice (número inteiro) para obter o elemento correspondente na lista. Trate casos em que o índice inserido está fora do intervalo da lista ou se o usuário inserir algo que não seja um número (Dica: ‘try’, ‘except’). Se ocorrer um erro, informe ao usuário qual o erro e permita que ele tente novamente.

Joel possui uma barraca na feira e quer dar um presente a um cliente. Crie um programa que receba do usuário uma lista de frutas disponíveis na barraca e as quantidades correspondentes de cada fruta. O programa deve escolher aleatoriamente uma fruta para presentear o cliente. Se o número de quantidades fornecido for maior do que o número de frutas, o programa deve contabilizar apenas até o último índice da lista de frutas. Caso o número de quantidades seja menor do que o número de frutas, o programa deve solicitar ao usuário que reescreva a lista de quantidades (Ex: input do usuário: ‘maçã, banana, laranja’ | ‘10, 5, 8’).

Escreva uma função que receba um texto do usuário e printe esse texto.

Defina uma função chamada ‘dividir’ que recebe dois números e retorna dois outputs: o resultado inteiro da divisão e o resto. Escreva uma docstring para documentar o que a função faz, quais são seus parâmetros, e o que ela retorna.

Defina uma função que receba um nome e uma idade como argumentos obrigatórios e uma cidade como argumento opcional (valor padrão "Desconhecida"). A função deve imprimir uma mensagem personalizada com essas informações. Ex: "Maria tem 30 anos e mora em São Paulo".

Defina uma função chamada calcular_total que receba dois parâmetros: preço e quantidade, onde a quantidade tem o valor padrão de 1. A função deve calcular e retornar o total, multiplicando o preço pela quantidade.
'''
import random

#EXERCICIO 1
idades = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}
maiores_de_idade = {pessoa: idade for pessoa, idade in idades.items() if idade >= 18}
print(maiores_de_idade)

#EXERCICIO 2
tupla1 = ('A', 'B', 'C')
tupla2 = ('D', 'A', 'F')

lista1 = sorted(tupla1)
lista2 = sorted(tupla2)

if lista1 == lista2:
  print("As tuplas possuem os mesmos elementos.")
else:
  print("As tuplas não possuem os mesmos elementos.")


#EXERCICIO 3
lista = [4, 1, 5, 2, 3, 2, 4, 4]
frequencia = {}

for numero in lista:
  if numero in frequencia:
    frequencia[numero] += 1
  else:
    frequencia[numero] = 1

print(frequencia)

#EXERCICIO 4
dicionario1 = {'Bethania': 22, 'Caetano': 17}
dicionario2 = {'Bethania': 22, 'Caetano': 17, 'Zeca': 19, 'Milton': 16}

if all(item in dicionario2.items() for item in dicionario1.items()):
  print("dicionario1 é subconjunto de dicionario2.")
else:
  print("dicionario1 não é subconjunto de dicionario2.")

#EXERCICIO 5
notas = {'Bethania': 8.5, 'Caetano': 6.0, 'Zeca': 7.5, 'Gal': 5.5}
classificacao = {'Aprovado': [], 'Reprovado': []}

for aluno, nota in notas.items():
  if nota >= 7:
    classificacao['Aprovado'].append(aluno)
  else:
    classificacao['Reprovado'].append(aluno)

print(classificacao)

#EXERCICIO 6



#EXERCICIO 7
notas_alunos = {}

while True:
  nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
  if nome.lower() == "fim":
    break
    
  try:
    nota = float(input(f"Digite a nota de {nome}: "))
    notas_alunos[nome] = nota
  except ValueError:
    print("Por favor, insira uma nota válida.")

print("\nNotas dos alunos:")
for nome, nota in notas_alunos.items():
  print(f"{nome}: {nota}")


#EXERCICIO 8
numero_magico = random.randint(1, 20)
tentativas = 4

print("Bem-vindo(a) ao jogo do Número Mágico! \nTente adivinhar o número entre 1 e 20.")
print(f"Você tem {tentativas} tentativas.")

for tentativa in range(1, tentativas + 1):
  palpite = int(input(f"Tentativa {tentativa} de {tentativas}: Digite seu palpite: "))

  if palpite == numero_magico:
    print("Parabéns! Você adivinhou o número mágico!")
    break
  elif palpite < numero_magico:
    print("O número mágico é maior. Tente novamente.")
  else:
    print("O número mágico é menor. Tente novamente.")

if palpite != numero_magico:
  print(f"Errouuu! Você usou todas as {tentativas} tentativas. O número mágico era {numero_magico}.")


#EXERCICIO 9
def verificar_palindromo(frase):
  frase_limpa = frase.replace(" ", "").lower()
  
  if frase_limpa == frase_limpa[::-1]:
    return True
  else:
    return False

entrada = input("Digite uma palavra ou frase para verificarmos se é um palíndromo: ")

if verificar_palindromo(entrada):
  print("É um palíndromo!")
else:
  print("Não é um palíndromo.")


#EXERCICIO 10


#EXERCICIO 11
lista = ["Ana Carolina", "Maria Bethania", "Caetano Veloso", "Milton Nascimento"]

def acessar_elemento():
    while True:
        try:
            indice = int(input("Digite o índice -de 0 a 3- para acessar um(a) cantor(a) da lista: "))
            print(f"Cantor no índice {indice}: {lista[indice]}")
            break 

        except ValueError:
            print("Erro: Você deve digitar um número inteiro.")
        
        except IndexError:
            print("Erro: Índice fora do intervalo da lista. Tente novamente com um número entre 0 e 3.")

acessar_elemento()


#EXERCICIO 12
def solicitar_frutas_e_quantidades():
    while True:
        try:
            frutas_input = input("Digite as frutas disponíveis (separadas por vírgula): ")
            frutas = [fruta.strip() for fruta in frutas_input.split(',')] 

            quantidades_input = input("Digite as quantidades correspondentes às frutas (separadas por vírgula): ")
            quantidades = [int(quant.strip()) for quant in quantidades_input.split(',')]

            if len(quantidades) > len(frutas):
              quantidades = quantidades[:len(frutas)]  
            elif len(quantidades) < len(frutas):
              print("Erro: O número de quantidades deve ser igual ao número de frutas ou maior. Tente novamente.")
              continue

            return frutas, quantidades
        except ValueError:
          print("Erro: As quantidades devem ser números inteiros. Tente novamente.")

def escolher_fruta(frutas, quantidades):
  frutas_repetidas = []
  for fruta, quantidade in zip(frutas, quantidades):
    frutas_repetidas.extend([fruta] * quantidade)
    fruta_escolhida = random.choice(frutas_repetidas)
    return fruta_escolhida

frutas, quantidades = solicitar_frutas_e_quantidades()

fruta_escolhida = escolher_fruta(frutas, quantidades)

print(f"A fruta escolhida para presentear o cliente é: {fruta_escolhida}")


#EXERCICIO 13
def imprimir_texto():
  texto = input("Digite um texto: ")
  print(f"O texto digitado foi '{texto}'")

imprimir_texto()


#EXERCICIO 14
def dividir(num1, num2):
  res_inteiro = num1 // num2
  res_resto_divisao = num1 %num2
  print(f"O resultado da divisão inteira de {num1} com {num2} é {res_inteiro} e o resultado do resto da divisão é {res_resto_divisao}")
  return res_inteiro, res_resto_divisao

dividir(5, 3)


#EXERCICIO 15
def apresentar_pessoa(nome, idade, cidade="Desconhecida"):
  """
  Imprime mensagem personalizada com o nome, idade e cidade de uma pessoa.

  Parâmetros:
  nome (string): O nome da pessoa.
  idade (inteiro): A idade da pessoa.
  cidade (string): A cidade onde a pessoa mora (opcional, valor padrão é "Desconhecida").

  """
  print(f"{nome} tem {idade} anos e mora em {cidade}.")

apresentar_pessoa("Maria", 30, "São Paulo")
apresentar_pessoa("Luise", 28)


#EXERCICIO 16
def calcular_total(preco, quantidade=1):
  """
  Calcula o total multiplicando o preço pela quantidade.

  Parâmetros:
  preco (float): O preço de um item.
  quantidade (inteiro): A quantidade de itens (valor padrão é 1).

  Retorna:
  float: O total, que é o preço multiplicado pela quantidade.
  """
  total = preco * quantidade
  return total

print(calcular_total(10.50, 3))
print(calcular_total(5.00))