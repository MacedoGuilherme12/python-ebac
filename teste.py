def exibe_menu():
    print("Menu:")
    print("1 - Adicione Produto")
    print("2 - Listar Produtos")
    print("3 - Remover Produto")
    print("4 - Atualizar quantidade do produto")
    print("5 - Sair")
    opcao = int(input("Qual sua escolha: "))
    return opcao

def adicionar_produto(produto, quantidade, produtos, preco):
    produtos[produto] = {
        "Quantidade" : quantidade,
        "Preço" : preco
    }
def listar_produtos(produtos):
    if(len(produtos) == 0):
        print("Estoque facil")
        return
    for produto in produtos:
        print(f"Produto: {produto} Quantidade: {produtos[produto]["Quantidade"]} Preço: {produtos[produto]["Preço"]}  ")

def remover_produto(produto, produtos):
    encontrado = False
    for produtoo in list(produtos.keys()):
        if produtoo.lower() == produto.lower():
            produtos.pop(produtoo)
            print(f"Produto removido: {produtoo}")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")
def produto_quantidade(produtos, atual_produto, quantidade):
    for produto in list(produtos.keys()):
        if produto.lower() == atual_produto.lower():
            print(f"Alterado quantidade do produto: {produto} de {produtos[produto]['Quantidade']} para {quantidade}")
            produtos[produto]["Quantidade"] = quantidade
            return
    print("Esse produto não existe!!")
    
def main():
    produtos = {}
    condicao = True
    while condicao:
        opcao = exibe_menu()
        print("--")
        match opcao:
            case 1:
                produto = input("Qual Produto deseja adicionar? ")
                quantidade = int(input("Qual a quantidade? "))
                preco = int(input("Qual o preço? "))

                adicionar_produto(produto, quantidade, produtos, preco)
                print("--")
            case 2 :
                listar_produtos(produtos)
                print("--")
            case 3:
                produto = input("Qual produto deseja excluir? ").lower()
                remover_produto(produto, produtos)
                print("--")
            case 4:
                atual_produto = input("Qual produto deseja mudar a quantidade? ").lower()
                quantidade = int(input("Qual nova quantidade? "))
                produto_quantidade(produtos, atual_produto, quantidade)
            case 5:
                condicao = False
main()
    