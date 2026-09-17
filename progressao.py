def recompensa (personagens, classe, inimigos, monstro_adversario, saldo):
    #atualizar ouro quando vence
    saldo = saldo + inimigos[monstro_adversario]["ouro"]
    print(f"você ganhou: {inimigos[monstro_adversario]['ouro']}")
    
    #atualizar xp quando vence
    personagens[classe]["xp"] = personagens[classe]["xp"] + inimigos[monstro_adversario]["xp"]
    print(f"você ganhou: {inimigos[monstro_adversario]['xp']} de xp")
    
    while personagens[classe]["xp"] >= personagens[classe]["xp_necessario"]:
        personagens[classe]["nivel"] = (personagens[classe]["nivel"] + 1)
        personagens[classe]["dano"] = (personagens[classe]["dano"] + 5)
        personagens[classe]["defesa"] = (personagens[classe]["defesa"] + 5)
        personagens[classe]["hp"] = (personagens[classe]["hp"] + 20)
        personagens[classe]["xp"] = (personagens[classe]["xp"] - personagens[classe]["xp_necessario"])
        personagens[classe]["xp_necessario"] = (personagens[classe]["xp_necessario"] + 50)
        print(f"Parabéns! Você subiu de nível! Agora você é nível {personagens[classe]['nivel']}")
    return saldo