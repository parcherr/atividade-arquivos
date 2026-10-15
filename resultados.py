with open("aprovados.txt", "r") as aprovados:
    dadosa = []
    for linha in aprovados: 
        linha = linha.strip()
        if linha != "":
            dadosa.append(linha)

with open("reprovados.txt", "r") as reprovados:
    dadosr = []
    for linha in reprovados: 
        linha = linha.strip()
        if linha != "":
            dadosr.append(linha)

print("Aluno; Média Final; Situacao/Legenda.")

for i in range(0, len(dadosa), 3):
    print(f"{dadosa[i]}; {dadosa[i + 1]}; {dadosa[i + 2]}.")

for i in range(0, len(dadosr), 3):
    print(f"{dadosr[i]}; {dadosr[i + 1]}; {dadosr[i + 2]}.")