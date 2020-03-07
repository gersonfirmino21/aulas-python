nome= input("digite o seu nome: ")
acesso= input("login: ")
if acesso =='ADM':
    print("acesso autorizado")
elif acesso =='URS':
    print("acesso autorizado")
elif  acesso =='GUEST':
    print("acesso autorizado")        
else:
    print("usuario desconhecido")  
      
genero= input("qual o seu genero:") 
if genero =='feminino' and acesso =='ADM':
    print("ola administradora:")
elif genero =='masculino' and acesso =='ADM':
    print("ola administrador")    
elif genero =='feminino' and acesso =='URS':
    print("ola usuaria") 
elif genero =='masculino' and acesso =='URS':
    print("ola usuario")
elif genero =='femino' or 'masculino' and acesso =='GUEST':
    print("ola visitante" )   
else:
    print("login invalido")   
