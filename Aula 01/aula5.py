# lista = []

# while True:
#     adicionar = input('Adicionar a lista? "1": Adicionar, "2": Remover, "3": Exibir ou se deseja se deseja sair, digite: "4"')
#     if adicionar == "4":
#         break
#     elif adicionar == "1":
#         adicionarElemento = input("O que você deseja adicionar?")
#         lista.append(adicionarElemento)
#     elif adicionar == "2":
#         removerElemento = input("Qual elemento você deseja remover?")
#         lista.remove(removerElemento)
#     elif adicionar == "3":
#         print(lista)
#         break
    

# print("Encerramos por aqui")

#Funções

#Cria uma função para retornar e exibir a soma de numeros pares usando while



def soma_numeros_pares(*args):
    soma = 0
    i = 0
    while i < len(args):
        if args[i] % 2 == 0:
            soma += args[i]
        i+=1
    print(f"A soma dos números pares é: {soma}")

soma_numeros_pares(1, 2, 3, 4, 5, 6, 7)
