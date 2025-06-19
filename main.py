import os
import time
import gerador  # Importa o gerador de senha

# Listas para armazenar dados temporários
lista = []
lista_usuario = []
lista_arquivo_usuario = []
lista_arquivo_senha = []

# Variável para controle de login
logado = False


# Classe da conta
class conta:
    def __init__(self, titular, saldo):
        self.__saldo = saldo
        self.titular = titular

    def get_nome(self):
        return self.__saldo
    
    def mostrar_saldo(self):
        print(f"O saldo atual e de {self.__saldo}")

    def aumentar_saldo(self):
        self.__saldo += p_aumentar_saldo

    def sacar_saldo(self):
        if p > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= p_sacar_saldo


# Função para criar ou gerar senha
def criar_senha():
    while True:
        print("Criar - 1")
        print("Gerar - 2")
        try:
            pergunta_gerar_criar = int(input("Criar uma senha ou gerar uma senha? \n"))
            os.system("cls")
        except ValueError:
            print("Digite apenas 1 ou 2")
            time.sleep(1)
            os.system("cls")
            continue
        except KeyboardInterrupt:
            print("Copie usando o mouse")
            time.sleep(1)
            os.system("cls")
            continue
         
        if pergunta_gerar_criar == 2:
            gerar1 = gerador.gerador_de_senha()
            print(gerar1)
            lista.append(gerar1)
            print("Copie essa senha")
            with open("conta.txt", "a") as arquivo:
                arquivo.write(gerar1 + "\n")
            time.sleep(4)
            os.system("cls")
            break

        elif pergunta_gerar_criar == 1:
            os.system("cls")
            print("Ok, o minimo de caracteres e 6 e o maximo e 15")
            pergunta_criar_senha = input("")

            if len(pergunta_criar_senha) < 6:
                print("Senha muito curta")
                time.sleep(1)
                os.system("cls")
            elif len(pergunta_criar_senha) > 15:
                print("A senha e muito grande")
                time.sleep(1)
                os.system("cls")
            else:
                lista.append(pergunta_criar_senha)
                os.system("cls")
                print("Ok, senha criada")
                time.sleep(1)
                os.system("cls")
                with open("conta.txt", "a") as arquivo:
                    arquivo.write(pergunta_criar_senha + "\n")
                break
        else:
            print("Digite apenas 1 ou 2")
            time.sleep(1)
            os.system("cls")


# Função para criar usuário
def criar_usuario():
    pergunta_usuario = input("Qual e seu nome de usuario?\n")
    lista_usuario.append(pergunta_usuario)
    with open("conta.txt", "a") as arquivo:
        arquivo.write(pergunta_usuario + "\n")
    time.sleep(1)
    os.system("cls")


# Menu principal
def menu():
    print("1 - Ver saldo")
    print("2 - Adicionar")
    print("3 - Sacar")
    print("4 - Redefinir senha")
    print("0 - sair")


