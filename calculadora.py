import os 

########## Variável ##########
result = 0
equacao = ""
operat = ""

########## funções ##########

def show_help():
    clear_screen()
    print("> Resultado final: =")
    print("> Ajuda: 'HELP'")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def conta(num1, operacao, num2):
    num1 = float(num1)
    num2 = float(num2)
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2

def show_result():
    print("\n 👉", "Seu resultado final é {}\n \n👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n".format(result))

def inserit_in_equacao(to_add, local): 
        clear_screen()
        local = "{} {} _".format(local[:-1], to_add)
        print("\n")
        print(local, "\n")
        return local

############ inicio do programa ############ 

show_help()

equacao = "_"
print(equacao)

while True:
    try: 
        if len(equacao) < 3: #primeira conta
            num = input("digite um numero: ")
            equacao = inserit_in_equacao(num, equacao)
            result = num

            operat = input("digite + - * / : ")
            equacao = inserit_in_equacao(operat, equacao)


            if num.upper() == "HELP" or operat.upper() == "HELP" :
                show_help()

            elif num == "=" or operat == "=":
                show_result()
                break
            else:    
                float(num) # averiguando se foi digitado um numero

        else:
            if num.upper() == "HELP" or operat.upper() == "HELP" :
                show_help()

            elif num == "=" or operat == "=":
                show_result()
                break

            else:    
                num = input("digite um numero: ")
                equacao = inserit_in_equacao(num, equacao)
                result = conta(result, operat, num)
                print("= {}".format(result))

                same_operat = operat
                operat = input("digite + - * / : ")
                if operat == "+" or operat == "-" or operat == "*" or operat == "/": 
                    equacao = inserit_in_equacao(operat, equacao)
                
                else: 
                    equacao = inserit_in_equacao(same_operat, equacao)
                    operat = same_operat

                print("= {}".format(result))              

    except ValueError:
        print("🚷🚷 Por favor, digite números, sinais matematicos ou os comandos descritos no 'HELP'")
        continue
