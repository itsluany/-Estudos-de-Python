#texto = input("inform um texto: ")
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adicione uma quebra de linha
    
for numero in range(0, 51, 5):
    print(numero)