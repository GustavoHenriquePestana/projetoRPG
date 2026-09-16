import random
from personagens import personagens, classes
from inimigos import inimigos
from itens import itens_loja
from loja import loja_comprar, loja_vender, catalogo_loja
from inventario import inventario


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
def iniciar_combate(personagens, inimigos, classe, saldo):

#----------------------------------------------------------------
# Sistema de combate
#----------------------------------------------------------------

  print("Você está em uma zona de combate")

  hp_jogador = personagens[classe]["hp"]
  dano_jogador = personagens[classe]["dano"]
  defesa_jogador = personagens[classe]["defesa"]

  print("------------------")
  print("status do jogador")
  print(f"HP: {hp_jogador}")
  print(f"Dano: {dano_jogador}")
  print(f"Defesa: {defesa_jogador}")

  monstros_sorteados = list(inimigos.keys())
  monstro_adversario = random.choice(monstros_sorteados)

  print(f"Você foi atacado por: {monstro_adversario}")

  hp_inimigo = inimigos[monstro_adversario]["hp"]
  dano_inimigo = inimigos[monstro_adversario]["dano"]
  defesa_inimigo = inimigos[monstro_adversario]["defesa"]

  print("------------------")
  print("status do monstro")
  print(f"HP: {hp_inimigo}")
  print(f"Dano: {dano_inimigo}")
  print(f"Defesa: {defesa_inimigo}")

  defesa_partida_jogador = defesa_jogador
  dano_partida_jogador = dano_jogador
  hp_partida_jogador = hp_jogador

  defesa_partida_inimigo = defesa_inimigo
  dano_partida_inimigo = dano_inimigo
  hp_partida_inimigo = hp_inimigo


  while hp_partida_inimigo > 0 and hp_partida_jogador > 0:

    defesa_turno_jogador = defesa_jogador

    #sorteios 
    sorteio_dano = 0
    sorteio_defesa = 0
    sorteio_turno_defesa = 0

    acao = input("escolha uma ação:\n[0] - sair\n[1] - ataque\n[2] - defesa" )
    if acao.isdigit():
      acao = int(acao)

      # ataque jogador
      if acao == 1:
        sorteio_dano = random.randint(1,20)
        sorteio_defesa = random.randint(1,20)
        
        # dano causado na rodada
        dano_turno_jogador = (((sorteio_dano/100) + 1) * dano_partida_jogador) - (defesa_partida_inimigo *((sorteio_defesa/100) + 1))
        print(f"({sorteio_dano} - bônus de ataque)/ ({sorteio_defesa} - bônus de defesa)")
        
        if dano_turno_jogador < 0:
          hp_partida_jogador = hp_partida_jogador + dano_turno_jogador
          print(f"você recebeu: {dano_turno_jogador:.2f} de dano")
          
          if hp_partida_jogador > 0:
            print(f"HP jogador: {hp_partida_jogador:.2f}")
            print(f"HP inimigo: {hp_partida_inimigo:.2f}")
          
          else:
            print("Você foi derrotado")
            print(f"HP jogador: {hp_partida_jogador:.2f}")
            print(f"HP inimigo: {hp_partida_inimigo:.2f}")
            return saldo
        else: 
          hp_partida_inimigo = hp_partida_inimigo - dano_turno_jogador
          print(f"você infringiu: {dano_turno_jogador:.2f} de dano")
          if hp_partida_inimigo > 0:
            print(f"HP jogador: {hp_partida_jogador:.2f}")
            print(f"HP inimigo: {hp_partida_inimigo:.2f}")
          else:
            print("Você derrotou o seu adversário")
            print(f"HP jogador: {hp_partida_jogador:.2f}")
            print(f"HP inimigo: {hp_partida_inimigo:.2f}")
            saldo = saldo + inimigos[monstro_adversario]["ouro"]
            print(f"você ganhou: {inimigos[monstro_adversario]['ouro']}")
            return saldo

      elif acao == 2:
        sorteio_turno_defesa = random.randint(1,20)
        defesa_turno_jogador = (((sorteio_turno_defesa/10) +1) * defesa_partida_jogador)
      
      elif acao == 0:
        return saldo

      else:
        print("digite um número válido!")
        continue
      
    # ataque inimigo
    sorteio_dano = random.randint(1,20)
    sorteio_defesa = random.randint(1,20)

    dano_turno_inimigo = (((sorteio_dano/100) + 1) * dano_partida_inimigo) - (defesa_turno_jogador *((sorteio_defesa/100) + 1))
    print(f"({sorteio_dano} - dado de ataque)/ ({sorteio_defesa} - dado de defesa)")

    if dano_turno_inimigo < 0:
      hp_partida_inimigo = hp_partida_inimigo + dano_turno_inimigo
      print(f"O seu adversário recebeu: {dano_turno_inimigo:.2f} de dano")
      if hp_partida_inimigo > 0:
        print(f"HP jogador: {hp_partida_jogador:.2f}")
        print(f"HP inimigo: {hp_partida_inimigo:.2f}")
      else:
        print("O seu adversário foi derrotado")
        print(f"HP jogador: {hp_partida_jogador:.2f}")
        print(f"HP inimigo: {hp_partida_inimigo:.2f}")
        saldo = saldo + inimigos[monstro_adversario]["ouro"]
        print(f"você ganhou: {inimigos[monstro_adversario]['ouro']}")
        return saldo
    else: 
      hp_partida_jogador = hp_partida_jogador - dano_turno_inimigo
      print(f"Seu inimigo infringiu: {dano_turno_inimigo:.2f} de dano")
      if hp_partida_jogador > 0:
        print(f"HP jogador: {hp_partida_jogador:.2f}")
        print(f"HP inimigo: {hp_partida_inimigo:.2f}")
      else:
        print("Você foi derrotado!")
        print(f"HP jogador: {hp_partida_jogador:.2f}")
        print(f"HP inimigo: {hp_partida_inimigo:.2f}")
        return saldo



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

