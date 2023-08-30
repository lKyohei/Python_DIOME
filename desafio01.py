print("MENU\n")
print("[1] - deposito\n")
print("[2] - Saques\n")
print("[3] - Extrato\n")
print("[0] - sair\n")


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0



while True:
    opcao = int(input("digite a operaçao.\n"))

    if opcao == 1:
        print("deposito\n")
        saldo = float(input("qual o valor que deseja depositar.\n"))
        extrato += f"deposito: R$ {saldo:.2f}\n"
        print(f"seu saldo apos o deposito e de R${saldo}")

    elif opcao == 2:
        valor = float(input("digite o valor de saque desejado\n"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        execedeu_saques = numero_saques >= LIMITE_SAQUES
        

        if excedeu_saldo:
            print("sem saldo na conta.\n")
        
        elif excedeu_limite:
            print("excedeu o limite da conta.\n")
        
        elif execedeu_saques:
            print("execedeu o limite de saques diarios")
        
        elif valor > 0:
            saldo -= valor 
            extrato += (f"saque: R$ {valor:.2f}\n")
            print(f"saque: R$ {valor:.2f}\n")
            numero_saques += 1
       
        else:
            print("operação invalida")
        
        
    elif opcao == 3:
        print("\n=============extrato==============")
        print("não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("====================================")

    elif opcao == 0:
        break

    else:
        print("operação invalida, por favor selecione novamente a operação desejada.")







