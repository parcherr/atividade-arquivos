#while True:
with open("exame.txt", "r") as exame:
    dados = []
    for linha in exame: 
        linha = linha.strip()
        if linha != "":
            dados.append(linha)
    for i in range(0, len(dados), 2):
        n_exame = float(input(f"Digite a nota do {dados[i]} no exame: "))
        media = (n_exame + float(dados[i + 1])) / 2
        if media >= 5: 
            with open("aprovados.txt", "a") as aprovados:
                aprovados.write(f"{dados[i]} \n")
                aprovados.write(f"{media} \n")
                aprovados.write("Aprovado pelo exame! \n")
        else:
            with open("reprovados.txt", "a") as reprovados: 
                reprovados.write(f"{dados[i]} \n")
                reprovados.write(f"{media} \n")
                reprovados.write("Reprovado pelo exame! \n")