class Conta:
    def __init__(self):
        self.extrato = 0.0
        self.lmt_saque = 3
        self.saque_realizado = 0

    def depositar(self, valor):
        if valor > 0:
            self.extrato += valor
            print(f'Depósito no valor de R${valor:.2f}')
        else:
            print('Valor de depósito inválido')

    def sacar(self, valor):
        if self.saque_realizado >= self.lmt_saque:
            print('Limite de saques diários realizado')
        elif valor > 500:
            print('O valor do saque não pode ser superior a R$500,00')
        elif valor > self.extrato:
            print('Saldo insuficiente')
        else:
            self.extrato -= valor
            self.saque_realizado += 1
            print(f'Saque de R${valor:.2f} na sua conta')

    def mostrar_extrato(self):
        print(f'Você tem R${self.extrato:.2f} na sua conta')

    def resetar_saques(self):
        self.saque_realizado = 0

def menu():
    conta = Conta()

    while True:
        escolha = int(input('''
[1] Extrato
[2] Depósito
[3] Saque
[4] Sair

Escolha: '''))

        if escolha == 2:
            valor_do_deposito = float(input('Quantos reais você gostaria de depositar? '))
            conta.depositar(valor_do_deposito)
        elif escolha ==3:
            valor_do_saque = float(input('Quanto gostaria de sacar? '))
            conta.sacar(valor_do_saque)

        elif escolha == 1:
            conta.mostrar_extrato()

        elif escolha == 4:
            break

        else:
            print('Opção inválida, tente novamente.')

menu()
