from inventario import inventario

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