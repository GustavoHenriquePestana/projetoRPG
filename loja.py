from inventario import inventario

#função para comprar item

def loja_comprar(saldo, mochila, itens_loja, capacidade_maxima):
  print("----------------------")
  print(f"Os itens disponiveis são:")
  catalogo_loja (itens_loja)
  print("qual deles você quer comprar?")
  print("----------------------")



  while True:
      item_escolhido = input("Digite o item escolhido (ou 'sair'): ").lower().strip()
      if item_escolhido =="sair":
          break
      if item_escolhido not in itens_loja:
          print("item inválido. Tente novamente.")
          continue
      if (len(mochila) >= capacidade_maxima):
        print("Você não tem espaço suficiente na mochila")
        continue
        
      preco_item = itens_loja[item_escolhido]["preco"]
      if saldo < preco_item:
        print(f"Saldo insuficiente! O item custa {preco_item}, mas você tem apenas {saldo}.\n")
        continue

      quantidade_compra = input("Quantas unidades você quer comprar? ")
      if quantidade_compra.isdigit():
        quantidade_compra = int(quantidade_compra)
      else:
        print("Erro! Você precisa digitar um número.")
        continue

      if (quantidade_compra + len(mochila)) > capacidade_maxima:
        print("Você não tem espaço suficiente para comprar todos esses itens")
        continue
      preco_total = preco_item * quantidade_compra
      if(preco_total > saldo):
        print("você não tem saldo suficiente para essa quantdade de itens.")
        continue                   
              
      saldo = saldo - preco_total

      for item in range (quantidade_compra):
        mochila.append(item_escolhido)
      print(f"Compra do item {item_escolhido} concluída!")
      print(f"Seu novo saldo é de {saldo} moedas.")
      print(f"Seu inverntário agora contém:")
      inventario(mochila)
      
    
  return saldo


#função para vender itens

def loja_vender(saldo, mochila, itens_loja):

    print(f"Seus itens são:")
    inventario(mochila)
    print("Qual deles você quer vender?")

    while True:
        item_escolhido = input("Digite o item escolhido (ou 'sair): ").lower().strip()
        if item_escolhido == "sair":
            break

        if item_escolhido not in mochila:
            print("você não tem esse item")
            continue

        quantidade_venda = input("Quantas unidades você quer vender?: ")
        if quantidade_venda.isdigit():
          quantidade_venda = int(quantidade_venda)
        else: 
          print("valor inválido, digite um número!")
          continue

        quantidade_mochila = mochila.count(item_escolhido)

        if quantidade_mochila >= quantidade_venda:
          saldo = (itens_loja[item_escolhido]["preco"]*quantidade_venda) + saldo
          
          for item in range(quantidade_venda):
            mochila.remove(item_escolhido)

          print(f"item {item_escolhido}, vendido")
          print(f"agora seu saldo é de {saldo}")
        else:
          print("você não tem essa quantidade de itens")
          continue
    return saldo

#função para consultar os itens da loja

def catalogo_loja (itens_loja):
  for nome, atributos in itens_loja.items():
    print(f"{nome}: {atributos['preco']}")