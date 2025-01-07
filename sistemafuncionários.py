from abc import ABC, abstractmethod

class Funcionario:
    """
    Classe base para representar um Funcionário.
    Utiliza encapsulamento para proteger atributos sensíveis.
    """
    def __init__(self, nome, salario):
        self._nome = nome  # Atributo encapsulado (protegido)
        self._salario = salario  # Atributo encapsulado (protegido)

    def exibir_informacoes(self):
        """Método que será sobrescrito pelas classes filhas."""
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

    # Getter para o nome
    @property
    def nome(self):
        return self._nome

    # Setter para o nome
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    # Getter para o salário
    @property
    def salario(self):
        return self._salario

    # Setter para o salário
    @salario.setter
    def salario(self, novo_salario):
        if isinstance(novo_salario, (int, float)) and novo_salario > 0:
            self._salario = novo_salario
        else:
            raise ValueError("O salário deve ser um valor numérico positivo.")


class Gerente(Funcionario):
    """Classe derivada que representa um Gerente."""
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self._departamento = departamento  # Atributo adicional

    def exibir_informacoes(self):
        return f"Gerente: {self._nome}, Salário: {self._salario}, Departamento: {self._departamento}"


class Desenvolvedor(Funcionario):
    """Classe derivada que representa um Desenvolvedor."""
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self._linguagem = linguagem  # Atributo adicional

    def exibir_informacoes(self):
        return f"Desenvolvedor: {self._nome}, Salário: {self._salario}, Linguagem: {self._linguagem}"


# Exemplo de polimorfismo
def exibir_detalhes(funcionario):
    """Função que demonstra polimorfismo ao aceitar diferentes tipos de Funcionários."""
    print(funcionario.exibir_informacoes())


# Testando o código
if __name__ == "__main__":
    gerente = Gerente("Ana", 15000, "Vendas")
    desenvolvedor = Desenvolvedor("Carlos", 8000, "Python")

    # Alterando valores usando encapsulamento
    gerente.salario = 16000
    desenvolvedor.nome = "Carlos Silva"

    # Exibindo detalhes
    exibir_detalhes(gerente)
    exibir_detalhes(desenvolvedor)

    # Demonstrando encapsulamento com valores inválidos
    try:
        gerente.salario = -5000
    except ValueError as e:
        print(f"Erro ao atualizar o salário: {e}")

    try:
        desenvolvedor.nome = ""
    except ValueError as e:
        print(f"Erro ao atualizar o nome: {e}")