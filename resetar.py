import os

confirmacao = input("Tem certeza que deseja apagar tudo? [S] [N]: ").upper().strip()
arquivos = ["notas.txt", "exame.txt", "aprovados.txt", "reprovados.txt"]

if confirmacao == "S":

    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)

    print("Arquivos excluídos com sucesso!")