nome= input("nome do paciente: ")
idade= int(input("idade do paciente:"))
if idade  <=15:    
    print("voce esta dentro do grupo de risco:")
if idade  >=60:
    print("voce esta dentro do grupo de risco:")    
viagem= input("voce viajou para o exterior recentemente?:")      
if viagem =='sim':
    print("voce tem grandes chances de estar com covid-19:")

if viagem =='nao':
    print("voce provavelmente esta apenas gripado")
elif idade <=15:
    print("atendimento com plantonista")   
elif idade >=60:
    print("precisará ficar em observação")    
exames= input("voce gostaria de estar realizando um exame para garantir?:")
if exames =='sim':
    print("basta apenas informar seu numero de telefone que entraremos em contato:") 
if exames =='nao':
    
    print("vai com Deus")    
telefone= input("")                       
