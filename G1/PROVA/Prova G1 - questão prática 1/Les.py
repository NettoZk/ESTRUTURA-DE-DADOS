
class Les:
    
    def __init__(self, tamanho):
        
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
        
    def show(self):
        
        for i in range(self.quant): 
            print(self.vetor[i], end=" ") 
        print()  
    
    def inserir_fim(self, valor):
        if self.quant == self.tam:
            print('Não dá krlh, a lista está cheiaaaa')
        else:
            self.vetor[self.quant] = valor
            self.quant += 1
    
    def remover_fim(self):
        
        if self.quant == 0:
            print('A lista está vazia')
        else:
            self.quant -= 1

    def inserir_inicio(self, valor):
        
        if self.quant == self.tam:
            print('Não dá krlh, a lista está cheiaaaa')
        else:
            for i in range(self.quant, 0, -1):
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[0] = valor
            self.quant += 1
            
    def remover_inicio(self):
        
        if self.quant == 0:
            print('A lista está vazia')
        else:
            for i in range(self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            self.quant -= 1
            
    def ver_quantidade(self):
        return self.quant
            
# ========================== função resposta AQUI =====================================

    def remover_depois(self, valor):
        if self.quant == 0:
            print('A lista está vazia')
        else:
            i = 0
            while i < self.quant and self.vetor[i] != valor:
                i += 1
            if i != self.quant:
                for j in range(i, self.quant - 1):
                    self.quant -= 1
            else:
                print('Valor não existe ou não foi encontrado')
                