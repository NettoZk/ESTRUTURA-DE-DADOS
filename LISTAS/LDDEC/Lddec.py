class No:
    
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
        
class Ldsec:
    
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info)
            aux = aux.prox
    
    def inserir_incio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1