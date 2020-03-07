nome= input("nome do paciente: ")
idade= int(input("idade do paciente:"))
if idade  <=15:    
    print("voce esta dentro do grupo de risco:")
elif idade <=15:
    print("atendimento com plantonista")       
elif  idade  >=60:
    print("voce esta dentro do grupo de risco:")    
    
viagem= input("voce viajou para o exterior recentemente?:")      
if viagem =='sim':
    print("Seria bom realizar alguns exames:")

elif  viagem =='nao':
    print("voce provavelmente esta apenas gripado")
    
exames= input("voce gostaria de estar realizando um exame para garantir?:")
if exames =='sim':
    print("basta apenas informar seu numero de telefone que entraremos em contato:")
     
elif  exames =='nao':
        print("vai com Deus")    
telefone= input("")                        
