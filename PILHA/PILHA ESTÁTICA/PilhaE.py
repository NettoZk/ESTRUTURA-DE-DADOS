class PilhaE:
    
    def __init__(self, tamanho):
        
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0      
    
    def push(self, valor):
        if self.quant == self.tam:
            print('Não dá krlh, a pilha está cheiaaaa')
        else:
            self.vetor[self.quant] = valor
            self.quant += 1
    
    def pop(self):
        if self.quant == 0:
            print('A lista está vazia')
        else:
            self.quant -= 1
            
    def ver_ultimo(self):
        return self.vetor[self.quant - 1]
        
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def show(self):
        for i in range(self.quant): 
            print(self.vetor[i], end=" ") 
        print()