
def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print()
            print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF mais de uma vez.")
            return None
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso!")
    return cpf


def criar_conta(contas, usuarios, cpf):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return None

    numero_conta = len(contas) + 1
    contas.append({
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    })
    print("Conta corrente criada com sucesso!")
    return numero_conta


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        for transacao in extrato:
            print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")
    print("==========================================")


def listar_contas(contas):
    print("\n=== LISTA DE CONTAS ===")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
    print("========================")


# Inicialização das listas de usuários, contas e outras variáveis
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do programa
while True:
    menu = """\n
    ====== SISTEMA BANCÁRIO ======
    [c] Criar usuário
    [ac] Criar conta corrente
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar contas
    [q] Sair
    => """
    
    opcao = input(menu)

    if opcao == "c":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF (apenas números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        if criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Falha ao cadastrar usuário. Verifique o CPF e tente novamente.")

    elif opcao == "ac":
        cpf = input("Informe o CPF do usuário para criar a conta: ")
        criar_conta(contas, usuarios, cpf)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite,
                                               numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")