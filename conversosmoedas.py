from abc import ABC, abstractmethod

class ConversorMoeda(ABC):
    """
    Classe base abstrata para conversores de moeda.
    Utiliza encapsulamento para proteger atributos sensíveis.
    """
    def __init__(self, taxa_cambio):
        self._taxa_cambio = taxa_cambio  # Atributo encapsulado (protegido)

    @abstractmethod
    def converter(self, valor):
        """Método abstrato para conversão de moeda."""
        pass

    # Getter para a taxa de câmbio
    @property
    def taxa_cambio(self):
        return self._taxa_cambio

    # Setter para a taxa de câmbio
    @taxa_cambio.setter
    def taxa_cambio(self, nova_taxa):
        if isinstance(nova_taxa, (int, float)) and nova_taxa > 0:
            self._taxa_cambio = nova_taxa
        else:
            raise ValueError("A taxa de câmbio deve ser um valor numérico positivo.")


class ConversorDolarParaReal(ConversorMoeda):
    """Classe que converte de Dólar para Real."""
    def converter(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser convertido deve ser positivo.")
        return valor * self._taxa_cambio


class ConversorEuroParaReal(ConversorMoeda):
    """Classe que converte de Euro para Real."""
    def converter(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser convertido deve ser positivo.")
        return valor * self._taxa_cambio


# Exemplo de polimorfismo
def realizar_conversao(conversor, valor):
    """Função que demonstra polimorfismo ao aceitar diferentes tipos de conversores."""
    print(f"Valor convertido: {conversor.converter(valor):.2f}")


# Testando o código
if __name__ == "__main__":
    conversor_dolar = ConversorDolarParaReal(5.25)  # 1 USD = 5.25 BRL
    conversor_euro = ConversorEuroParaReal(6.18)   # 1 EUR = 6.18 BRL

    # Realizando conversões
    realizar_conversao(conversor_dolar, 100)  # Convertendo 100 USD para BRL
    realizar_conversao(conversor_euro, 50)   # Convertendo 50 EUR para BRL

    # Alterando a taxa de câmbio usando encapsulamento
    conversor_dolar.taxa_cambio = 5.30
    realizar_conversao(conversor_dolar, 100)

    # Demonstrando encapsulamento com valores inválidos
    try:
        conversor_dolar.taxa_cambio = -1
    except ValueError as e:
        print(f"Erro ao atualizar a taxa de câmbio: {e}")

    try:
        realizar_conversao(conversor_euro, -20)
    except ValueError as e:
        print(f"Erro ao realizar a conversão: {e}")