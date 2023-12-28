import csv

# Obtendo dados do usúario 

linguagemDoUser = (input("Me informe qual a linguagem que deseja aprender: \n"))
propositoDoUser = (input("Agora,me diga o que deseja desenvolver com ela: \n"))

with open("dio.csv","a", encoding= "utf-8") as file:
    writer = csv.writer(file,lineterminator = "\n")
    writer.writerow([linguagemDoUser,propositoDoUser])

# Criando uma lista e retornando um DICIONARIO 

minhaLista = []

with open("dio.csv","r",encoding = "utf-8") as lendoDados:
    lendo = csv.DictReader(lendoDados)
    for linha in lendo :
        minhaLista.append({"primeira coluna":linha["primeira coluna"],"segunda coluna":linha["segunda coluna"]})
print(minhaLista)