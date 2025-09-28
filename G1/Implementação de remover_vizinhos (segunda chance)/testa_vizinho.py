import Ldde

l = Ldde.Ldde()

print('Tentando remover com a lista vazia:')
print(f"Foram removidos {l.remover_vizinhos('A')} nós vizinhos")
print('Lista:')
l.show()
print()

l.inserir_fim('A')

print('Tentando remover com a lista contendo somente um elemento:')
print(f"Foram removidos {l.remover_vizinhos('A')} nós vizinhos")
print('Lista:')
l.show()
print()

l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.inserir_fim('E')
l.inserir_fim('F')
l.inserir_fim('G')
l.inserir_fim('H')
l.inserir_fim('I')
l.inserir_fim('J')
l.inserir_fim('K')
l.inserir_fim('L')

print('Lista:')
l.show()          # ABCDEFGHIJKL
print()
print('Lista reverso:')
l.show_reverso()  # LKJIHGFEDCBA
print()

print("Vizinhos de 'F' (meio): remove 'E' e 'G'")
print(f"Foram removidos {l.remover_vizinhos('F')} nós vizinhos")
print('Lista:')
l.show()                    # ABCDFHIJKL
print()
print('Lista reverso:')
l.show_reverso()            # LKJIHFDCBA 
print()

print("Vizinhos de 'A' : remove apenas 'B'")
print(f"Foram removidos {l.remover_vizinhos('A')} nós vizinhos")
l.show()                    # ACDFHIJKL
print()
l.show_reverso()            # LKJIHFDCA
print()

print("Vizinhos de 'L' : remove apenas 'K'")
print(f"Foram removidos {l.remover_vizinhos('L')} nós vizinhos")
print('Lista:')
l.show()                    # ACDFHIJL
print()
print('Lista reverso:')
l.show_reverso()            # LJIHFDCA
print()

print("Vizinhos de 'C' : remove 'A' e 'D'")
print(f"Foram removidos {l.remover_vizinhos('C')} nós vizinhos")
print('Lista:')
l.show()                    # CFHIJL
print()
print('Lista reverso:')
l.show_reverso()            # LJIHFC
print()

print("Inserindo 'A' no início")
l.inserir_inicio('A')
print('Lista:')
l.show()                    # ACFHIJL
print()
print('Lista reverso:')
l.show_reverso()            # LJIHFCA
print()

print("Vizinhos de 'J' : remove 'I' e 'L'")
print(f"Foram removidos {l.remover_vizinhos('J')} nós vizinhos")
print('Lista:')
l.show()                    # ACFHJ
print()
print('Lista reverso:')
l.show_reverso()            # JHFCA
print()

print("Insrindo 'L' no fim")
l.inserir_fim('L')
print('Lista:')
l.show()                    # ACFHJL
print()
print('Lista reverso:')
l.show_reverso()            # LJHFCA
print()

print("Valor inexistente 'X' (não altera)")
print(f"Foram removidos {l.remover_vizinhos('X')} nós vizinhos")
print('Lista:')
l.show()                    # ACFHJL
print()
print('Lista reverso:')
l.show_reverso()            # LJHFCA
print()
