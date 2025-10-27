import FilaD

class FilaP:
    
    def __init__(self):
        self.f1 = FilaD.FilaD()
        self.f2 = FilaD.FilaD()
        self.f3 = FilaD.FilaD()
        self.f4 = FilaD.FilaD()
        
    def inserir(self, valor, prior):
        if prior == 1:
            self.f1.inserir_fim(valor)
        elif prior == 2:
            self.f2.inserir_fim(valor)
        elif prior == 3:
            self.f3.inserir_fim(valor)
        elif prior == 4:
            self.f4.inserir_fim(valor)
        else:
            print("Prioridade inválida.")
    
    def remover(self):
        if not self.f1.esta_vazia():
            return self.f1.remover_inicio()
        elif not self.f2.esta_vazia():
            return self.f2.remover_inicio()
        elif not self.f3.esta_vazia():
            return self.f3.remover_inicio()
        elif not self.f4.esta_vazia():
            return self.f4.remover_inicio()
        else:
            print("Fila vazia.")
            
    def ver_primeiro(self):
        if not self.f1.esta_vazia():
            return self.f1.ver_primeiro()
        elif not self.f2.esta_vazia():
            return self.f2.ver_primeiro()
        elif not self.f3.esta_vazia():
            return self.f3.ver_primeiro()
        elif not self.f4.esta_vazia():
            return self.f4.ver_primeiro()
        
    def esta_vazia(self):
        return (self.f1.esta_vazia() and 
                self.f2.esta_vazia() and 
                self.f3.esta_vazia() and 
                self.f4.esta_vazia())
        
    def show(self):
        self.f1.show()
        self.f2.show()
        self.f3.show()
        self.f4.show()