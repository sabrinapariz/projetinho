# projetinho
código em phyton

# Sistema de Funcionários

Visão Geral

Este projeto implementa um sistema de gerenciamento de funcionários utilizando os princípios de herança, polimorfismo e encapsulamento em Python. Ele simula diferentes tipos de funcionários (Gerentes e Assistentes), permitindo cálculos de salários com base em suas respectivas regras de pagamento.

Funcionalidades

Gerenciamento de Funcionários: Permite criar diferentes tipos de funcionários com atributos e comportamentos específicos.

Cálculo de Salários: Cada tipo de funcionário possui uma regra específica para cálculo do salário (ex.: bônus adicional para gerentes).
Encapsulamento: Informações sensíveis, como nome e salário, são protegidas e acessíveis apenas através de métodos.
Polimorfismo: A classe base Funcionario é extendida por outras classes que implementam comportamentos específicos.

Tecnologias

Python 3.10+
Biblioteca abc (Abstract Base Class) para criação de classes abstratas.

Estrutura de Classes

Diagrama UML:

# +-------------------------------+
# |    Funcionario                |
# +-------------------------------+
# | - _nome: str                  |
# | - _salario: float             |
# +-------------------------------+
# | + calcular_pagamento(): float |
# | + nome: str                   |
# | + salario: float              |
# +-------------------------------+
#         /\
#         ||
# +--------------------------------+ +--------------------------------+
# |      Gerente                   |  |     Assistente                |
# +--------------------------------+ +--------------------------------+
# | + calcular_pagamento(): float  | | + calcular_pagamento(): float  |
# +--------------------------------+ +--------------------------------+

Como Usar

Clone ou baixe este repositório.
Execute o arquivo sistema_funcionarios.py no terminal do VS Code ou qualquer ambiente Python:
python sistema_funcionarios.py
Altere os valores ou crie novos funcionários conforme necessário no próprio código.

Exemplo de Saída

Funcionário: Ana
Cargo: Gerente
Salário base: 10000.00
Pagamento total: 12000.00

Funcionário: Carlos
Cargo: Assistente
Salário base: 5000.00
Pagamento total: 5000.00


# Conversor de Moedas

Visão Geral

Este projeto é uma implementação de um conversor de moedas utilizando os princípios de herança, polimorfismo e encapsulamento em Python. Ele permite realizar a conversão de valores entre diferentes moedas (Dólar para Real e Euro para Real) e demonstra boas práticas de programação orientada a objetos.

Funcionalidades

Conversão de Dólar para Real: Utiliza uma taxa de câmbio configurável.

Conversão de Euro para Real: Similarmente, a taxa de câmbio pode ser alterada.

Validação: Garante que os valores a serem convertidos e as taxas de câmbio sejam positivos.

Encapsulamento: Atributos sensíveis são protegidos e acessíveis apenas através de métodos específicos.

Polimorfismo: Função genérica aceita diferentes tipos de conversores.

Tecnologias

Python 3.10+

Biblioteca abc (Abstract Base Class) para criação de classes abstratas.

Estrutura de Classes

# Diagrama UML:
# +-------------------------+
# |     ConversorMoeda      |
# +-------------------------+
# | - _taxa_cambio: float   |
# +-------------------------+
# | + converter(valor): float |
# | + taxa_cambio: float     |
# +-------------------------+
#           /\
#           ||
# +-------------------------+       +--------------------------+
# | ConversorDolarParaReal  |       |  ConversorEuroParaReal   |
# +-------------------------+       +--------------------------+
# | + converter(valor): float |     | + converter(valor): float |
# +-------------------------+       +--------------------------+

Como Usar

Clone ou baixe este repositório.

Execute o arquivo conversor_moedas.py no terminal do VS Code ou qualquer ambiente Python:

python conversor_moedas.py

Altere os valores ou taxas de câmbio conforme necessário no próprio código.

Exemplo de Saída

Valor convertido: 525.00
Valor convertido: 309.00
Valor convertido: 530.00
Erro ao atualizar a taxa de câmbio: A taxa de câmbio deve ser um valor numérico positivo.
Erro ao realizar a conversão: O valor a ser convertido deve ser positivo.
