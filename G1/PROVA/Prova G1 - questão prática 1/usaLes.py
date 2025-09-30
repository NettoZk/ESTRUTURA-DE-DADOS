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

print('Lista após inserir no fim B C D E: espera-se A B C D E')
l.inserir_fim('B')
l.inserir_fim('C')
l.inserir_fim('D')
l.inserir_fim('E')
l.show()
print()

print('remover depois de B: espera-se A B')
l.remover_depois('B')
l.show()
print('ver quantidade:', l.ver_quantidade())
print()