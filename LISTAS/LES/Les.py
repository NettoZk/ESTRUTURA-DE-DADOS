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
        # função que remove o valor da lista
        # não há repetição
        
        
        if self.quant == 0:
            print('A lista está vazia')
        else:
            i = 0
            while i < self.quant and self.vetor[i] != valor:
                i += 1
            if i != self.quant:
                for j in range(i, self.quant - 1):
                    self.vetor[j] = self.vetor[j + 1]
                self.quant -= 1
            else:
                print('Valor não existe ou não foi encontrado')
                
    def removerTF(self, valor):
        # remover valor da lista
        # retorna True se houver remoção
        # e False caso contrário
        if self.quant == 0:
            print('A lista está vazia')
        else:
            for i in range(self.quant):
                if self.vetor[i] == valor:
                    for j in range(i, self.quant - 1):
                        self.vetor[j] = self.vetor[j + 1]
                    self.quant -= 1
                    return True
            return False
    
    def remover_contar(self, valor):
        contador = 0
        i = 0

        if self.quant == 0:
            print('A lista está vazia')
        else:
            while i < self.quant:
                if self.vetor[i] == valor:
                    for j in range(i, self.quant - 1):
                        self.vetor[j] = self.vetor[j + 1]
                    self.quant -= 1
                    contador += 1
                    # não incrementa i, pois elemento deslocado pode ser igual
                else:
                    i += 1
            # Se contador continuar 0, significa que o valor não estava na lista
            if contador == 0:
                print('Valor não existe ou não foi encontrado')

        return contador
