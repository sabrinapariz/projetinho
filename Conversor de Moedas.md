Conversor de Moedas

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
