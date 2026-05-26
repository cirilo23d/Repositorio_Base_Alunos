import os
from datetime import datetime

os.system("cls") #clear screen
hora = int(input("Digite a hora de agora: "))

if hora < 12: 
    mensagem = "Bom dia 🌤️"
elif hora < 18:
    mensagem = "Boa tarde ⛅"
else:
    mensagem = "Boa noite 💤"

os.system(f"start cmd /k echo {mensagem}")