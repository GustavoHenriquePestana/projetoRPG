from personagens import personagens, classes
from inimigos import inimigos, chefe_final
from itens import itens_loja
from loja import loja_comprar, loja_vender
from inventario import inventario
from combate import iniciar_combate
from equipamentos import equipando_itens, retirar_equipamento, consultar_equipamento
from menus import escolherClasse, escolherOperacao, navegacao, acao_equipamento, menu_inicial
from status import mostrar_status
from save import salvar_jogo, carregar_jogo
from pathlib import Path


escolha_inicial = ["sair", "novo", "carregar"]


operacoes = ["sair", "comprar", "vender", "consultar"]
menuPrincipal = ["sair","loja de equipamentos", "zona de combate", "zona de equipamento"]
zonaEquipamento = ["sair", "consultar", "equipar", "retirar"]

inicio = menu_inicial(escolha_inicial)

if inicio == "novo":
  mochila = []
  print("Vamos começar a explorar o mundo!")
  print("Escolha a classe do seu personagem")

  classe = escolherClasse(classes)

  saldo = personagens[classe]["saldo_inicial"]
  capacidade_maxima = personagens[classe]["capacidade"]

elif inicio == "carregar":
  jogo_salvo = Path("save.json")

  if jogo_salvo.is_file():
    classe, saldo, mochila, personagem_salvo = carregar_jogo()

    personagens[classe] = personagem_salvo
    capacidade_maxima = personagens[classe]["capacidade"]

    print("jogo carregado com sucesso")

  else:
    print("nenhum jogo salvo encontrado")
    exit()
elif inicio == "sair":
  exit()
#invocando função para comprar item
try:
  while True:
    mostrar_status(personagens, classe, saldo)
    menuPrincipal = [
      "sair",
      "loja de equipamentos",
      "zona de combate",
      "zona de equipamento"
    ]

    if personagens[classe]["nivel"] >= 10:
      menuPrincipal.append("chefe final")

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
          inventario(mochila)
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

    if navigation == "chefe final":
      print(chefe_final)

    if navigation == "sair":
      salvar_jogo(classe, saldo, mochila, personagens)
      print("\njogo salvo com sucesso.")
      break
except KeyboardInterrupt:
  salvar_jogo(classe, saldo, mochila, personagens)
  print("\njogo salvo antes de sair.")


