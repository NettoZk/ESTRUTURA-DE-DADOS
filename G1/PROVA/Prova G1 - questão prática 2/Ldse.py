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
                aux = aux.prox
                cont += 1
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1
        
    def show(self): 
        aux = self.prim 
        while aux != None:
            print(aux.info, end=' ') 
            aux = aux.prox 
        print('\n')
        
    def ver_quantidade(self):
        return self.quant
# ===================== Resposta da questão AQUI ========================================
        
    def remover_depois(self, valor):
        if self.quant == 1 and self.prim.info == valor:
            print('Valor é o único na lista, não tem depois para ser removido')
        else:
            aux = self.prim
            ant = None
            contador = 0
            while aux != None and aux.info != valor:
                ant = aux
                aux = aux.prox
            if aux != None:
                navegador = aux
                if aux == self.prim:
                    while navegador != self.ult:
                        navegador = navegador.prox
                        contador += 1
                    aux.prox = None
                    self.quant = self.quant - contador
                else:
                    if aux == self.ult:
                        print('Este valor é o último, não tem ninguém para ser removido após ele')
                    else:
                        while navegador != self.ult:
                            navegador = navegador.prox
                            contador += 1
                        aux.prox = None
                        self.ult = aux
                        self.quant = self.quant - contador
            else:
                print('Valor não existe ou não foi encontrado!')    