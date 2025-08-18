# Exemplos de uso do range em um laço for

# 1) Usando apenas 1 argumento → range(fim)
# Vai de 0 até (fim - 1)
print("Exemplo 1: range(5)")
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4
print()


# 2) Usando 2 argumentos → range(início, fim)
# Vai de 'início' até (fim - 1), passo padrão é +1
print("Exemplo 2: range(2, 6)")
for i in range(2, 6):
    print(i)
# Saída: 2, 3, 4, 5
print()


# 3) Usando 3 argumentos → range(início, fim, passo)
# Aqui controlamos o incremento manualmente
print("Exemplo 3: range(0, 10, 2)")
for i in range(0, 10, 2):
    print(i)
# Saída: 0, 2, 4, 6, 8
print()


# 4) Usando passo negativo → range(início, fim, -1)
# Contagem decrescente
print("Exemplo 4: range(5, 2, -1)")
for i in range(5, 2, -1):
    print(i)
# Saída: 5, 4, 3
print()


# 5) Caso inválido (sequência vazia)
# Se o passo for positivo, início >= fim gera nada
print("Exemplo 5 (inválido): range(5, 2)")
for i in range(5, 2):
    print(i)
# Saída: (nada, pois a sequência é vazia)
print()


# 6) Caso válido equivalente ao Exemplo 5, mas com passo negativo
# Agora funciona porque o passo é compatível com início > fim
print("Exemplo 6 (válido): range(5, 2, -1)")
for i in range(5, 2, -1):
    print(i)
# Saída: 5, 4, 3

# A função range pode receber até 3 argumentos: range(início, fim, passo)

# - Se for usado apenas 1 argumento: range(fim)
#   Começa do 0 e vai até (fim - 1)
#   Ex.: range(5) → [0, 1, 2, 3, 4]

# - Se forem usados 2 argumentos: range(início, fim)
#   Começa em 'início' e vai até (fim - 1), com passo padrão +1
#   Ex.: range(2, 6) → [2, 3, 4, 5]

# - Se forem usados 3 argumentos: range(início, fim, passo)
#   Vai de 'início' até (fim - 1), pulando de 'passo' em 'passo'
#   O passo pode ser positivo ou negativo
#   Ex.: range(5, 2, -1) → [5, 4, 3]

# Observação:
# - Se 'passo' for positivo, o 'início' deve ser menor que o 'fim', senão gera sequência vazia
# - Se 'passo' for negativo, o 'início' deve ser maior que o 'fim', senão gera sequência vazia


# =========================
# Exemplos práticos em tabela
# =========================

print("-" * 45)
print(f"{'range(...)':<20} | {'Saída':<20}")
print("-" * 45)

print(f"{'range(5)':<20} | {list(range(5))}")
print(f"{'range(2, 6)':<20} | {list(range(2, 6))}")
print(f"{'range(0, 10, 2)':<20} | {list(range(0, 10, 2))}")
print(f"{'range(5, 2, -1)':<20} | {list(range(5, 2, -1))}")
print(f"{'range(5, 2)':<20} | {list(range(5, 2))}")  # vazio

print("-" * 45)

