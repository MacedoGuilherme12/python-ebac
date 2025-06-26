def numeros_menu():
    try:
        primeiro_numero = int(input("Insira o primeiro número:"))
    except ValueError:
        print("Valor invalido!!")
        return
    try:
        segundo_numero = int(input("Insira o segundo numero:"))
    except ValueError:
        print("Valor invalido!!")
        return
    return(primeiro_numero, segundo_numero)

def principal_menu():
    menu_opcoes = ["Soma","Subtração","Multiplicação","Divisão"]
    menu = [f" {i + 1} - {op}" for i, op in enumerate(menu_opcoes)]
    for i in menu:
        print(i)
   
    

    
def main():
    
    while True:
        principal_menu()
        operacao = {
            1 : lambda x,y : x + y,
            2 : lambda x,y : x - y,
            3 : lambda x,y : x * y,
            4 : lambda x,y : x / y 
        }
        try:
            opcao = int(input("Qual opção deseja?"))
            
            print("---")
            numeros = list(numeros_menu())   


            if opcao == 4 and numeros[1] == 0:
                while numeros[1] == 0:
                    try:
                        numeros[1] = int(input("Divisão por zero não é permitida. Insira outro número: "))
                    except ValueError:
                        print("Valor inválido!")
        
            resultado = operacao[opcao](*numeros)
            print(f"Resultado: {resultado}")
            continuar = input("Deseja continuar? (s/n)")
            if continuar.lower() != "s":
                return
        except ValueError:
            print("Valor invalido!!")

        
main()