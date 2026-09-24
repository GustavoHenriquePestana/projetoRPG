import random
from progressao import recompensa

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
  print(f"HP: {hp_jogador:.2f}")
  print(f"Dano: {dano_jogador:.2f}")
  print(f"Defesa: {defesa_jogador:.2f}")

  monstros_sorteados = list(inimigos.keys())
  monstro_adversario = random.choice(monstros_sorteados)

  print(f"Você foi atacado por: {monstro_adversario}")

  hp_inimigo = inimigos[monstro_adversario]["hp"]
  dano_inimigo = inimigos[monstro_adversario]["dano"]
  defesa_inimigo = inimigos[monstro_adversario]["defesa"]

  if personagens[classe]["nivel"] > 1:
    percentual_evo = (personagens[classe]['nivel'] - 1) * 0.10
    hp_inimigo = hp_inimigo * (1 + percentual_evo)
    dano_inimigo = dano_inimigo * (1 + percentual_evo)
    defesa_inimigo = defesa_inimigo * (1 + percentual_evo)  

  print("------------------")
  print("status do monstro")
  print(f"HP: {hp_inimigo:.2f}")
  print(f"Dano: {dano_inimigo:.2f}")
  print(f"Defesa: {defesa_inimigo:.2f}")

  defesa_partida_jogador = defesa_jogador
  dano_partida_jogador = dano_jogador
  hp_partida_jogador = hp_jogador

  defesa_partida_inimigo = defesa_inimigo
  dano_partida_inimigo = dano_inimigo
  hp_partida_inimigo = hp_inimigo

  cooldown_habilidades = 0
  turnos_efeito = 0

  while hp_partida_inimigo > 0 and hp_partida_jogador > 0:

    dano_turno_base = dano_partida_jogador
    defesa_inimigo_turno = defesa_partida_inimigo

    if turnos_efeito > 0 and classe == "barbaro":
      dano_turno_base = dano_partida_jogador * 1.50
      defesa_inimigo_turno = defesa_partida_inimigo * 0.80

    defesa_turno_jogador = defesa_jogador
    print(f"Cooldown: {cooldown_habilidades}")
    #sorteios 
    sorteio_dano = 0
    sorteio_defesa = 0
    sorteio_turno_defesa = 0

    acao = input("escolha uma ação:\n[0] - sair\n[1] - ataque\n[2] - defesa\n[3] - habilidade especial")
    if acao.isdigit():
      acao = int(acao)

      # ataque jogador
      if acao == 1:
        sorteio_dano = random.randint(1,20)
        sorteio_defesa = random.randint(1,20)
        
        # dano causado na rodada
        dano_turno_jogador = (((sorteio_dano/100) + 1) * dano_turno_base) - (defesa_inimigo_turno *((sorteio_defesa/100) + 1))
        print(f"({sorteio_dano:.2f} - bônus de ataque)/ ({sorteio_defesa:.2f} - bônus de defesa)")
        
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
            saldo = recompensa(personagens, classe, inimigos, monstro_adversario, saldo)
            return saldo

      elif acao == 2:
        sorteio_turno_defesa = random.randint(1,20)
        defesa_turno_jogador = (((sorteio_turno_defesa/10) +1) * defesa_partida_jogador)

      elif acao == 3:
        if cooldown_habilidades == 0:

          if classe == "barbaro":
            print("Você ativou a fúria dos guerreiros!")

            turnos_efeito = 3
            cooldown_habilidades = 5

        else:
          print ("Você ainda não pode usar essa habilidade!")
          continue

      
      elif acao == 0:
        return saldo

      else:
        print("digite um número válido!")
        continue
    else:
      print("você precisa digitar um número")
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
        saldo = recompensa(personagens, classe, inimigos, monstro_adversario, saldo)
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
   
    if cooldown_habilidades >0:
      cooldown_habilidades -= 1
    if turnos_efeito >0:
      turnos_efeito -= 1
