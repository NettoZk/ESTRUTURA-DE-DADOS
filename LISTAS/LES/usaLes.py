import Les

l = Les.Les(5)

'''
print('Lista sem nenhum valor: espera-se lista vazia')
l.show()
print(l.vetor)
print()

print('Lista após inserir no fim A: espera-se A')
l.inserir_fim('A')
l.show()
print()

print('Lista após inserir no fim B C D: espera-se A B C D')
l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.show()
print()

print('Lista após remover fim: ')
l.remover_fim()
l.show()
print()

print('Lista após inserir no fim E: espera-se A B C E ')
l.inserir_fim('E')
l.show()
print()

print('Lista após inserir no início F: espera-se F A B C E')
l.inserir_inicio('F')
l.show()
print()

print('Lista após inserir no início G: espera-se alerta de lista cheia')
l.inserir_inicio('G')
print()

print('Lista após remover início: espera-se A B C E')
l.remover_inicio()
l.show()
print()

'''

l.inserir_inicio('A')
l.inserir_inicio('B')
l.inserir_inicio('B')
l.inserir_inicio('C')
print('Espera-se: C B B A')
l.show()
print()

print('Remover "D", espera-se: C B B A')
l.remover('D')
l.show()
print()

print('Remover "A", espera-se: C B B')
l.remover('A')
l.show()
print()

print('Remover "F", espera-se: C B B')
if l.removerTF('F'):
    print('F foi removido da lista')
else:
    print('F não foi encontrado na lista')
l.show()
print()

print('Remover "C", espera-se: B B')
if l.removerTF('C'):
    print('C foi removido da lista')
else:
    print('C não estava na lista')
l.show()
print()

print('inserindo fim "B D B", espera-se: B B B D B')
l.inserir_fim('B')
l.inserir_fim('D')
l.inserir_fim('B')
l.show()
print()

print('A letra "B" foi removida ', l.remover_contar('B'), ' vezes')
l.show()
print()

print('Lista de vetores para verificação:')
print(l.vetor)