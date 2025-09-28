class No:
    def __init__(self, ant, info, prox):
        self.ant  = ant
        self.info = info
        self.prox = prox


class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    # ---------------- inserções ----------------
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    # --------------- remoção por intervalo ---------------
    
    def remover_vizinhos(self, valor):       
        if self.quant != 0 and self.quant != 1:
            contador_no_removidos = 0
            aux = self.prim  
            while aux != None and aux.info != valor:
                aux = aux.prox
            # entra aqui quando achar o valor 
            if aux != None:
                # remoção do nó anterior
                if aux != self.prim: # verifico antes se o nosso nó não é o primeiro (self.prim)
                    if aux.ant == self.prim: # se por caso o nó anterior do nosso AUX que precisa ser removido for o primeiro (self.prim)
                        self.prim = aux # atualizamos os ponteiros do PRIM para o nosso AUX, tornando ele o primeiro (self.prim)
                        aux.ant = None # e atualizamos o ponteiro do anterior apontar para None, agora ele é o primeiro (não tem ninguém antes)
                    # em outros casos 
                    else:
                        aux.ant = aux.ant.ant # atualizamos o nosso ant do AUX para onde o ponteiro do anterior do anterior apontava
                        aux.ant.prox = aux # e atualizamos o prox do nosso atual anterior para apontar para AUX
                    self.quant -= 1
                    contador_no_removidos += 1
                    print('removido no "aux != self.prim"')               
                # remoção no nó posterior
                if aux != self.ult: # verifico antes se o nosso nó não é o úlitmo nó (self.ult)
                    if aux.prox == self.ult: # se por acaso o nó próximo do nosso AUX que precisa ser removido for o último (self.ult)
                        self.ult = aux # atualizamos o ponteiro do ULT para nosso AUX, tornando ele o ùltimo (self.ult)
                        aux.prox = None # e atualizamos o ponteiro do prox para None, já que ele agora é o último (não tem ninguém depois)
                    # em outros casos
                    else:
                        aux.prox = aux.prox.prox # atualizamos o nosso prox do AUX para onde o ponteiro do proximo do proximo apontava
                        aux.prox.ant = aux # e atualizamos o prox nosso atual anterior para a apontar para AUX
                    self.quant -= 1
                    contador_no_removidos += 1
                    print('removido no "aux != self.ult"')                   
                return contador_no_removidos           
            else:
                print('Valor não foi encontrado na lista!')
                return 0
        else:
            print('A lista tem 0 ou 1 elemento, não tem vizinho(s) para ser removido')
            return 0
            
    # ---------------- exibição ----------------
    def show(self):
        aux = self.prim
        while aux:
            print(aux.info, end='')
            aux = aux.prox
        print()

    def show_reverso(self):
        aux = self.ult
        while aux:
            print(aux.info, end='')
            aux = aux.ant
        print()
