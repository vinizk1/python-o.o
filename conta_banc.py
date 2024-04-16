class ContaBancaria:
    def __init__(self, num, tit, saldo=0):
        self.num = num
        self.tit = tit
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_detalhes(self):
        print("Número da conta:", self.num)
        print("Titular:", self.tit)
        print("Saldo:", round(self.saldo, 2))

def main():
    num_conta = input("Digite o número da conta: ")
    tit_conta = input("Digite o titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: ").replace(',', '.'))

    conta_usuario = ContaBancaria(num_conta, tit_conta, saldo_inicial)

    while True:
        print("\n1. Depositar")
        print("2. Sacar")
        print("3. Exibir detalhes da conta")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a ser depositado: ").replace(',', '.'))
            conta_usuario.depositar(valor_deposito)
            print("Depósito realizado com sucesso!.")
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a ser sacado: ").replace(',', '.'))
            conta_usuario.sacar(valor_saque)
        elif opcao == "3":
            conta_usuario.exibir_detalhes()
        elif opcao == "4":
            print("hasta la vista baby")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
