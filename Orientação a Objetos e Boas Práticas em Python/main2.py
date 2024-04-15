class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    def verificar_saldo(self):
        if self.__saldo < 10:
            return self.__saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return self.__saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self.__saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        return self.plano.verificar_saldo()

    def mensagem_personalizada(self):
        _, mensagem = self.verificar_saldo()
        return mensagem


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
