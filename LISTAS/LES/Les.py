class Les:
    
    def __init__(self, tamanho):
        
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
        
        # Inicializa a lista LES com capacidade fixa.

        # Exemplo:

        # tamanho = 5

        # Vetor inicial (tamanho 5, vazio):
        # Índices:
        #  _____  _____  _____  _____  _____
        # |  0  ||  1  ||  2  ||  3  ||  4  |
        #  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        # Valores:
        #  _____  _____  _____  _____  _____
        # |     ||     ||     ||     ||     |
        #  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        # Quantidade de elementos = 0
        
    def show(self):
        
        for i in range(self.quant): 
            print(self.vetor[i], end=" ") 
        print()
        
        # Mostra os elementos da lista (do índice 0 até quant-1).
        
        # Exemplo visual:
        # Índices:
        #   _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        # Valores:
        #   _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  D  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   
        
    def inserir_fim(self, valor):
        
        if self.quant == self.tam:
            print('Não dá krlh, a lista está cheiaaaa')
        else:
            self.vetor[self.quant] = valor
            self.quant += 1
        
        # Insere um valor no final da lista, se houver espaço.

        # Exemplo:

        # Antes (quant=3):

        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||     ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 

        # Inserir_fim('D'):
        
        # Depois (quant=4):
        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  D  ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾   
    
    def remover_fim(self):
        
        if self.quant == 0:
            print('A lista está vazia')
        else:
            self.quant -= 1
        
        # Remove o último elemento da lista, se não estiver vazia.

        # Exemplo:

        # Antes (quant=4):
        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  D  ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        # Remover_fim():

        # Depois (quant=3):
        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  D  ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        # Obs: o valor na posição removida ainda existe no vetor,
        # mas não é considerado porque quant diminuiu.
        
        # Sáida no terminal após show()
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||     ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        
    def inserir_inicio(self, valor):
        
        if self.quant == self.tam:
            print('Não dá krlh, a lista está cheiaaaa')
        else:
            for i in range(self.quant, 0, -1): # (start, stop, step)
                self.vetor[i] = self.vetor[i - 1]
            self.vetor[0] = valor
            self.quant += 1
        
        # Insere um elemento no início da lista, movendo todos para a direita.

        # Exemplo:

        # Antes (quant=4):

        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  E  ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        # Passo a passo do deslocamento (do fim para o início):

        # i=4 <- valor da posição 3 (E)
        # i=3 <- valor da posição 2 (C)
        # i=2 <- valor da posição 1 (B)
        # i=1 <- valor da posição 0 (A)

        # Depois de inserir 'F' no início:
        # Depois (quant=5):

        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  F  ||  A  ||  B  ||  C  ||  E  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            
    def remover_inicio(self):
        
        if self.quant == 0:
            print('A lista está vazia')
        else:
            for i in range(self.quant - 1):
                self.vetor[i] = self.vetor[i + 1]
            # for i in range(1, self.quant):
            #     self.vetor[i - 1] = self.vetor[i]
            # self.vetor[self.quant - 1] = None # Limpa a última posição
            self.quant -= 1
        
        # Remove o primeiro elemento da lista, movendo todos para a esquerda.

        # Exemplo:

        # Antes (quant=5):

        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  F  ||  A  ||  B  ||  C  ||  E  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

        # Passo a passo do deslocamento:

        # i=1 -> posição 0 recebe 'A'
        # i=2 -> posição 1 recebe 'B'
        # i=3 -> posição 2 recebe 'C'
        # i=4 -> posição 3 recebe 'E'

        # Depois da remoção:
        # depois (quant=4):

        #  Índices:
        #   _____  _____  _____  _____  _____
        #  |  0  ||  1  ||  2  ||  3  ||  4  |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #  Valores:
        #   _____  _____  _____  _____  _____
        #  |  A  ||  B  ||  C  ||  E  ||     |
        #   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