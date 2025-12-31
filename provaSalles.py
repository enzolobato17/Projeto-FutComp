# QUESTÃO 1 !!!!!


# #   16>=idade<=80    e     altura>=1,6m
# idade= int(input("qual sua idade?"))
# altura = float(input("Qual a sua altura?"))
# if (idade >= 16 and idade <= 80) and altura>= float(1.60):  
#     print("Você pode entrar!")
# else:
#     print("Você não pode entrar!")    
    


#    QUESTÃO DOISS!!!!!


#pedra papel tesoura / funçao winner verifica qm venceu
   
   #stone vence scissors / scissors vence paper / paper vence stone 
 
def winner(play1 , play2):
   if play1==play2: 
      return "draw"
   if play1 =="paper" and play2 =="stone" or play1== "stone" and play2 == "scissors" or play1== "scissors" and play2== "paper":
      return"play1 venceu"
   else:
      return"play2 venceu"
         



#     QUESTÃO 3!!!!

# precisa media 70 nas 3 primeiras - se não, vai p reposicao

def notaReposicao (nota1, nota2, nota3):
   soma = (nota1 + nota2 + nota3)
   
   if soma>= 210:
      print ("aprovado")
      return 0

   menor_nota = min(nota1, nota2, nota3)
   nota_necessaria = (210 - soma) + menor_nota
  
   if nota_necessaria > 100:    
      print ("Não tem como passar")
      return -1
   else:
      return nota_necessaria

#  QUARTA QUESTÃO !!! 

# ataque lanca 3 dados,   defesa defende c 3 dados / maior do atq compara c maior da def / valor do meio e o menor tbm / empate = def ganha 

def ataque(atq1, atq2, atq3, def1, def2, def3):
   