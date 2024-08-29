n1 = int(input('Digite um valor: '))
#Para saber o tipo de Váriavel -> print(type(n1))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
print('A soma entre', n1, 'e', n2, 'vale', soma) #Formato do Python 2
# Forma de resumir o print sem ficar abrindo e fechando aspas. Formato do Python 3.
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
#Outra forma de print no Python 3 é o ->
print(f'A soma entre {n1} e {n2} vale {soma}')