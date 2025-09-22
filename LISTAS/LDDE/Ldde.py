class No:
    
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
        
class Ldde:
    
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
        
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1
        
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
        
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
        print('\n')
        
    def show_reverso(self):
        aux = self.ult
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.ant
        print('\n')
        
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1
        
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
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
    
    def remover(self, valor):
        if self.quant == 0:
            print('A lista está vazia')
            return False
            
        aux = self.prim
        while aux != None and aux.info != valor:
            aux = aux.prox
            
        if aux == None:
            print(f"Valor {valor} não encontrado na lista.")
            return False
        if aux == self.prim and aux == self.ult:
            self.prim = self.ult = None
        elif aux == self.prim:
            self.prim = self.prim.prox
            self.prim.ant = None
        elif aux == self.ult:
            self.ult = self.ult.ant
            self.ult.prox = None
        else:
            aux.ant.prox = aux.prox
            aux.prox.ant = aux.ant
            
        self.quant -= 1        

    
    def removerTF(self, valor):
        aux = self.prim
        
        if self.quant == 1 and aux.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
            return True
        
        while aux != None and aux.info != valor:
            aux = aux.prox
            
        if aux == None:
            return False
        if aux == self.prim and aux == self.ult:
            self.prim = self.ult = None
        elif aux == self.prim:
            self.prim = self.prim.prox
            self.prim.ant = None
        elif aux == self.ult:
            self.ult = self.ult.ant
            self.ult.prox = None
        else:
            aux.ant.prox = aux.prox
            aux.prox.ant = aux.ant
            
        self.quant -= 1 
        return True
    
    def remover_contar(self, valor):
        cont = 0
        aux = self.prim
        if self.quant == 1 and aux.info == valor:
            self.prim = self.ult = None
            self.quant -= 1
            cont += 1
        else:
            while aux != None:
                if aux.info == valor:
                    if aux.ant == None:
                        aux = self.prim = aux.prox
                        self.prim.ant = None
                    elif aux.prox == None:
                        aux = self.ult = aux.ant
                        self.ult.prox = None
                    else:
                        aux.ant.prox = aux.prox
                        aux.prox.ant = aux.ant
                    cont += 1
                    self.quant -= 1
                aux = aux.prox
        print(f"O valor {valor} foi removido {cont} vez(es)")