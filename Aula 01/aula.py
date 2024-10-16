lista3 = ["C", 4.6, True, "true", "vamo aprender", ["outra", "lista", "interna"]]
print(lista3[-2:])
lista3.pop(3)
print(lista3)

a = [1,2,3]
b = a[:]
b[0] = 5
print(b)

uma_lista = [1,2,3,4]
uma_lista = uma_lista + ['gato', 'jonas', 'rafael']
print(uma_lista)