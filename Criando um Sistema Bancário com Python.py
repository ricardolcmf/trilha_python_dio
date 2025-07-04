menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0

limite = 500
extrato = ""
contador_deposito = numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            contador_deposito += 1
            extrato += f"{contador_deposito}º Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"{numero_saques}º Saque: R$ {valor:.2f}\n"


        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "e":
        print("\n==============EXTRATO==============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {valor:.2f}")
        print("\n===================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")