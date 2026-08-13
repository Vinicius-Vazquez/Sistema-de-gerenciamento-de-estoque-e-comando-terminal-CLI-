class Produto:

    def __init__(self, id_Produto, nome, quantidade, preco):
        self.id = id_Produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def calcular_valor_total(self):
        return self.quantidade * self.preco

    def __str__(self):
        return f"[{self.id}] {self.nome} - Qtd: {self.quantidade} | R${self.preco:.2f}"


# Área deteste inicial
if __name__ == "__main__":
    print("\t\t\t===TESTANDO A CLASSE PRODUTO==")

    p1 = Produto(1, "Coca-Cola", 3000, 5.00)
    p2 = Produto(2, "Arroz", 300, 30.00)

    print(p1)
    print(p2)

    valor_p1 = p1.calcular_valor_total()
    print(f"Valor total investido em {p1.nome}: R$ {valor_p1:.2f}") 