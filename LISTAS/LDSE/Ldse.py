class No:
    
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
        
class Ldse:
    
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
        
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1
        
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1
        
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            cont = 0
            aux = self.prim
            while aux.prox != self.ult:
            # while cont < self.quant - 2:
                aux = aux.prox
                cont += 1
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1
            
    def ver_primeiro(self):
        return self.prim.info
    
    def ver_ultimo(self):
        return self.ult.info
    
    def ver_quantidade(self):
        return self.quant
    
    def esta_vazia(self):
        return self.quant == 0
    
    def show(self): 
        aux = self.prim 
        while aux != None:
            print(aux.info, end=' ') 
            aux = aux.prox 
        print('\n')
        
    def remover_irmaos(self, valor):
        if self.quant != 1 and self.quant != 0:
            anterior_do_anterior = None
            anterior = None
            atual = self.prim
            while atual != None and atual.info != valor:
            # andando pela lista até achar valor ou chegar ao fim da lista
                anterior_do_anterior = anterior
                anterior = atual
                atual = atual.prox
            if atual != None and atual.info == valor:
            # ou seja, achou valor na lista e ele está no nó atual
                if anterior != None and anterior == self.prim:
                # age se o irmão anterior for o primeiro da lista
                    self.remover_inicio()
                else:
                    if anterior_do_anterior != None:
                    # caso o irmão anterior não seja o primeiro da lista
                        anterior_do_anterior.prox = atual
                        anterior = None
                        self.quant -= 1
                if atual.prox != None and atual.prox == self.ult:
                # age se o irmão posterior for o último da lista
                    self.remover_fim()
                else:
                    if atual.prox != None:
                    # caso o irmão posterior não seja o último da lista
                        proximo = atual.prox
                        atual.prox = proximo.prox
                        proximo = None
                        self.quant -= 1
