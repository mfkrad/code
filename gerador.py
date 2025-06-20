import random
import string

def gerador_de_senha():
    # gerar a senha aleatória
    senha_nova = []

    gerador = 0
    while gerador < 5:
        # adiciona letra aleatória
        letra_aleatoria = random.choice(string.ascii_letters)
        senha_nova.append(letra_aleatoria)

        # adiciona número aleatório
        numero_aleatorio = random.choice(string.digits)
        senha_nova.append(numero_aleatorio)

        # adiciona caractere especial aleatório
        caractere_aleatorio = random.choice(string.punctuation)
        senha_nova.append(caractere_aleatorio)

        gerador += 1

    # remove aspas simples da senha
    while "'" in senha_nova:
        senha_nova.remove("'")
        numero_extra = random.choice(string.digits)
        senha_nova.append(numero_extra)

    # remove vírgulas da senha
    while "," in senha_nova:
        senha_nova.remove(",")
        numero_extra = random.choice(string.ascii_lowercase)
        senha_nova.append(numero_extra)

    # junta lista em string
    juntar = "".join(senha_nova)
    return juntar
