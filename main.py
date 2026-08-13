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


class Estoque:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"-> Produto '{produto.nome}' adicionado com sucesso!")

    def listar_produtos(self):
        print("\n\t\t\t== RELATÓRIO DE ESTOQUE ==")
        if not self.produtos:
            return print("Estoque vázio!")

        for p in self.produtos:
            print(p)



# Área deteste inicial
if __name__ == "__main__":
    print("\t\t\t===TESTANDO A CLASSE PRODUTO==")

    meu_estoque = Estoque()

    p1 = Produto(1, "Coca-Cola", 0, 5.00)
    p2 = Produto(2, "Arroz", 0, 30.00)

    meu_estoque.adicionar_produto(p1)
    meu_estoque.adicionar_produto(p2)

    meu_estoque.listar_produtos()