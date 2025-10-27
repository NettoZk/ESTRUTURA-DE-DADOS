from fila_prioridade import FilaP

fila = FilaP()

fila.inserir("A", 1)
fila.inserir("B", 2)
fila.inserir("C", 3)
fila.inserir("D", 4)
fila.inserir("E", 1)

print("Filas após inserções:")
fila.show()

print("Primeiro da fila:", fila.ver_primeiro())

print("\nRemovendo elementos...")
print("Removido:", fila.remover())
print("Removido:", fila.remover())

print("\nFilas após duas remoções:")
fila.show()

fila.inserir("F", 2)
print("Após nova inserção:")
fila.show()

fila.inserir("A", 1)
print("Após nova inserção:")
fila.show()

print("\nEsvaziando a fila...")
while not fila.esta_vazia():
    print("Removido:", fila.remover())

print("Fila está vazia?", fila.esta_vazia())
