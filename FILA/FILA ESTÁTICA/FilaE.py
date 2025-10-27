class FilaE:
    
    def __init__(self, tamanho):
        
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
        
    def inserir_fim(self, valor):
        if self.quant == self.tam:
            print('Não dá krlh, a lista está cheiaaaa')
        else:
            self.vetor[self.quant] = valor
            self.quant += 1
            
    def remover_inicio(self):
        if self.quant == 0:
            print('A lista está vazia')
        else:
            for i in range(self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            self.quant -= 1
            
    def ver_primeiro(self):
        return self.vetor[0]
    
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def show(self):
        for i in range(self.quant): 
            print(self.vetor[i], end=" ") 
        print()