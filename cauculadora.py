
# coding: utf-8

# In[43]:


print("\n 👋 Bem vindo(a) à cauculadora da Tati ")
print("\n")
print("Para escolher a operação desejada digite um dos números abaixo:")
print("> Soma: +")
print("> Subtração: -")
print("> Multiplicação: *")
print("> Divisão: /")



operacao = ""
resultado = 0
attempt_count = 0


while operacao != "=" :
    
    if attempt_count == 0:
    
        operacao = input('\n 🧮 Qual operação deseja fazer? ')
        num1 = float(input("\n 🔢 Qual o primeiro numero? "))
        num2 = float(input("\n 🔢 Qual o segundo numero? "))
        attempt_count += 1
    
        if operacao == "+":
            resultado += num1 + num2
            print("\n 👉", num1,"+", num2, "=", resultado, "\n")

        elif operacao == "-":
            resultado = num1 - num2
            print("\n 👉", num1,"-", num2, "=", resultado, "\n")

        elif operacao == "*":
            resultado = num1 * num2
            print("\n 👉", num1,"x", num2, "=", resultado, "\n")

        elif operacao == "/":
            resultado = num1 / num2
            print("\n 👉", num1,"/", num2, "=", resultado, "\n")

        elif operacao == "=":
            print("\n 👉", "Seu resultado final é {}".format(resultado))

        else: 
            print("""\n 🛑 Erro! Por favor responda qual operação quer fazer digitando "+", "-", "*", "/".""")
            
        
        
    else:
        # operacao = input('\n 🧮 Qual operação deseja fazer com o resultado? ')
        other_num = input("\n 🔢 Outro número? ")
        attempt_count += 1
        
        if "n" not in other_num:
            if operacao == "+":
                old_total = resultado
                resultado = old_total + float(other_num)
                print("\n 👉", old_total, "+", other_num, "=", resultado, "\n")

            elif operacao == "-":
                old_total = resultado
                resultado = old_total - other_num
                print("\n 👉", old_total, "-", other_num, "=", resultado, "\n")
                
            elif operacao == "*":
                old_total = resultado
                resultado = old_total * other_num
                print("\n 👉", old_total, "*", other_num, "=", resultado, "\n")

            elif operacao == "/":
                old_total = resultado
                resultado = old_total / other_num
                print("\n 👉", old_total, "/", other_num, "=", resultado, "\n")
            else: 
                print("""\n 🛑 Erro! Por favor responda qual operação quer fazer digitando "+", "-", "*", "/".""")
        else:
            operacao = "=" 
            print("\n 👉", "Seu resultado final é {} \n \n \n 👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n".format(resultado))
            attempt_count = 0




