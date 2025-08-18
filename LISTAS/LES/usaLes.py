import Les

l = Les.Les(5)

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
