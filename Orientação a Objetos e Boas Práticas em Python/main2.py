class PlanoTelefone:
    """
    Classe para representar um plano de telefone.
    
    Atributos:
        nome (str): Nome do plano.
        saldo (float): Saldo disponível no plano.
    
    Métodos:
        nome (property): Retorna o nome do plano.
        saldo (property): Retorna o saldo do plano.
        verificar_saldo(): Verifica o saldo do plano e retorna uma mensagem personalizada.
    """
    
    def __init__(self, nome, saldo):
        """
        Inicializa um novo objeto PlanoTelefone.
        
        Args:
            nome (str): Nome do plano.
            saldo (float): Saldo inicial do plano.
        """
        self.__nome = nome
        self.__saldo = saldo

    @property
    def nome(self):
        """
        Retorna o nome do plano.
        
        Returns:
            str: Nome do plano.
        """
        return self.__nome

    @property
    def saldo(self):
        """
        Retorna o saldo do plano.
        
        Returns:
            float: Saldo do plano.
        """
        return self.__saldo

    def verificar_saldo(self):
        """
        Verifica o saldo do plano e retorna uma mensagem personalizada.
        
        Returns:
            tuple: (saldo, mensagem)
                saldo (float): Saldo do plano.
                mensagem (str): Mensagem personalizada de acordo com o saldo.
        """
        if self.__saldo < 10:
            return self.__saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return self.__saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self.__saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


class UsuarioTelefone:
    """
    Classe para representar um usuário de telefone.
    
    Atributos:
        nome (str): Nome do usuário.
        plano (PlanoTelefone): Plano do usuário.
    
    Métodos:
        verificar_saldo(): Verifica o saldo do plano do usuário.
        mensagem_personalizada(): Retorna uma mensagem personalizada baseada no saldo do usuário.
    """
    
    def __init__(self, nome, plano):
        """
        Inicializa um novo objeto UsuarioTelefone.
        
        Args:
            nome (str): Nome do usuário.
            plano (PlanoTelefone): Plano do usuário.
        """
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        """
        Verifica o saldo do plano do usuário.
        
        Returns:
            tuple: (saldo, mensagem)
                saldo (float): Saldo do plano do usuário.
                mensagem (str): Mensagem personalizada baseada no saldo.
        """
        return self.plano.verificar_saldo()

    def mensagem_personalizada(self):
        """
        Retorna uma mensagem personalizada baseada no saldo do usuário.
        
        Returns:
            str: Mensagem personalizada.
        """
        _, mensagem = self.verificar_saldo()
        return mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("Digite o nome do usuário: ")
nome_plano = input("Digite o nome do plano (Plano Essencial Fibra, Plano Prata Fibra, Plano Premium Fibra): ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo e imprimir a mensagem:
print(usuario.mensagem_personalizada())
