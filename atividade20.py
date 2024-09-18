# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.

# Inicializa a soma
soma = 0

# Loop de 1 a 100
for numero in range(1, 101):
    # Verifica se o número é par
    if numero % 2 == 0:
        soma += numero  # Adiciona o número par à soma

# Exibe o resultado
print("A soma dos números pares de 1 a 100 é:", soma)