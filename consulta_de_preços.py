print("Codigos de produtos:")
print("1 - café")
print("2 - chá")
print("3 - suco")
print("4 - refrigerantes")
print("5 - água")
print("0 - SAIR")

# solicita o codigo do produto para o usuario
codigo = int(input("digite o codigo do produto "))

# usa matc-case para mostrar o preço com base no codigo 
match codigo:
    case 1:
        print("produtos: café - preço: R$ 4,50")
    case 2:
        print("produtos: chá - preço: R$ 3,00")
    case 3:
        print("produtos: suco - preço: R$ 5,00")
    case 4:
        print("produtos: refrigerantes - preço: R$ 6,00")
    case 5:
        print("produtos: água - preço: R$ 2,00")
    case 6:
        print("saindo do programa...")
        exit() # encerra o programa se o codigo for 0
    case _:
        print("codigo invalido. Por favor, tente novamente")