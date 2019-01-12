import os 

########## Variável ##########
result = 0

########## funções ##########

def show_help():
    clear_screen()
    print("Para escolher a operação desejada digite um dos números abaixo:")
    print("> Soma: +")
    print("> Subtração: -")
    print("> Multiplicação: *")
    print("> Divisão: /")
    print("> Resultado final: =")
    print("> Ajuda: 'HELP'")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def conta(num1, operat, num2):
    num1 = float(num1)
    num2 = float(num2)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Erro: conta recebeu uma operação não conhecida")
    print("👉 {} {} {} = {}".format(num1, operation, num2, result))
    return result

def show_result():
    print("\n 👉", "Seu resultado final é {}\n👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n".format(result))
    attempt_count = 0

############ inicio do programa ############ 

print("\n👋 Bem vindo(a) à cauculadora da Tati ")

show_help()

while True: #primeira conta
    input1 = input('\n🧮 Qual operação deseja fazer? ')
    
    if input1.upper() == "HELP":
        show_help()
        continue

    elif input1 == "+" or input1 == "-" or input1 == "/" or input1 == "*":
        operation = input1
        first_n = input("🔢 Primeiro número: ")
        second_n = input("🔢 Segundo número: ")
        if has_alphabet(first_n) == True or has_alphabet(second_n) == True:
            print("🚷 Por favor, digite um número.")
    
        else:
            result = conta(first_n, operation, second_n)
            break

    else:
        clear_screen()
        print("Digite a operação: + - * /")
        continue
        
while True: #contas sequentes
    others_inputs = input('• Número ou sinal: ')
    try: 
        if others_inputs.upper() == "HELP":
            show_help()
            continue

        elif others_inputs == "+" or others_inputs == "-" or others_inputs == "/" or others_inputs == "*":
            operation = others_inputs
            second_n = input("• Segundo número: ")
            result = conta(result, operation, second_n)
            continue
            
        # elif has_alphabet(others_inputs) == True:
        #     print("🚷 Por favor, digite números, sinais matematicos ou os comandos descritos no 'HELP.'")
        
        elif others_inputs == "=":
            show_result()
            break

        else:
            result = conta(result, operation, others_inputs)
    except ValueError:
        print("🚷🚷 Por favor, digite números, sinais matematicos ou os comandos descritos no 'HELP'")

