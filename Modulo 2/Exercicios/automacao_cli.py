import os
import shutil

#os.getcwd() - Mostra a pasta atual
#os.listdir() - Lista arquivos e pastas
#os.mkdir("pasta") - Cria uma pasta
#os.remove("pasta") - Remove uma pasta
#shutil.move("origem", "destino") - Move uma pasta da origem ao destino.
#os.system("comando") - Executa um comando.

print("CRiador de pastas")
pasta = input("Digite o nome da pasta que deseja criar: ")
os.mkdir(pasta)