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
            for i in range(self.quant, 0, -1): # (start, stop, step)
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
        
    def remover(self, valor):
        #pos = 999
        if self.quant == 0:
            print('A lista está vazia')
        else:
            if valor in self.vetor:
                for i in range(self.quant):
                    if valor == self.vetor[i]:
                        # pos = i
                        # for i in range(pos, self.quant - 1):
                        for j in range(i, self.quant - 1):
                            self.vetor[j] = self.vetor[j + 1]
                        self.quant -= 1
                        return  #coloquei para que caso haja repetição ele pare na primeira, se retirar, tira todas
            else:
                print('Valor não existe ou não foi encontrado')
                
    def removerTF(self, valor):
        pass
    
    def remover_contar(self, valor):
        pass