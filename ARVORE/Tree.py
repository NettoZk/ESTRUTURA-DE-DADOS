class No:
    
    def __init__(self, valor):
        self.info = valor
        self.dir = None
        self.esq = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None: 
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.inOrdem()
            
    def preOrdem(self):
        print(self.info, end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()
            
    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem
        print(self.info, end=" ")
    
    #Imprimir todos os nós ancestrais do nó que contém valor.
    def print_ancestrais(self, valor):
        if valor < self.info:
            if self.esq != None:
                print(self.info, end=' ')
                self.esq.print_ancestrais(valor)
        elif valor > self.info:
            if self.dir != None:
                print(self.info, end=' ')
                self.dir.print_ancestrais(valor)
    
    #Imprimir todos os nós do menor caminho do nó raiz ao nó que contém valor.
    def print_caminho(self, valor):
        print(self.info, end=' ')
        if valor < self.info:
            if self.esq != None:
                self.esq.print_caminho(valor)
        else:
            if self.dir != None:
                self.dir.print_caminho(valor)

    #Imprimir somente os nós que são nós internos e ancestrais do nó que contém valor.
    def print_ancestrais_internos(self, valor): 
        if valor < self.info:
            if self.esq != None:
                print(self.info, end=' ')
                self.esq.print_ancestrais_internos(valor)
        elif valor > self.info:
            if self.dir != None:
                print(self.info, end=' ')
                self.dir.print_ancestrais_internos(valor)
    
    #Imprimir em ordem crescente todos os nós descendentes do nó que contém o maior valor da árvore.
    def print_descendentes_do_maior(self):
        if self.dir != None:
            self.dir.print_descendentes_do_maior()
        else:
            self.esq.inOrdem()
    
    #Imprimir em ordem crescente todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore e que são menores que ele.
    def print_ida_ao_maior(self):
        print(self.info, end=' ')
        if self.dir != None:
            self.dir.print_ida_ao_maior()
            
    def print_ida_ao_menor(self):
        print(self.info, end=" ")
        if self.esq != None:
            self.esq.print_ida_ao_menor()

    #Retornar a soma de todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore.
    def soma_ida_ao_maior(self):
        soma_total = self.info
        if self.dir != None:
            soma_total += self.dir.soma_ida_ao_maior()
        return soma_total
    
    def soma_ida_ao_menor(self):
        soma_total = self.info
        if self.esq != None:
            soma_total += self.esq.soma_ida_ao_menor()
        return soma_total
    
    def busca(self, valor):
        if valor ==  self.info:
            # print(self.info)
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                # print(self.info)
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                # print(self.info)
                return self.dir.busca(valor)     
    
    def distancia(self, valor):
        
        # essa função verificar se um valor está presente na árvore binária e, se encontrado, calcular a "distância" 
        # (número de nós visitados a partir do nó atual até o nó onde o valor está localizado).
        
        if valor ==  self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.distancia(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.distancia(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
                
    def distancia_em_nos(self, valor):
        if valor ==  self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return 1 + self.esq.distancia_em_nos(valor)
        else:
            if self.dir == None:
                return False
            else:
                return 1 + self.dir.distancia_em_nos(valor)
            
    def soma_nos_visitados(self, valor):
        if valor ==  self.info:
            return self.info
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.info + self.esq.soma_nos_visitados(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.info + self.dir.soma_nos_visitados(valor)
            
    def printFolhas(self):
        
        # método para imprimir todos os nós folha de uma árvore binária. 
        # Um nó folha é aquele que não possui filhos, ou seja, ambos esq(esquerda) e dir(direita) são None.
        
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info, end=" ")
        if self.dir != None:
            self.dir.printFolhas()
            
    def soma(self):
        
        # calcular a soma de todos os valores armazenados em nós de uma árvore binária
        
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
    
    def somaFolhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
    
    def altura(self):
        hesq = hdir = -1
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)
    
    def h(self, valor):
        
        # O método hbusca um nó específico na árvore e retorna a altura do subárvore com raiz nesse nó,
        # caso o valor seja encontrado. Se o valor não existir na árvore, o método retorna False.
        
        if valor == self.info:
            return self.altura()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)
            
    def nivel(self, valor):
        
        # O método nivelbusca o nível de um nó específico na árvore. O nível de um nó é definido como 
        # a quantidade de arestas entre a raiz da árvore e o nó. Se o valor não for encontrado, o método retorna 0.
        
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0
                
    def quant(self, valor):
        
        # O método quantcalcula quantas vezes um determinado valor aparece na subárvore com raiz no nó atual.
        # Este método é útil para árvores onde valores duplicados podem existir.
        
        total = 0
        if self.info == valor:  # Se o valor do nó atual é igual ao valor buscado
            total = 1
        if self.esq != None:  # Soma as ocorrências na subárvore esquerda
            total += self.esq.quant(valor)
        if self.dir != None:  # Soma as ocorrências na subárvore direita
            total += self.dir.quant(valor)
        return total  # Retorna o total de ocorrências
    
    def maisDir(self):
        
        # o mais a direita é aquele filho que fica no extremo direito da arvore
        
        
        if self.dir != None:
            return self.dir.maisDir()
        else:
            return self.info
        
    def maisEsq(self):
        
        # o mais a esquerda é o cara que fica ao extremo esquerda da arvore
        
        if self.esq != None:
            return self.esq.maisEsq()
        else:
            return self.info
        
    def print_tem_filho(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                self.esq.print_tem_filho(valor)
                print(self.info, end=" ")
        else:
            if self.dir == None:
                return False
            else:
                self.dir.print_tem_filho(valor)
                print(self.info, end=" ")
    
    def print_internos(self, valor):
        if valor == self.info:
            print()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                print(self.info, end=" ")
                return self.esq.print_internos(valor)
        else:
            if self.dir == None:
                return False
            else:
                print(self.info, end=" ")
                return self.dir.print_internos(valor)
            
    def print_ancestrais_do_menor(self):
        if self.esq != None:
            print(self.info, end=" ")
            self.esq.print_ancestrais_do_menor()
        else:
            print()
            
    def print_caminho_decrescente(self, valor):
        valores = []  # Lista para armazenar os valores do caminho

        # Função auxiliar para coletar os valores
        def coleta_valores(no, valor):
            if no is None:  # Caso base: nó inexistente
                return
            valores.append(no.info)  # Armazena o valor atual
            if valor < no.info:  # Move para a subárvore esquerda
                coleta_valores(no.esq, valor)
            elif valor > no.info:  # Move para a subárvore direita
                coleta_valores(no.dir, valor)

        # Inicia a coleta de valores
        coleta_valores(self, valor)

        # Ordena os valores em ordem decrescente e imprime
        for v in sorted(valores, reverse=True):
            print(v, end=" ")
        print()  # Nova linha ao final da impressão

            
class Tree:
    
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
    
    def quant(self, valor):
        if self.raiz != None:
            return self.raiz.quant(valor)
    
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def h(self, valor):
        if self.raiz != None:
            return self.raiz.h(valor)
    
    def inOrdem(self):
        if self.raiz != None:
            return self.raiz.inOrdem()
        
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    #Imprimir todos os nós ancestrais do nó que contém valor.
    def print_ancestrais(self, valor):
        if self.raiz != None:
            self.raiz.print_ancestrais(valor)
            print() #serve unicamente para dar quebra de linha após finalizar
    
    #Imprimir todos os nós do menor caminho do nó raiz ao nó que contém valor.
    def print_caminho(self, valor):
        if self.raiz != None:
            self.raiz.print_caminho(valor)
            print()

    #Imprimir somente os nós que são nós internos e ancestrais do nó que contém valor.
    def print_ancestrais_internos(self, valor):
        if self.raiz != None:
            self.raiz.print_ancestrais_internos(valor)
            print()
    
    #Imprimir em ordem crescente todos os nós descendentes do nó que contém o maior valor da árvore.
    def print_descendentes_do_maior(self):
        if self.raiz != None:
            self.raiz.print_descendentes_do_maior()
            print()
    
    #Imprimir em ordem crescente todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore e que são menores que ele.
    def print_ida_ao_maior(self):
        if self.raiz != None:
            self.raiz.print_ida_ao_maior()
    
    #Retornar a soma de todos os nós do menor caminho do nó raiz ao nó que contém o maior valor da árvore.
    def soma_ida_ao_maior(self):
        if self.raiz != None:
            return self.raiz.soma_ida_ao_maior()
        
    def busca(self, valor):
        if self.raiz ==  None:
            return False
        else:
            return self.raiz.busca(valor)
        
    def distancia(self, valor):
        if self.raiz ==  None:
            return False
        else:
            return self.raiz.distancia(valor)
        
    def distancia_em_nos(self, valor):
        if self.raiz ==  None:
            return False
        else:
            return self.raiz.distancia_em_nos(valor)
        
    def soma_nos_visitados(self, valor):
        if self.raiz ==  None:
            return False
        else:
            return self.raiz.soma_nos_visitados(valor)
        
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
            
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
            
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
        
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()
        
    def nivel(self, valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)
        
    def maisDir(self):
        if self.raiz != None:
            return self.raiz.maisDir()
        
    def maisEsq(self):
        if self.raiz != None:
            return self.raiz.maisEsq()
        
    def print_caminho_decrescente(self, valor):
        if self.raiz != None:
            self.raiz.print_caminho_decrescente(valor)
        
    def print_caminho(self, valor):
        if self.raiz != None:
            self.raiz.print_caminho(valor)

    def print_ancestrais_do_menor(self):
        if self.raiz != None:
            self.raiz.print_ancestrais_do_menor()

    def print_internos(self, valor):
        if self.raiz != None:
            self.raiz.print_internos(valor)

    def print_tem_filho(self, valor):
        if self.raiz != None:
            self.raiz.print_tem_filho(valor)

    def print_ida_ao_menor(self):
        if self.raiz != None:
            self.raiz.print_ida_ao_menor()

    def soma_ida_ao_menor(self):
        if self.raiz != None:
            return self.raiz.soma_ida_ao_menor()
        return 0