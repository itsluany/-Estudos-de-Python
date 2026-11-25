nome = "lUaNy"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "     Olá mundo!       " 

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))

nome = "MARIA"
idade = 45
profissao = "programadora"
linguagem = "Python"
saldo = 54.608

dados = {"nome": "MARIA", "idade": 45}

# 1. Formatação antiga (%)
print("Nome: %s Idade: %d" % (nome, idade))

# 2. Método format() com parênteses vazios
print("Nome: {} Idade: {}".format(nome, idade))

# 3. Método format() com índices
print("Nome: {1} Idade: {0}".format(idade, nome))

# 4. Método format() com índices repetidos
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# 5. Método format() com parâmetros nomeados
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

# 6. Método format() com nomes diferentes
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

# 7. Desempacotamento de dicionário
print("Nome: {nome} Idade: {idade}".format(**dados))

# 8. F-strings
print(f"Nome: {nome} Idade: {idade}")

# 9. F-string com saldo
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")