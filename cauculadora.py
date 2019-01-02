
# coding: utf-8

# In[43]:


print("\n** Bem vindo(a) à cauculadora da Tati **")
print("\n")
print("Para escolher a operação desejada digite um dos números abaixo:")
print("> Soma = 1")
print("> Subtração = 2")
print("> Multiplicação = 3")
print("> Divisão = 4")

operacao = int(input('\nQual operação deseja fazer? '))
num1 = int(input("\nQual o primeiro numero? "))
num2 = int(input("\nQual o segundo numero? ")) 
    
if operacao == 1:
    resultado = num1 + num2
    print("\n>>>", num1,"+", num2, "=", resultado, "\n")
    
elif operacao == 2:
    resultado = num1 - num2
    print("\n>>>", num1,"-", num2, "=", resultado, "\n")
    
elif operacao == 3:
    resultado = num1 * num2
    print("\n>>>", num1,"x", num2, "=", resultado, "\n")
    
elif operacao == 4:
    resultado = num1 / num2
    print("\n>>>", num1,"/", num2, "=", resultado, "\n")

else: 
    print("\n", "*** Erro! Por favor responda escolha os números indicados. 1 soma, 2 subtração, 3 multiplicação e 4 divisão **")   

