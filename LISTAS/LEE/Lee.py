class No:
    
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo
        
class Lee:
    
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * self.tam_maximo
        self.quant = 0
        
        self.prox_pos_vazia = self.inicializa_estrutura()
        
        self.prim = -1
        self.ult = -1  
        
    def inicializa_estrutura(self):
        for i in range(self.tam_maximo - 1):
            self.vetor[i] = No(None, i + 1)
        self.vetor[self.tam_maximo - 1] = No(None, -1)
        return 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1
        else:
            self.prim = self.ocupa_no(valor, self.prim)
            self.quant += 1
    
    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1
        else:
            self.vetor[self.ult].prox = self.ult = self.ocupa_no(valor, -1)
            self.quant += 1
    
    def ocupa_no(self, valor, proximo):
        posicao_livre = self.prox_pos_vazia
        self.prox_pos_vazia = self.vetor[self.prox_pos_vazia].prox
        self.vetor[posicao_livre] = No(valor, proximo)
        return posicao_livre
    
    '''def show(self):
        aux = self.prim
        while aux != -1:
            print(self.vetor[aux].info)
            aux = self.vetor[aux].prox'''
            
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(self.vetor[aux].info)
            aux = self.vetor[aux].prox
        
    def show_vetor(self):
        print('Prim = ', self.prim)
        print('Ult = ', self.ult)
        print('Primeira pos vazia = ', self.prox_pos_vazia)
        print('Vetor =')
        for i in range(self.tam_maximo):
            print(i, self.vetor[i].info, self.vetor[i].prox)
            
    def devolve_no(self, no):
        self.vetor[no].prox = self.prox_pos_vazia
        self.prox_pos_vazia = no
        
    def remover_inicio(self):
        if self.quant == 1:
            self.devolve_no(self.prim)
            self.prim = self.ult = -1
        else:
            novo_prim = self.vetor[self.prim].prox
            self.devolve_no(self.prim)
            self.prim = novo_prim
        self.quant -= 1
        
    # def remover_fim(self):
    #     if self.quant == 1:
    #         self.devolve_no(self.prim)
    #         self.prim = self.ult - 1
    #     else:
    #         aux = self.prim
    #         while self.vetor[aux].prox != self.ult:
    #             aux = self.vetor[aux].prox
    #         self.devolve_no(self.ult)
    #         self.vetor[aux].prox -= 1
    #         self.ult = aux
    #     self.quant -= 1
        
    def remover_fim(self): 
        if self.quant == 1: 
            self.devolve_no(self.prim) 
            self.prim = self.ult = -1 
        else: 
            aux = self.prim 
            for i in range(self.quant-2): 
                aux = self.vetor[aux].prox 
            self.devolve_no(self.ult) 
            self.vetor[aux].prox = -1 
            self.ult = aux 
        self.quant-=1 
        
    def tamanho_atual(self):
        return self.quant
    
    def capacidade(self):
        return self.tam_maximo
    
    def esta_vazia(self):
        return self.quant == 0
    
    def esta_cheia(self):
        return self.quant == self.tam_maximo
    
    def ver_primeiro(self):
        return self.vetor[self.prim].info
    
    def ver_ultimo(self):
        return self.vetor[self.ult].info
    
    def remover_imaos(self, valor):
        if self.quant != 1 and self.quant != 0:
            anterior_do_anterior = -1
            anterior = -1
            atual = self.prim
            while self.vetor[atual].info != valor and atual != -1:
                anterior_do_anterior = anterior
                anterior = atual
                atual = self.vetor[atual].prox
            if self.vetor[atual].info == valor:
                if self.vetor[self.prim].prox == atual:
                    self.remover_inicio()
                else:
                    if atual != self.prim:
                        self.vetor[anterior_do_anterior].prox = atual
                        self.devolve_no(anterior)
                        self.quant -= 1
                if self.vetor[atual].prox == self.ult:
                    self.remover_fim()
                else:
                    if atual != self.ult:
                        proximo = self.vetor[atual].prox
                        self.vetor[atual].prox = self.vetor[proximo].prox
                        self.devolve_no(proximo)
                        self.quant -= 1
                        
    def remover_elemento(self, valor):
        if self.quant == 0:  
            print("A lista está vazia, não é possível remover.")
            return False

        anterior = -1
        atual = self.prim  
        
        while atual != -1 and self.vetor[atual].info != valor:
            anterior = atual
            atual = self.vetor[atual].prox

        if atual == -1:
            print(f"Elemento {valor} não encontrado.")
            return False

        if atual == self.prim: 
            self.prim = self.vetor[atual].prox
        elif atual == self.ult: 
            self.ult = anterior
            self.vetor[anterior].prox = -1
        else: 
            self.vetor[anterior].prox = self.vetor[atual].prox
        self.devolve_no(atual)
        self.quant -= 1
        print(f"Elemento {valor} removido com sucesso.")
        return True

    def remover_elemento(self, valor):
        if self.quant == 0:  
            return
        anterior = -1
        atual = self.prim
        while atual != -1 and self.vetor[atual].info != valor:
            anterior = atual
            atual = self.vetor[atual].prox
        if atual == -1:
            return
        if atual == self.prim:
            self.prim = self.vetor[atual].prox
        elif atual == self.ult:
            self.ult = anterior
            self.vetor[anterior].prox = -1
        else:
            self.vetor[anterior].prox = self.vetor[atual].prox
        self.devolve_no(atual)
        self.quant -= 1

    def buscar(self, valor):
        pos = 0
        aux = self.prim
        while aux != -1:
            if self.vetor[aux].info == valor:
                return pos
            aux = self.vetor[aux].prox
            pos += 1
        return None

    def inserir_apos(self, valor1, valor2):
        aux = self.prim
        while aux != -1 and self.vetor[aux].info != valor2:
            aux = self.vetor[aux].prox
        if aux == -1:
            return
        novo_no = self.ocupa_no(valor1, self.vetor[aux].prox)
        self.vetor[aux].prox = novo_no
        if aux == self.ult:
            self.ult = novo_no
        self.quant += 1

    def inserir_antes(self, valor1, valor2):
        if self.quant == 0:
            return
        if self.vetor[self.prim].info == valor2:
            self.inserir_inicio(valor1)
            return
        anterior = self.prim
        atual = self.vetor[self.prim].prox
        while atual != -1 and self.vetor[atual].info != valor2:
            anterior = atual
            atual = self.vetor[atual].prox
        if atual == -1:
            return
        novo_no = self.ocupa_no(valor1, atual)
        self.vetor[anterior].prox = novo_no
        self.quant += 1
