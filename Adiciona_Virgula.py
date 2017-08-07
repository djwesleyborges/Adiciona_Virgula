'''
Este script le linha por linha de um arquivo .txt e coloca no final de cada linha uma virgula.

Ex:	

Entrada sem vírgula		Saida com vírgula
321						321,
465						465,
654						654,
789						789,
654						654,
789						789,


Author: Wesley Borges
'''

file1 = input("Caminho do Arquivo do SalesForce? ")
file2 = input("Onde você quer salvar o novo arquivo? ")
with open(file1, "r") as in_file:
    with open(file2, "a") as out_file:
        for word in in_file:
            word2 = word.replace("\n", ",")
            word3 = word2 + '\n'
            out_file.write(word3)
