#Rafael Carlos dos Santos
#Teste dev WebDeveloper Eduqu

n = 6 #número de fileiras
n=n*2 
x = (n // 2)-1 #Resto da entrada -1 
y = 1 # Contador para imprimir "*"

while x != 0:
    while y < (n):
        print("_" * x, end="") #End para tirar a quebra de linha
        print("*" * y, end="") #End para tirar a quebra de linha
        print("_" * x, end="\n")
        x = x - 1
        y = y + 2




