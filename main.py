from personagens import personagens, classes
from inimigos import inimigos
from itens import itens_loja
from loja import loja_comprar, loja_vender
from inventario import inventario
from combate import iniciar_combate
from equipamentos import equipando_itens, retirar_equipamento, consultar_equipamento
from menus import escolherClasse, escolherOperacao, navegacao, acao_equipamento
from status import mostrar_status

mochila = []



operacoes = ["sair", "comprar", "vender", "consultar"]

menuPrincipal = ["sair","loja de equipamentos", "zona de combate", "zona de equipamento"]

zonaEquipamento = ["sair", "consultar", "equipar", "retirar"]


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




