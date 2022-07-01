#Escrita
with open("primeiro_arquivo.txt", "a") as arquivo:

    arquivo.write("\nHakuna Matata!!")

#leitura
with open("primeiro_arquivo.txt", "r") as arquivo:

    for linha in arquivo.readlines():
        print(linha)
