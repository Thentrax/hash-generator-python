import hashlib
from os import waitpid

print("Gerador de Hash MD5")
print("por Thiago Cardoso")

def addsenha():
    senha = input("Senha : ")
    output = hashlib.md5(senha.encode()).hexdigest()
    print(output)

    with open("key.txt", "a") as file:
        file.write("\n" + output)
        file.close()

addsenha()
outra = input("Adicionar mais? y/n ")
while outra:
    if(outra == "y"):
        addsenha()