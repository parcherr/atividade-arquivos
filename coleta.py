
while True:
    nome = str(input("Digite seu nome: ")).capitalize().strip()
    n1 = float(input("Digite sua nota 1: "))
    n2 = float(input("Digite sua nota 2: "))
    n3 = float(input("Digite sua nota 3: "))

    with open("notas.txt", "a") as notas:
        notas.write(f"{nome} \n")
        notas.write(f"{n1} \n")
        notas.write(f"{n2} \n")
        notas.write(f"{n3} \n")

    continuar = str(input("Deseja continuar? [S] [N]: ")).upper().strip()
    if continuar == "N":
        break

with open("notas.txt", "r") as notas:
    dados = []
    for linha in notas: 
        linha = linha.strip()
        if linha != "":
            dados.append(linha)

    count = 0
    for i in range(0, len(dados), 4):
        n1 = float(dados[i + 1])
        n2 = float(dados[i + 2])
        n3 = float(dados[i + 3])
        media = (n1 + n2 + n3) / 3
        nome = dados[count]
        count += 4

        if media >= 7:
            with open("aprovados.txt", "a") as aprovados:
                aprovados.write(f"{nome} \n")
                aprovados.write(f"{media} \n")
                aprovados.write(f"Aprovado sem exame! \n")
        elif 7 > media >= 5:
            with open("exame.txt", "a") as exame:
                exame.write(f"{nome} \n")
                exame.write(f"{media} \n")
        else: 
            with open("reprovados.txt", "a") as reprovados:
                reprovados.write(f"{nome} \n")
                reprovados.write(f"{media} \n")
                reprovados.write(f"Reprovado sem exame! \n")