#função para equipar os itens de combate
def equipando_itens(mochila, personagens, classe, itens_loja):
  inventario(mochila)
  item_escolhido = input("Qual item você quer equipar? ").lower().strip()
  if item_escolhido in mochila:
    tipo = itens_loja[item_escolhido]["tipo"]
    if personagens[classe]["equipamentos"][tipo] == "":
      personagens[classe]["equipamentos"][tipo] = item_escolhido
      personagens[classe]["defesa"] = (itens_loja[item_escolhido]["defesa"] + personagens[classe]["defesa"])
      personagens[classe]["dano"] = (itens_loja[item_escolhido]["dano"] + personagens[classe]["dano"])
      mochila.remove(item_escolhido)
    else:
      troca_item = personagens[classe]["equipamentos"][tipo]
      personagens[classe]["equipamentos"][tipo] = item_escolhido
      personagens[classe]["defesa"] = (personagens[classe]["defesa"] - itens_loja[troca_item]["defesa"])
      personagens[classe]["dano"] = (personagens[classe]["dano"] - itens_loja[troca_item]["dano"])
      mochila.append(troca_item)
      
      
      personagens[classe]["defesa"] = (itens_loja[item_escolhido]["defesa"] + personagens[classe]["defesa"])
      personagens[classe]["dano"] = (itens_loja[item_escolhido]["dano"] + personagens[classe]["dano"])
      mochila.remove(item_escolhido)
  else:
     print(f"você não tem o item {item_escolhido}")

# função para retirar os itens de combate     
def retirar_equipamento(mochila, personagens, classe, itens_loja):
  consultar_equipamento(personagens, classe)
  slot_escolhido = input("Qual slot você quer retirar? ").lower().strip()
  if slot_escolhido == "sair":
      print("obrigado pela visita!")
      return
  if slot_escolhido in personagens[classe]["equipamentos"]:
    item_equipado = personagens[classe]["equipamentos"][slot_escolhido]
    if item_equipado =="":
      print("você não tem nenhum item equipado nesse espaço!")

    else:
      personagens[classe]["equipamentos"][slot_escolhido] = ""
      personagens[classe]["defesa"] = personagens[classe]["defesa"] - itens_loja[item_equipado]["defesa"]
      personagens[classe]["dano"] = personagens[classe]["dano"] - itens_loja[item_equipado]["dano"]
      mochila.append(item_equipado)
  else:
    print("esse slot não existe")
  



#consultando equipamentos já equipados

def consultar_equipamento(personagens, classe):
   for tipo, equipamento in personagens[classe]["equipamentos"].items():
      if equipamento == "":
        equipamento = "vázio"
        print(f"{tipo}: {equipamento}")

      else:
        print(f"{tipo}: {equipamento}")
          

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
    print(classe)
    print(saldo)
    print(personagens[classe]["hp"])
    print(personagens[classe]["dano"])
    print(personagens[classe]["defesa"])



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
      print("obrigado pela visita")
    continue 

  if navigation == "sair":
    break




