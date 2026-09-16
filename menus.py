#função para escolher uma classe
def escolherClasse (classes):

    print("-------------")
    print("[0] - Mago\n"
        "[1] - Barbaro\n"
        "[2] - bardo")
    print("-------------")



    while True:
        escolha_texto = input("Escolha uma classe: ")
        if escolha_texto.isdigit():
            escolha = int(escolha_texto)
            if 0 <= escolha < len (classes):
                classe_escolhida = classes[escolha]
                print(f"você escolheu a classe {classe_escolhida}")
                return classe_escolhida
            else:
                print("opção inválida")
        else:
            print("você precisa digitar um número!")

#função pra escolher operações

def escolherOperacao (operacoes):
    print("seja bem-vindo a loja!")
    print("-------------")
    print("[0] - sair\n[1] - comprar\n[2] - vender\n[3] - consultar a bolsa\n")
    print("-------------")

    while True:
        escolha_texto = input("Escolha uma operação: ")
        if escolha_texto == "sair":
            break

        if escolha_texto.isdigit():
            escolha = int(escolha_texto)
            if 0 <= escolha < len(operacoes):
                operacao_escolhida = operacoes[escolha]
                print(f"Você escolheu {operacao_escolhida}")
                return operacao_escolhida
            else:
                print("operação inválida")
        else:
            print("você precisa digitar um número!")
    return escolha_texto

#Navegar pelo menu da zona de equipamento
def acao_equipamento(zonaEquipamento):
  print("seja bem-vindo à zona de equipamento!")
  print("-----------------")
  print("[1] - consultar\n[2] - equipar\n[3] = retirar equipamento\n[0] - sair")

  while True:
    escolha_texto = input("O que você quer fazer? ")
    if escolha_texto == "sair":
      break

    if escolha_texto.isdigit():
      escolha = int(escolha_texto)
      if 0<= escolha < len(zonaEquipamento):
        navegacao_escolhida = zonaEquipamento[escolha]
        print(f"você escolheu {navegacao_escolhida}")
        return navegacao_escolhida
      else:
        print("escolha inválida")
    else:
       print("Você precisa digitar um número!")
  return escolha_texto