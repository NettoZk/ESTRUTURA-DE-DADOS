class Tree:
    
    def __init__(self):
        self.raiz = None
    
    def insere(self, valor):
        if self.raiz == None:
            print(f'Criando raiz com {valor}')
            self.raiz = No(valor)
        else:
            print(f'\nInserindo {valor}...')
            self.raiz.insere(valor, origem="RAIZ")
            print()


class No:
    
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
        
    def insere(self, valor, origem):
        print(f'[NO {self.info}] Recebido de {origem}: decidir onde inserir {valor}')
        
        if valor < self.info:
            print(f'  {valor} < {self.info} → ESQ')
            if self.esq == None:
                print(f'  ESQ de {self.info} está vazio → inserindo {valor} em ESQ de {self.info}')
                self.esq = No(valor)
            else:
                print(f'  ESQ de {self.info} ocupado por {self.esq.info} → repassando... para {self.info}')
                self.esq.insere(valor, origem=f'NO {self.info}')
        else:
            print(f'  {valor} > {self.info} → DIR')
            if self.dir == None:
                print(f'  DIR de {self.info} está vazio → inserindo {valor} em DIR de {self.info}')
                self.dir = No(valor)
            else:
                print(f'  DIR de {self.info} ocupado por {self.dir.info} → repassando... para {self.info}')
                self.dir.insere(valor, origem=f'NO {self.info}')
