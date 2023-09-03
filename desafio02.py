print("MENU\n")
print("[1] - deposito\n")
print("[2] - Saques\n")
print("[3] - Extrato\n")
print("[4] - criar usuario\n")
print("[5] - criar conta corrente\n")
print("[6] - listar contas\n")
print("[0] - sair\n")


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0
usuarios = []
contas = []

#teste de cpf
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
#criar usuario
def criar_usuario(usuarios):
    cpf = input("informe o cpf.\n")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("ja existe usuario com esse cpf")
        return
    
    nome = input("digite seu nome.\n")
    data = input("digite sua data de nascimento\n")
    endereco = input("digite seu endereço.\n")

    novo_usuario ={"nome":nome, "data":data, "cpf":cpf, "endereço":endereco}
    usuarios.append(novo_usuario)

    print("cadastro feito com sucesso")
#criar usuario
#realizar deposito#
def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"deposito: \tR$ {valor:.2f}\n"
        print(f"deposito: \tR$ {valor:.2f}\n")
    else:
        print("operação falhou!!\n")
    
    return saldo, extrato
##realizar deposito#
#saque
def saque(valor, saldo, extrato,LIMITE_SAQUES,numero_saques):

    
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
        print(numero_saques)
        print(LIMITE_SAQUES)
    else:
        print("operação invalida")
    
    return saldo, extrato
#saque
#criar_conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
#criar_conta
#extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")



while True:
    AGENCIA = "0001"
    opcao = int(input("digite a operaçao.\n"))

    if opcao == 1:
        valor = float(input("digite o valor que deseja depositar.\n"))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == 2:
        valor = float(input("digite o valor de saque desejado\n"))
        saldo, extrato = saque(valor, saldo, extrato, LIMITE_SAQUES, numero_saques)
        numero_saques = numero_saques + 1

    elif opcao == 3:
        exibir_extrato(saldo, extrato = extrato)
    
    
    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
    
    elif opcao == 0:
        break

    else:
        print("operação invalida, por favor selecione novamente a operação desejada.")







