# *****Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números. OK
# *****Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais. OK
# *****Escreva um programa que receba dois nomes de usuário e os combine de maneira criativa para formar um novo nome. OK
# *****Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números. OK
# *****Crie um programa que peça ao usuário seu nome e sobrenome usando input e, em seguida, combine-os para formar uma saudação personalizada. OK
# *****Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo. OK
# *****Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
# *****Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não. OK
# *****Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%. OK
# *****Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa. OK
# *****Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados. OK
# *****Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais). OK
# *****Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente). OK
# *****Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção. OK
#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.
# *****Neste exercício, você deverá escrever um programa em Python que verifique se um número fornecido pelo usuário é par ou ímpar. Imprima uma mensagem indicando se o número é par ou ímpar. OK

import random

# EXERCICIO 1
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(f'A soma entre o número {num1} e {num2} é', num1 + num2)
print(f'A subtração entre o número {num1} e {num2} é', num1 - num2)
print(f'A multiplicação entre o número {num1} e {num2} é', num1 * num2)
print(f'A divisão entre o número {num1} e {num2} é', num1 / num2)


# EXERCICIO 2
def minutos_para_horas(minutos):
  horas = minutos // 60
  minutos_restantes = minutos % 60
  return horas, minutos_restantes

def horas_e_minutos_para_minutos(horas, minutos):
  return horas * 60 + minutos

minutos = int(input("Digite os minutos para serem convertidos em horas: "))
horas, minutos_restantes = minutos_para_horas(minutos)

print(f"{minutos} minutos é igual a {horas} e {minutos_restantes} minutos.")

horas = int(input("Digite as horas para serem convertidas em minutos: "))
minutos = int(input("Digite os minutos: "))
minutos_totais = horas_e_minutos_para_minutos(horas, minutos)

print(f"{horas} horas é igual a {minutos_totais} minutos.")

