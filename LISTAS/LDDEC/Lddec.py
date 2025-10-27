class No:
    
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
        
class Lddec:
    
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
            self.prim = self.ult = No(None, valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1
        
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
            self.prim.ant = self.ult.prox = self.prim
        else:
            self.ult.prox = self.ult = No(self.ult, valor, self.prim)
            self.prim.ant = self.ult
        self.quant += 1
        
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = self.ult
            self.ult.prox = self.prim
    
    def remover_todos_apos(self, valor):
        if self.quant == 1:
            print("Não tem valores após o valor informado!")
        else:
            aux = self.prim
            cont = 1
            while aux.info != valor:
                aux = aux.prox
                cont += 1
            if aux.info == valor:
                self.ult = aux
                self.ult.prox = self.prim
                self.prim.ant = self.ult
        self.quant = cont

            