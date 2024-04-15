# Desafio de Programação: Classe de Usuário de Telefone

## Desafio 1: Criando a Classe UsuarioTelefone

Vamos criar uma classe chamada `UsuarioTelefone` para representar um usuário de telefone. Esta classe terá os seguintes atributos:

- Nome do usuário
- Número de telefone
- Plano (Plano Essencial Fibra, Plano Prata Fibra, Plano Premium Fibra)

### Entrada
- Nome do usuário
- Número de telefone
- Plano

### Saída
Mensagem indicando que o usuário foi criado com sucesso.

#### Exemplos:

- **Entrada**: 
  - Nome: Ana
  - Número: (11) 91111-1111
  - Plano: Plano Essencial Fibra
- **Saída**: 
  - Usuário Ana criado com sucesso.

## Desafio 2: Adicionando Funcionalidades ao Plano

Agora, vamos adicionar uma funcionalidade à classe `UsuarioTelefone` para verificar o saldo disponível em seu plano. Para isso, criaremos uma classe `PlanoTelefone` com os seguintes atributos:

- Nome do usuário
- Saldo

E os seguintes métodos:

- `verificar_saldo()`: Verifica o saldo do plano e retorna uma mensagem personalizada.
- `mensagem_personalizada()`: Gera uma mensagem personalizada com base no saldo.

### Condições da verificação do saldo:

- Saldo < 10: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Saldo >= 50: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

### Entrada
- Nome do usuário
- Plano (Essencial, Prata, Premium)
- Saldo atual do cliente

### Saída
Mensagem personalizada de acordo com o saldo do cliente.

#### Exemplos:

- **Entrada**: 
  - Nome: João
  - Plano: Essencial
  - Saldo: 9
- **Saída**: 
  - Seu saldo está baixo. Recarregue e use os serviços do seu plano.

## Desafio 3: Realizando Chamadas

Adicionaremos uma funcionalidade à classe `UsuarioTelefone` para realizar chamadas para outros usuários. O custo da chamada será deduzido do saldo do usuário, com um custo de $0.10 por minuto.

### Métodos:

- `fazer_chamada(destinatario, duracao)`: Realiza a chamada e deduz o custo do saldo.
- `custo_chamada(duracao)`: Calcula o custo da chamada com base na duração.
- `deduzir_saldo(valor)`: Deduz o valor do saldo do plano.

### Entrada
- Número do usuário
- Número do telefone
- Saldo inicial
- Número do destinatário
- Duração da chamada em minutos

### Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

#### Exemplos:

- **Entrada**: 
  - Número: Rodrigo (00) 90000-0000
  - Saldo inicial: 10.00
  - Destinatário: (33) 93333-3333
  - Duração: 60 minutos
- **Saída**: 
  - Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00

---

Espero que este README.md ajude a entender o desafio e a implementação proposta. Divirta-se codificando!
