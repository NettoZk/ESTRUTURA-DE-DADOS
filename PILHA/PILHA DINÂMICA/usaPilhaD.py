import PilhaD

pilha = PilhaD.PilhaD() 


print("=== Teste inicial ===")
print("A pilha está vazia?", pilha.esta_vazia())

# Inserindo elementos
print("\n=== Inserindo elementos ===")
pilha.push(10)
pilha.push(20)
pilha.push(30)
print("Pilha atual:")
pilha.show()
print("Topo da pilha:", pilha.ver_topo())
print("A pilha está vazia?", pilha.esta_vazia())

# Removendo elementos
print("\n=== Removendo elementos ===")
pilha.pop()
print("Pilha após 1 pop:")
pilha.show()
print("Topo da pilha:", pilha.ver_topo())

pilha.pop()
print("Pilha após 2 pops:")
pilha.show()
print("Topo da pilha:", pilha.ver_topo())

# Removendo o último elemento
pilha.pop()
print("Pilha após 3 pops (deve ficar vazia):")
pilha.show()
print("A pilha está vazia?", pilha.esta_vazia())

# Teste pop em pilha vazia (não deve quebrar)
print("\n=== Tentando pop em pilha vazia ===")
pilha.pop()
print("Pilha após tentar pop em vazia:")
pilha.show()
