from personagens import personagens, classes
from inimigos import inimigos
from itens import itens_loja
from loja import loja_comprar, loja_vender
from inventario import inventario
from combate import iniciar_combate
from equipamentos import equipando_itens, retirar_equipamento, consultar_equipamento


mochila = []



operacoes = ["sair", "comprar", "vender", "consultar"]

menuPrincipal = ["sair","loja de equipamentos", "zona de combate", "zona de equipamento"]

zonaEquipamento = ["sair", "consultar", "equipar", "retirar"]




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







#função para começar o combate



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

#função pra navegar entre os cenários

def navegacao(menuPrincipal):
  print("seja bem-vindo ao nosso mundo!")
  print("-----------------")
  print("[1] - loja de equipamentos\n[2] - zona de combate\n[3] = zona de equipamentos\n[0] - sair")

  while True:
    escolha_texto = input("Para onde você quer ir? ")
    if escolha_texto == "sair":
      break

    if escolha_texto.isdigit():
      escolha = int(escolha_texto)
      if 0<= escolha < len(menuPrincipal):
        navegacao_escolhida = menuPrincipal[escolha]
        print(f"você escolheu {navegacao_escolhida}")
        return navegacao_escolhida
      else:
        print("escolha inválida")
    else:
       print("Você precisa digitar um número!")
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

#consultar status
def mostrar_status(personagens, classe, saldo):
    print(f"classe: {classe}")
    print(f"saldo: {saldo}")
    print(f"HP: {personagens[classe]['hp']}")
    print(f"Dano: {personagens[classe]['dano']}")
    print(f"Defesa: {personagens[classe]['defesa']}")



#invocação de função para escolher classe
print("Vamos começar a explorar o mundo! Por onde você quer começar: ")
print("Escolha a classe do seu persongame")

classe = escolherClasse(classes)

print("Para onde você quer ir agora?")


#funções para começar o jogo
saldo = personagens[classe]["saldo"]
capacidade_maxima = personagens[classe]["capacidade"]

#invocando função para comprar item

while True:
  mostrar_status(personagens, classe, saldo)
  navigation = navegacao(menuPrincipal)
  if navigation == "loja de equipamentos":    
    while True:
      mostrar_status(personagens, classe, saldo)
      transacao = escolherOperacao(operacoes)
      if transacao == "comprar":
        saldo = loja_comprar(saldo, mochila, itens_loja, capacidade_maxima)
        continue
      if transacao == "vender":
        saldo = loja_vender(saldo, mochila, itens_loja)
        continue
      if transacao == "consultar":
        consulta = inventario(mochila)
        continue

      if transacao == "sair":
        break
      print("obrigado pela visita")
    continue

  if navigation == "zona de combate":
     mostrar_status(personagens, classe, saldo)
     saldo = iniciar_combate(personagens, inimigos, classe, saldo)

  if navigation == "zona de equipamento":
    
    while True:
      mostrar_status(personagens, classe, saldo)
      navegacao_escolhida = acao_equipamento(zonaEquipamento)
      if navegacao_escolhida == "equipar":
        equipando_itens(mochila, personagens, classe, itens_loja)

      if navegacao_escolhida == "retirar":
        retirar_equipamento(mochila, personagens, classe, itens_loja)
        

      if navegacao_escolhida == "consultar":
        consultar_equipamento(personagens, classe)
        

      if navegacao_escolhida == "sair":
        break
    continue 

  if navigation == "sair":
    break




