# Projeto Final Python
# Sistema de Gestão de Alunos

# lista onde os alunos serão guardados
alunos = []

# função para adicionar aluno
def adicionar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade do aluno: ")
    curso = input("Curso do aluno: ")
    numero = input("Número do aluno: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "numero": numero
    }

    alunos.append(aluno)
    print("Aluno adicionado com sucesso!\n")


# função para listar alunos
def listar_alunos():
    if len(alunos) == 0:
        print("Não existem alunos registados.")
    else:
        print("\nLista de alunos:")
        for aluno in alunos:
            print("-----------------------")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
            print("Número:", aluno["numero"])


# função para procurar aluno
def procurar_aluno():
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("Aluno encontrado:")
            print(aluno)
            return

    print("Aluno não encontrado.")


# função para remover aluno
def remover_aluno():
    nome = input("Nome do aluno a remover: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print("Aluno removido com sucesso.")
            return

    print("Aluno não encontrado.")


# função extra: mostrar total de alunos
def total_alunos():
    print("Total de alunos registados:", len(alunos))


# menu principal
while True:

    print("\n===== SISTEMA DE GESTÃO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Procurar aluno")
    print("4 - Remover aluno")
    print("5 - Total de alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        procurar_aluno()

    elif opcao == "4":
        remover_aluno()

    elif opcao == "5":
        total_alunos()

    elif opcao == "0":
        print("Programa terminado.")
        break

    else:
        print("Opção inválida.")
