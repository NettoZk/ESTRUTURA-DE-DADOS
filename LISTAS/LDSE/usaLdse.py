import Ldse

l = Ldse.Ldse()

l.inserir_inicio('A')
l.inserir_inicio('B')
l.inserir_inicio('C')
l.remover_inicio()
l.show()
l.inserir_inicio('D')
l.show()
l.inserir_inicio('D')
l.show()
l.remover_irmaos('B')
l.show()