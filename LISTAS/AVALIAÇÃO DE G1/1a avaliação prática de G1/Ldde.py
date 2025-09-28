class No:
    def __init__(self, ant, info, prox):
        self.ant  = ant
        self.info = info
        self.prox = prox


class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    # ---------------- inserções ----------------
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    # --------------- remoção por intervalo ---------------
    def remover_vizinhos(self, valor):
        """
        Remove o nó anterior e o nó posterior ao nó que contém 'valor'.
        - Se 'valor' estiver no início, remove apenas o posterior.
        - Se 'valor' estiver no fim, remove apenas o anterior.
        - Se 'valor' não for encontrado, não faz nada.

        Remove o nó ANTERIOR e o nó POSTERIOR ao nó que contém 'valor' (quando existirem).
        Não remove o próprio 'valor'.
        Retorna a quantidade de nós removidos (0, 1 ou 2).
        """
        cont = 0
        aux = self.prim

        if self.quant == 0:
            print('A lista está vazia')
            # return False
        else:
            while aux != None:
                if aux.info == valor:
                    if self.quant == 1:  # lista com 1 único nó
                        print('Único valor na lista, não pode ser removido')
                    elif aux.ant == None:  # nó é o primeiro
                        # Se 'valor' estiver no início, remove apenas o posterior.
                        if aux.prox != None:
                            aux.prox = aux.prox.prox
                            aux.prox.ant = aux.prox
                            self.quant -= 1
                            cont += 1
                    elif aux.prox == None: # nó é o último
                        # Se 'valor' estiver no fim, remove apenas o anterior.
                        if aux.ant != None:
                            aux.ant = aux.ant.ant
                            aux.ant.ant.prox = aux.prox
                            self.quant -= 1
                            cont += 1
                    else:  # nó no meio
                        if aux.ant == self.prim:
                            aux.ant = None
                            self.prim = aux
                            aux.prox.prox.ant = aux
                            aux.prox = aux.prox.prox
                            cont += 2
                            self.quant -= 1
                else:
                    aux = aux.prox

            print(f"Foram removidos {cont} nó(s)")



            # Se 'valor' estiver no início, remove apenas o posterior.

            # Se 'valor' estiver no fim, remove apenas o anterior.

            # Remove o nó anterior e o nó posterior ao nó que contém 'valor'.


    # ---------------- exibição ----------------
    def show(self):
        aux = self.prim
        while aux:
            print(aux.info, end='')
            aux = aux.prox
        print()

    def show_reverso(self):
        aux = self.ult
        while aux:
            print(aux.info, end='')
            aux = aux.ant
        print()
