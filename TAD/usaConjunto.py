import Conjunto

# criando os objetos da classe Conjunto

conjunto1 = Conjunto.Conjunto()
conjunto2 = Conjunto.Conjunto()

# inserção dos valores nos conjuntos 

conjunto1.inserir(5)
conjunto1.inserir(7)
conjunto1.inserir(8)
conjunto2.inserir(5)
conjunto2.inserir(9)
conjunto2.inserir(0)

# remoção dos valores nos conjuntos

conjunto1.remover(7)
conjunto2.remover(0)

# apresentação dos conjuntos

print("Conjunto 1:")
conjunto1.show()
print("Conjunto 2:")
conjunto2.show()

# união dos conjuntos 

uniao = conjunto1.uniao(conjunto2)
print("União dos conjuntos:")
uniao.show()

# intersecão dos conjuntos

inter = conjunto1.interseccao(conjunto2)
print("Interseção dos conjuntos:")
inter.show()