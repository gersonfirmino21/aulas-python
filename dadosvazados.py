import time
import random

email = ["katyasyl@yahoo.com.br","master.juliana@gmail.com","Andersondanze01@hotmail.com","paty_almeida1982@hotmail.com","ffortine40@hotmail.com","dmrtelecom89@gmai.com","isaug10@gmail.com","alvesj959@gmail.com","Cassia2015@gmail.com","rodrigueszapielo@gmail","bruna.fatima94@hotmail.com","tiago","andre","silvio","douglas","marcio","fabiano","soraia","juliana","fernanda","bossa","gustavo","ronaldo","gerson","alberico","cleiton"]

print("DADOS DOS FUNCIONARIOS DA DIRETORIA:")
print()
print()
dados =input("digite seu nome: ")
print("Seu nome esta vinculado a uma ---------------------infomação-------------------------------- vazada")
print()
time.sleep(1)
dadosdois =input("digite um email: ").upper()
time.sleep(1)
print("esse email esta na nossa lista ")
email.append(dadosdois)
print()
print("gostaria de conferir?")
print()
verificar= input("").upper()
if verificar == "sim".upper():   
    print()
    print("parabéns você esta fazendo o certo pela nossa SEGURANÇA INSTITUCIONAL")
    print()
else:
    print("Com esta atitude você contribui para falhas em segurança")
    
    print()
    print()
    print()
time.sleep(1)

      
resposta = input("digite \"Y\" para confirmar: ").upper() 
    
while resposta !="Y":
        resposta = input("digite \"Y\" para confirmar: ").upper()           
print()
print()
time.sleep(0.5)
print("Pegamos você, seu email agora esta vazado HAHAHAHHAAHA!!!!!")
    
print()
print()
print(                                 "LISTA VAZADA")
print()
for x in email :
        time.sleep(1)
        print(x)
        
        

       
print()
sorte= random.choice(email)
print("APENAS A SORTE PODERA LIBERTAR SEU EMAIL:\nOS NOMES DA LISTA EU VOU SORTEAR!!!!!!!")
print("SE SAIR --------- ALBERICO------------ seu email é LIBERTADO")
print()
print()
for x in email :
    time.sleep(1)
    print(x)
    print()
time.sleep(6)
print("O nome que saiu foi:", sorte)
print()
print()
if sorte== "alberico":
    print()
    print("parabéns seu email foi desVAZADO!!!!!!!!!!!")
else:
    print("VENDI SEU EMAIL NA DEEP, TENTE DENOVO MAIS TARDE!!!!!!!!")
    