# EXERCICIO 3
def combinar_nomes(nome1, nome2):
  nome_combinado = nome1[:len(nome1)//2] + nome2[len(nome2)//2:]
  return nome_combinado

usuario1 = input("Digite o primeiro nome de usuário: ")
usuario2 = input("Digite o segundo nome de usuário: ")

novo_nome = combinar_nomes(usuario1, usuario2)
print(f"O novo nome combinado entre os nomes enviados é: {novo_nome}. Lindo, não?")

# EXERCICIO 4
def realizar_operacao(numeroA, numeroB, operacao):
  if operacao == 'soma':
    return numeroA + numeroB
  elif operacao == 'subtração' or 'subtracao' or 'subtraçao':
    return numeroA - numeroB
  elif operacao == 'multiplicação' or 'multiplicacao' or 'multiplicaçao':
    return numeroA * numeroB
  elif operacao == 'divisão' or 'divisao':
    if numeroB != 0:
      return numeroA / numeroB
    else:
      return "Divisão por zero não existe!"
  else:
    return "Tente novamente!"
  
numeroA = float(input("Digite um número: "))
numeroB = float(input("Digite outro número: "))
operacao = input("Escolha a operação que deseja realizar, digitando a opção desejada: soma, subtração, multiplicação ou divisão: ")
resultado = realizar_operacao(numeroA, numeroB, operacao)
print(f"A {operacao} de {numeroA} e {numeroB} é igual a {resultado}")

# EXERCICIO 5
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(f"Olá, {nome} {sobrenome}! Seja bem vindo(a)!")

# EXERCICIO 6
import random
num_secreto = random.randint(1, 10)
tentativas = 0

print("JOGO DE ADIVINHAÇÃO! Adivinhe o número secreto entre 1 e 10.")

while True:
  palpite_usuario = int(input("Digite seu palpite: "))
  tentativas += 1

  if palpite_usuario < num_secreto:
    print("Palpite muito baixo... tente novamente!")
  elif palpite_usuario > num_secreto:
    print("Palpite muito alto... tente novamente!")
  elif palpite_usuario == num_secreto:
    if tentativas < 2:
      print(f"Você acertouuuuu! Adivinhou o número secreto {num_secreto} em {tentativas} tentativa!")
    else:
      print(f"Você acertouuuuu! Adivinhou o número secreto {num_secreto} em {tentativas} tentativas!")
      break
  else:
    print("Algo deu errado... tente novamente!")

# EXERCICIO 7
def calcula_IMC(peso, altura):
  imc = peso / (altura **2)
  return imc

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc_usuario = calcula_IMC(peso, altura)
print(f"Seu IMC é {imc_usuario}")

if imc_usuario < 18.5:
  print("Você está abaixo do peso!")
elif 18.5 <= imc_usuario < 24.9:
  print("Você está com o peso normal.")
elif 25 <= imc_usuario < 29.9:
  print("Você está acima do peso!")
else:
  print("Você está com obesidade.")

# EXERCICIO 8
def verifica_maioridade(idade):
  if idade >= 18:
    return "Você é maior de idade!"
  else:
    return "Você é menor de idade!"

idade = int(input("Digite sua idade: "))
print(verifica_maioridade(idade))

# EXERCICIO 9
def calcular_desconto(valor_compra):
  if valor_compra > 500:
      desconto = 0.25
  elif valor_compra > 200:
      desconto = 0.15
  elif valor_compra > 100:
      desconto = 0.10
  else:
      desconto = 0.0

  valor_desconto = valor_compra * desconto
  valor_final = valor_compra - valor_desconto

  return valor_desconto, valor_final

valor_compra = float(input("Digite o valor da compra: R$ "))
desconto, total = calcular_desconto(valor_compra)

print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor total a pagar: R$ {total:.2f}")

# EXERCICIO 10
dias = [
  "Era um dia ensolarado quando",
  "Em uma noite de vendaval,",
  "No meio de uma tempestade de fumaça",
  "Em um mundo não tão distante,"
]

personagens = [
    "Chico Buarque", 
    "Caetano Veloso", 
    "Gilberto Gil", 
    "Elis Regina", 
    "Gal Costa", 
    "Jorge Ben Jor", 
    "Maria Bethânia", 
    "Cazuza"
]

acoes = [
    "desvendou um mistério antigo", 
    "fez uma jornada épica", 
    "conheceu criaturas mágicas", 
    "participou de uma batalha musical", 
    "explorou um reino secreto"
]

locais = [
    "em uma caverna encantada.", 
    "numa casinha no alto do morro.", 
    "em uma ilha misteriosa.", 
    "dentro de uma tempestade mágica.", 
    "no palácio de cristal.",
    "na sonífera ilha."
]

def criar_historia():
  dia = random.choice(dias)
  personagem = random.choice(personagens)
  acao = random.choice(acoes)
  local = random.choice(locais)

  historia = print(f"{dia} {personagem} {acao} {local}")
  return historia

print("Era uma vez...")
criar_historia()

# EXERCICIO 11
def lancar_dados(num_dados):
  resultados = []
  for _ in range(num_dados):
    resultado = random.randint(1, 6)
    resultados.append(resultado)
  return resultados

quantidade_dados = int(input("Digite quantos dados deseja jogar: "))
resultados = lancar_dados(quantidade_dados)
print("Resultados dos lançamentos:", resultados)

# EXERCICIO 12
print("Digite as palavras para verificar se são curtas ou longas. Para finalizar, digite 'FIM'.")

while True:
  palavra = input("Digite uma palavra: ")
  if palavra.upper() == 'FIM':
    print("Programa finalizado.")
    break
  if len(palavra) <= 5:
    print(f"Palavra {palavra} é curta")
  else:
    print(f"Palavra {palavra} é longa")

# EXERCICIO 13
def eh_palindromo(palavra):
  palavra = palavra.replace(" ", "").lower()
  return palavra == palavra[::-1]

entrada = input("Digite uma palavra: ")
if eh_palindromo(entrada):
  print("É um palíndromo!")
else:
  print("Não é um palíndromo.")


# EXERCICIO 14
votos = [0, 0, 0]

opcoes = [
  "Marisa Monte",
  "Cássia Eller",
  "Ana Carolina"
]

print("Vote em uma das opções abaixo para melhor voz feminina (MPB):")
for i, opcao in enumerate(opcoes, start=1):
  print(f"{i}: {opcao}")

while True:
  voto = input("Digite o número da sua opção (1, 2 ou 3) ou escreva 'sair' para encerrar: ")

  if voto in ['1', '2', '3']:
    votos[int(voto) -1] += 1
  elif voto.lower() == 'sair':
    break
  else:
    print("Opção inválida! Tente novamente.")

print("Resultados da votação:")
for i in range(len(votos)):
  print(f"{opcoes[i]}: {votos[i]} votos")

# EXERCICIO 15
def historia():
  print("Você é um(a) cantor(a) famoso(a) em uma turnê pelo Brasil.")
  print("Após um show incrível, você tem duas opções:")
  print("1: Ir para uma festa em um bar da Lapa.")
  print("2: Ir para Porto Alegre tomar um chimarrão no Guaíba.")
  
  escolha1 = input("Qual você escolhe? (1 ou 2): ")

  if escolha1 == '1':
    print("Lá você encontra grandes músicos e juntos decidem fazer um show ao vivo para o pessoal da festa.")
    print("Você pode:")
    print("1: Cantar uma música clássica da MPB.")
    print("2: Tentar compor uma nova canção na hora.")
    
    escolha2 = input("O que você faz? (1 ou 2): ")

    if escolha2 == '1':
      print("Você canta 'Garota de Ipanema' e todos ficam emocionados!")
    elif escolha2 == '2':
      print("Você cria uma canção incrível que fala sobre amor e natureza, e todos aplaudem!")
    else:
      print("Escolha inválida! A aventura termina aqui.")
  
  elif escolha1 == '2':
    print("Em Porto Alegre, você encontra um amigo compositor que te convida para uma roda de canastra.")
    print("Você pode:")
    print("1: Falar sobre suas inspirações na música.")
    print("2: Pedir conselhos sobre como lidar com a fama.")
    
    escolha2 = input("O que você faz? (1 ou 2): ")

    if escolha2 == '1':
      print("Você compartilha suas histórias e inspirações, e ele sugere uma colaboração.")
    elif escolha2 == '2':
      print("Você recebe ótimos conselhos e se sente mais preparado para a vida artística.")
    else:
      print("Escolha inválida! A aventura termina aqui.")

  else:
    print("Escolha inválida! A aventura termina aqui.")

historia()

# EXERCICIO 16
def verifica_par_ou_impar(num):
  if (num % 2) != 0:
    print(f"O número {num} é ímpar!")
  else:
    print(f"O número {num} é par")

num = int(input("Digite um número: "))
verifica_par_ou_impar(num)