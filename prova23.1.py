# questão 1

# vm = AS / AT

distancia = 260 
tempo = float(input("Qual a duração da viagem (2.0 para 2 horas)"))

velocidade = distancia / tempo 

print (velocidade)

# questão 2

# verificar se 5 valores de 5 dados lansados sao iguais (6 faces)  / se 5 valores iguais, é Yahtzee
# funcao yahtzee true qnd 5 valores iguais / false qnd diferentes

def yahtzee (d1:int, d2:int, d3:int, d4:int, d5:int) -> bool:
    if (d1 == 1 and d2 == 1 and d3 == 1 and d4 == 1 and d5 == 1):
            return True
    if (d1 == 2 and d2 == 2 and d3 == 2 and d4 == 2 and d5 == 2):
          return True
    if (d1 == 3 and d2 == 3 and d3 == 3 and d4 == 3 and d5 == 3):
          return True                                                   #PODERIA USAR COMPARAÇÃO DIRETA
    if (d1 == 4 and d2 == 4 and d3 == 4 and d4 == 4 and d5 == 4):        # return d1 == d2 == d3 == d4 == d5 
          return True
    if (d1 == 5 and d2 == 5 and d3 == 5 and d4 == 5 and d5 == 5):
          return True
    if (d1 == 6 and d2 ==6 and d3 == 6 and d4 == 6 and d5 == 6):
          return True
    else:
          return False
          
# questão 3

#identificar full house =  em 5 dados, uma trinca (3) igual e um par (2) igual

def fullhouse (d1: int, d2: int, d3:int, d4:int, d5: int) -> bool:
     
  
 
 
# questão 4

# func retorna soma de tds resultados d1 ate d5 q sao iguais a value (parametro)

def sumCount (value: int, d1: int, d2: int, d3: int, d4:int, d5:int) -> int:
    dados = (d1, d2, d3, d4, d5)
    return dados.count(value)*value


#questão 4 outra resolução

def sumCount (value: int, d1: int, d2: int, d3: int, d4:int, d5:int) -> int:
    contador = 0
    if value == d1:
         contador = contador + 1
    if value == d2:
         contador = contador + 1
    if value == d3:
         contador = contador + 1
    if value == d4: 
         contador = contador + 1
    if value == d5:
         contador = contador + 1
    return (value * contador)
        


#questão 5

#usu informa 4 inteiros quaisquer / 
#prog verifica se    menor + maior    é  maior, igual ou menor    que os outros dois

def conta_valores ( n1:int, n2:int, n3:int, n4:int):
    n1 = int(input("informe n1 qualquer: "))
    n2 = int(input("Informe n2 qualquer: "))
    n3 = int(input("Informe n3 qualquer: "))
    n4 = int(input("Informe n4 qualquer: "))

    maior = max(n1, n2, n3, n4)
    menor = min(n1, n2, n3, n4)
    meio = n1 + n2 + n3 + n4 - maior - menor
    if maior + menor > meio:
         print("Maior")
         return 2
    if maior + menor == meio:
         print ("Igual")
         return 1
    else:
         print("Menor")
         return 0 

    


