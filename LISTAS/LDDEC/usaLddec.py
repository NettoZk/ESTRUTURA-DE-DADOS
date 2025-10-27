from Lddec import Lddec

lista = Lddec()

print("\n===== TESTES DA FUNÇÃO remover_todos_apos =====")

print()
lista.inserir_fim("A")
lista.inserir_fim("B")
lista.inserir_fim("C")
lista.inserir_fim("D")
lista.inserir_fim("E")
print("Lista atual:")
lista.show()
print("Quantidade:", lista.quant)

print("\nRemovendo todos os elementos após 'C'")
lista.remover_todos_apos("C")
print("Lista após remover todos após 'C':")
lista.show()
print("Quantidade:", lista.quant)

print("\nRemovendo todos os elementos após 'E' (que não está mais na lista)")
lista.remover_todos_apos("E")
print("Lista após tentativa de remoção com valor inexistente:")
lista.show()
print("Quantidade:", lista.quant)

print("\nRemovendo todos os elementos após 'A'")
lista.remover_todos_apos("A")
print("Lista após remover todos após 'A':")
lista.show()
print("Quantidade:", lista.quant)

print("\nTentando remover após o único elemento restante")
lista.remover_todos_apos("A")
print("Lista final:")
lista.show()
print("Quantidade:", lista.quant)
