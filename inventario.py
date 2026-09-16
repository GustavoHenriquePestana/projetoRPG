#função para consultar o dicionário

def inventario (mochila):
  inventario_agrupado = {}

  for item in mochila:
    if item in inventario_agrupado:
      inventario_agrupado[item] = inventario_agrupado[item] + 1
    else:
      inventario_agrupado[item] = 1

  for nome, quantidade in inventario_agrupado.items():
    print(f"{quantidade}x {nome}")