# Verificar se a conta já existe
def conta_existe():
    global logado
    pergunta_conta = input("Voce ja tem uma conta? \n")
    if pergunta_conta.lower() == "sim":
        os.system("cls")
        if os.path.exists("conta.txt"):
            with open("conta.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                if len(linhas) >= 2:
                    usuario = linhas[0].strip()
                    senha = linhas[1].strip()

                    lista_arquivo_usuario.append(usuario)
                    lista_arquivo_senha.append(senha)

                    print("Voce quer logar com a seguinte conta?")
                    print(usuario)
                    print(senha)

                    pergunta_conta_existente = input("")
                    if pergunta_conta_existente.lower() == "nao":
                        logado = False
                        os.system("cls")
                    if pergunta_conta_existente.lower() == "sim":
                        logado = True
                        return True
                else:
                    print("Arquivo incompleto. Crie uma nova conta.")
                    return False
        else:
            print("Nao, voce nao possui uma conta")
            return False
    elif pergunta_conta.lower() == "nao":
        os.system("cls")
        print("Ok, vamos criar uma")
        time.sleep(2)
        os.system("cls")
        return False
    else:
        print("Resposta inválida. Digite 'sim' ou 'nao'.")
        return False


# Inicia a conta
add = conta("Wendell", 0)

# Checar se existe conta
conta_existe()

# Criar usuario e senha se não tiver conta
if not logado:
    criar_usuario()
    criar_senha()


# Login caso não esteja logado
if not logado:
    while True:
        pergunta_usuario1 = input("Digite o seu nome de usuario (1 de 3)\n")
        if pergunta_usuario1 in lista_usuario or pergunta_usuario1 in lista_arquivo_usuario:
            os.system("cls")
            break
        else:
            time.sleep(1)
            os.system("cls")
            print("Usuario incorreto!")
            pergunta_usuario2 = input("Digite o seu nome de usuario (2 de 3)\n")
            if pergunta_usuario2 in lista_usuario or pergunta_usuario2 in lista_arquivo_usuario:
                os.system("cls")
                break
            else:
                time.sleep(1)
                os.system("cls")
                print("Usuario incorreto!")
                pergunta_usuario3_ultima = input("Digite o seu nome de usuario (3 de 3)\n")
                if pergunta_usuario3_ultima in lista_usuario or pergunta_usuario3_ultima in lista_arquivo_usuario:
                    os.system("cls")
                    break
                else:
                    print("Usuario incorreto!")
                    print("Voce foi bloqueado")
                    exit()

    while True:
        pergunta_senha1 = input("Digite a sua senha (1 de 3)\n")
        if pergunta_senha1 in lista or pergunta_senha1 in lista_arquivo_senha:
            os.system("cls")
            menu()
            break
        else:
            os.system("cls")
            print("Senha incorreta! Tente novamente.")
            pergunta_senha2 = input("Digite a sua senha (2 de 3)\n")
            if pergunta_senha2 in lista or pergunta_senha2 in lista_arquivo_senha:
                os.system("cls")
                menu()
                break
            else:
                os.system("cls")
                print("Senha incorreta! Tente novamente.")
                pergunta_senha3_ultima = input("Digite a sua senha (3 de 3)\n")
                if pergunta_senha3_ultima in lista or pergunta_senha3_ultima in lista_arquivo_senha:
                    os.system("cls")
                    menu()
                    break
                else:
                    os.system("cls")
                    print("Senha incorreta")
                    print("Voce foi bloqueado")
                    exit()
else:
    menu()


# Loop principal do programa
while True:
    try:
        p = int(input())
    except ValueError:
        os.system("cls")
        print("Digite um número válido")
        time.sleep(1)
        os.system("cls")
        menu()
        continue

    if p == 1:
        add.mostrar_saldo()
        time.sleep(1)
        os.system("cls")
        menu()

    elif p == 2:
        os.system("cls")
        try:
            p_aumentar_saldo = int(input("Quanto de saldo voce quer adicionar \n"))
        except ValueError:
            print("Digite um número válido para o saldo")
            time.sleep(1)
            os.system("cls")
            menu()
            continue

        print(f"Voce adicionou {p_aumentar_saldo} na sua conta")
        add.aumentar_saldo()
        time.sleep(2)
        os.system("cls")
        menu()

    elif p == 3:
        senha_sacar = input("Digite a senha\n")
        os.system("cls")
        if senha_sacar in lista or senha_sacar in lista_arquivo_senha:
            try:
                p_sacar_saldo = int(input("Digite o saldo que voce quer sacar\n"))
            except ValueError:
                print("Digite um número válido para sacar")
                time.sleep(1)
                os.system("cls")
                menu()
                continue

            print(f"Voce sacou {p_sacar_saldo} da sua conta")
            time.sleep(2)
            os.system("cls")
            add.sacar_saldo()
            os.system("cls")
            menu()
        else:
            print("Senha incorreta!")
            time.sleep(2)
            os.system("cls")
            menu()

    elif p == 4:
        pergunta_redefinir = input("Digite a sua senha atual (1 de 3)\n")
        if pergunta_redefinir in lista or pergunta_redefinir in lista_arquivo_senha:
            trocar_senha = input("Digite a sua nova senha \n")
            lista.clear()
            lista.append(trocar_senha)
            os.system("cls")
            menu()
        else:
            print("Senha errada (1)")
            time.sleep(2)
            os.system("cls")
            menu()

        pergunta_redefinir2 = input("Digite a sua senha atual (2 de 3)\n")
        if pergunta_redefinir2 in lista or pergunta_redefinir2 in lista_arquivo_senha:
            trocar_senha2 = input("Digite a sua nova senha \n")
            lista.clear()
            lista.append(trocar_senha2)
        else:
            print("Senha errada (2)")
            time.sleep(1)
            os.system("cls")
            menu()

        pergunta_redefinir3 = input("Digite a sua senha atual (3 de 3) \n")
        if pergunta_redefinir3 in lista or pergunta_redefinir3 in lista_arquivo_senha:
            trocar_senha3 = input("Digite a sua nova senha \n")
            lista.clear()
            lista.append(trocar_senha3)
        else:
            os.system("cls")
            print("Senha errada")
            print("Voce foi bloqueado")
            break

    elif p == 0:
        print("Finalizando codigo...")
        time.sleep(3)
        os.system("cls")
        break

    else:
        os.system("cls")
        print("Opção inválida, tente novamente.")
        time.sleep(1)
        os.system("cls")
        menu()
