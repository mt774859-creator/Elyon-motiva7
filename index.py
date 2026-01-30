import random

respostas = {
    "triste": [
        "Sinto muito que te sintas assim. Mesmo os dias difíceis passam.",
        "Tu és mais forte do que pensas. Continua.",
        "Não estás sozinho. Respira fundo."
    ],
    "cansado": [
        "Descansar também é progresso.",
        "Faz uma pausa. Amanhã é um novo dia.",
        "O teu esforço é válido."
    ],
    "desmotivado": [
        "Pequenos passos também contam.",
        "Acredita em ti, mesmo quando é difícil.",
        "Tu consegues mais do que imaginas."
    ],
    "feliz": [
        "Que bom ouvir isso! Aproveita esse momento.",
        "A felicidade merece ser celebrada.",
        "Continua nesse caminho positivo!"
    ],
    "default": [
        "Conta-me mais sobre isso.",
        "Estou aqui para te ouvir.",
        "Os teus sentimentos são importantes."
    ]
}

def responder(mensagem):
    mensagem = mensagem.lower()

    for palavra in respostas:
        if palavra in mensagem:
            return random.choice(respostas[palavra])

    return random.choice(respostas["default"])

def main():
    print("🤖 IA Motivacional")
    print("Escreve 'sair' para terminar.\n")

    while True:
        user = input("Tu: ")

        if user.lower() == "sair":
            print("IA: Lembra-te, tu és importante. Até breve 💙")
            break

        resposta = responder(user)
        print("IA:", resposta)

if __name__ == "__main__":
    main()
