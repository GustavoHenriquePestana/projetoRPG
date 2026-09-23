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

def carregar_jogo():
    with open("save.json", "r") as arquivo:
        dados_save = json.load(arquivo)
        return ( 
            dados_save["classe"], 
            dados_save["saldo"], 
            dados_save["mochila"], 
            dados_save["personagem"]
        )