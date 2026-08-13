class Produto:
    """Classe que representa um produto individual dentro do sistema."""

    # Inicializa os atributos fundamentais do produto
    def __init__(self, id_Produto, nome, quantidade, preco):
        self.id = id_Produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    # Multiplica a quantidade em estoque pelo valor unitário
    def calcular_valor_total(self):
        return self.quantidade * self.preco

    # Retorna o produto formatado como texto legível no terminal
    def __str__(self):
        return f"[{self.id}] {self.nome} - Qtd: {self.quantidade} | R${self.preco:.2f}"


class Estoque:
    """Classe responsável por gerenciar a coleção de produtos."""

    # Inicializa o estoque com uma lista vazia de produtos
    def __init__(self):
        self.produtos = []

    # Adiciona um objeto Produto à lista
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"-> Produto '{produto.nome}' adicionado com sucesso!")

    # Verifica se há produtos cadastrados
    def listar_produtos(self):
        print("\n\t\t\t== RELATÓRIO DE ESTOQUE ==")
        if not self.produtos:
            return print("Estoque vázio!")

        print("\n" + "=" * 40)
        print("         PRODUTOS EM ESTOQUE")
        print("=" * 40)

        # Exibe cada produto individualmente chamando o método __str__
        for p in self.produtos:
            print(p)
        print("=" * 40 + "\n")

    # Percorre a lista de produtos procurando pelo ID informado
    def buscar_id(self, id_Produto):
        for p in self.produtos:
            if p.id == id_Produto:
                return p
            return None

    # Tenta localizar o produto antes de remover
    def remover_produto(self, id_Produto):
        produto = self.buscar_id(id_Produto)
        if produto:
            self.produtos.remove(produto)
            print(f"Produto '{produto.nome}' (ID: {id_Produto}) removido com sucesso!")
        else:
            print(f"Erro: Produto com ID {id_Produto} não foi encontrado.")



# Área deteste inicial
if __name__ == "__main__":
    print("\t\t\t===TESTANDO A CLASSE PRODUTO==")

    # 1. Instanciando o objeto de estoque principal
    meu_estoque = Estoque()

    # 2. Criando instâncias de produtos individuais
    p1 = Produto(1, "Coca-Cola", 15000, 5.00)
    p2 = Produto(2, "Arroz", 300, 30.00)

    # 3. Adicionando os produtos cadastrados ao estoque
    meu_estoque.adicionar_produto(p1)
    meu_estoque.adicionar_produto(p2)

    # 4. Listando os itens iniciais cadastrados
    meu_estoque.listar_produtos()

    # 5. Executando teste de busca por ID existente
    print("\n\t\t\t===TESTANDO BUSCA===")
    item_buscado = meu_estoque.buscar_id(1)
    if item_buscado:
        print(f"Item encontrado na busca: {item_buscado.nome}")
    else:
        print("Item não encontrado.")

    # 6. Testando a remoção
    print("\n--- Testando Remoção ---")
    meu_estoque.remover_produto(2)  # Remove o Arroz

    # 7. Listando novamente para confirmar a remoção
    meu_estoque.listar_produtos()