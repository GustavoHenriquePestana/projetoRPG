import json

def salvar_jogo (classe, saldo, mochila, personagens):
    dados_save = {
        "classe": classe,
        "saldo": saldo,
        "mochila": mochila, 
        "personagem": personagens[classe]

    }

    with open("save.json", "w") as arquivo:
        json.dump(dados_save, arquivo, indent=4)