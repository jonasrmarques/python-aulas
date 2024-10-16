dic = {} # dicionário vazio!

print(type(dic)) # <class 'dict'>

dic_tupla = {'tupla': ('aqui não muda')}

dic_times = {'sport': 49, 'santa': 21}
print(dic_times)

#criar valores e atualiza valores
dic_times['nautico'] = 19
print(dic_times)

#Buscar valores
qtd_titulos = dic_times.get('sport') #Primeira forma
print(qtd_titulos)

print(dic_times['santa']) #Segunda forma

print(dic_times.keys())
print(dic_times.values())

teste1 = list(dic_times.keys())
teste2 = list(dic_times.values())
print(teste1[0])
print(teste2[0])

#alterar valores

aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Engenharia",
    "notas": [9.0, 8.5, 7.2]
}

del aluno['notas']
print(aluno)

aluno["faculdade"] = "UFPE"
print(aluno)

aluno["idade"] = 33
print(aluno)

exemplo = aluno.items()
print(list)