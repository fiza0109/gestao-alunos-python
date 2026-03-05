# Sistema de Gestão de Alunos

alunos = []

def adicionar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    print("Aluno adicionado!\n")


def listar():
    if len(alunos) == 0:
        print("Nenhum aluno registado.\n")
    else:
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
            print("---------")


def procurar():
    nome = input("Nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("Aluno encontrado:")
            print(aluno)
            return

    print("Aluno não encontrado.")


def remover():
    nome = input("Nome do aluno a remover: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print("Aluno removido!")
            return

    print("Aluno não encontrado.")


def total():
    print("Total de alunos:", len(alunos))


while True:

    print("\n===== GESTÃO DE ALUNOS =====")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Procurar")
    print("4 - Remover")
    print("5 - Total de alunos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        procurar()

    elif opcao == "4":
        remover()

    elif opcao == "5":
        total()

    elif opcao == "0":
        print("Programa terminado.")
        break

    else:
        print("Opção inválida.")
