class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")
        
    def exibir_saldo(self):
        print(f" {self.titular} seu saldo atual é de: R${self.saldo:.2f}")
#🏄‍♂️ TESTE DO SISTEMA
conta1 = Conta_Bancaria("Gustavo Fabiam", 1000)
conta1.exibir_saldo()
conta1.depositar(500)
conta1.exibir_saldo()
conta1.sacar(200)
conta1.exibir_saldo()
conta1.sacar(2000)  # SAQUE MAIOR QUE O SALDO ATUAL
# ---------------
print("----------------------------------------")
# ----------------
conta2 = Conta_Bancaria("Emanuel Cardoso", 1500)
conta2.exibir_saldo()
conta2.depositar(300)
conta2.exibir_saldo()
conta2.sacar(100)
conta2.exibir_saldo()
conta2.sacar(2000)  # SAQUE MAIOR QUE O SALDO ATUAL
#🏄‍♂️ ATIVIDADE COMPLETA.
