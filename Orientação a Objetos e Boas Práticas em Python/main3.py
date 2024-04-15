class Plano:
    """
    Classe para representar um plano de telefone.
    
    Atributos:
        saldo (float): Saldo disponível no plano.
    
    Métodos:
        verificar_saldo(): Retorna o saldo atual do plano.
        custo_chamada(duracao): Calcula o custo da chamada com base na duração.
        deduzir_saldo(valor): Deduz um valor do saldo do plano.
    """
    
    def __init__(self, saldo_inicial):
        """
        Inicializa um novo objeto Plano.
        
        Args:
            saldo_inicial (float): Saldo inicial do plano.
        """
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        """
        Retorna o saldo atual do plano.
        
        Returns:
            float: Saldo do plano.
        """
        return self.__saldo

    def custo_chamada(self, duracao):
        """
        Calcula o custo da chamada com base na duração.
        
        Args:
            duracao (int): Duração da chamada em minutos.
        
        Returns:
            float: Custo da chamada.
        """
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        """
        Deduz um valor do saldo do plano.
        
        Args:
            valor (float): Valor a ser deduzido do saldo.
        """
        self.__saldo -= valor


class UsuarioTelefone:
    """
    Classe para representar um usuário de telefone.
    
    Atributos:
        nome (str): Nome do usuário.
        numero (str): Número de telefone do usuário.
        plano (Plano): Plano do usuário.
    
    Métodos:
        fazer_chamada(destinatario, duracao): Realiza uma chamada para um destinatário com uma determinada duração.
        __str__(): Retorna uma mensagem indicando que o usuário foi criado com sucesso.
    """
    
    def __init__(self, nome, numero, plano):
        """
        Inicializa um novo objeto UsuarioTelefone.
        
        Args:
            nome (str): Nome do usuário.
            numero (str): Número de telefone do usuário.
            plano (Plano): Plano do usuário.
        """
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def fazer_chamada(self, destinatario, duracao):
        """
        Realiza uma chamada para um destinatário com uma determinada duração.
        
        Args:
            destinatario (str): Número do destinatário.
            duracao (int): Duração da chamada em minutos.
        
        Returns:
            str: Mensagem indicando o sucesso ou falha da chamada.
        """
        custo = self.__plano.custo_chamada(duracao)
        saldo_atual = self.__plano.verificar_saldo()
        if saldo_atual >= custo:
            self.__plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_atual - custo:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

    def __str__(self):
        """
        Retorna uma mensagem indicando que o usuário foi criado com sucesso.
        
        Returns:
            str: Mensagem de sucesso.
        """
        return f"Usuário {self.__nome} criado com sucesso."


class UsuarioPrePago(UsuarioTelefone):
    """
    Classe para representar um usuário de telefone pré-pago.
    
    Herda de UsuarioTelefone e utiliza um Plano com saldo inicial.
    
    Métodos:
        __init__(nome, numero, saldo_inicial): Inicializa um novo objeto UsuarioPrePago.
    """
    
    def __init__(self, nome, numero, saldo_inicial):
        """
        Inicializa um novo objeto UsuarioPrePago.
        
        Args:
            nome (str): Nome do usuário.
            numero (str): Número de telefone do usuário.
            saldo_inicial (float): Saldo inicial do plano.
        """
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número de telefone: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Digite o número do destinatário: ")
duracao = int(input("Digite a duração da chamada em minutos: "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
