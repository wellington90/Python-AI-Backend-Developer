class UsuarioTelefone:
    """
    Classe para representar um usuário de telefone.
    
    Atributos:
        nome (str): Nome do usuário.
        numero (str): Número de telefone do usuário.
        plano (str): Plano do usuário (Plano Essencial Fibra, Plano Prata Fibra, Plano Premium Fibra).
    
    Métodos:
        nome (property): Retorna o nome do usuário.
        numero (property): Retorna o número de telefone do usuário.
        plano (property): Retorna o plano do usuário.
        __str__(): Retorna uma mensagem indicando que o usuário foi criado com sucesso.
    """
    
    def __init__(self, nome, numero, plano):
        """
        Inicializa um novo objeto UsuarioTelefone.
        
        Args:
            nome (str): Nome do usuário.
            numero (str): Número de telefone do usuário.
            plano (str): Plano do usuário.
        """
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        """
        Retorna o nome do usuário.
        
        Returns:
            str: Nome do usuário.
        """
        return self.__nome

    @property
    def numero(self):
        """
        Retorna o número de telefone do usuário.
        
        Returns:
            str: Número de telefone do usuário.
        """
        return self.__numero

    @property
    def plano(self):
        """
        Retorna o plano do usuário.
        
        Returns:
            str: Plano do usuário.
        """
        return self.__plano

    def __str__(self):
        """
        Retorna uma mensagem indicando que o usuário foi criado com sucesso.
        
        Returns:
            str: Mensagem de sucesso.
        """
        return f"Usuário {self.nome} criado com sucesso."

# Entrada dos dados do usuário
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número de telefone: ")
plano = input("Digite o plano (Plano Essencial Fibra, Plano Prata Fibra, Plano Premium Fibra): ")

# Criação do objeto UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)

# Imprime a mensagem de sucesso
print(usuario)
