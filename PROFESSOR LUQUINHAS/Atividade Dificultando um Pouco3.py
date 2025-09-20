class Funcionario():
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario:.2f}")
        else:
            print("Percentual de aumento inválido.")

#🏄‍♂️ TESTE DO SISTEMA
funcionario1 = Funcionario("Gustavo Fabiam", 3000, "Desenvolvedor Full Stack")
funcionario1.aumentar_salario(10)
funcionario1.aumentar_salario(-5)  # AUMENTO INVÁLIDO EXEMPLO
print("----------------------------------------")
funcionario2 = Funcionario("Emanuel Cardoso", 2500, "Analista de Sistemas")
funcionario2.aumentar_salario(15)
funcionario2.aumentar_salario(0)  # AUMENTO INVÁLIDO EXEMPLO
#🏄‍♂️ ATIVIDADE COMPLETA.