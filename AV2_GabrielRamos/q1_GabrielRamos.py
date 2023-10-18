cpfColocado=input('Qual o seu usuário de cpf?')
senhaColocada=input('Qual a sua senha?')

cpf='000.000.000-00'
senha='123'
saldo=500

podeSacar=lambda saldo,valorMovimentado: print(saldo-int(valorMovimentado)) if saldo>=int(valorMovimentado) else print('valor inviavel')
decisao=lambda escolha,saldo,valorMovimentado: print(saldo+int(valorMovimentado)) if escolha=='1' else podeSacar(saldo,valorMovimentado)
entrar= lambda cpf,senha,saldo,cpfColocado,senhaColocada: decisao(input('0 para saque e 1 para deposito'),saldo,input('defina quanto voce quer movimentar da conta')) if cpf==cpfColocado and senha==senhaColocada else print('não vai passar')

entrar(cpf,senha,saldo,cpfColocado,senhaColocada)

print(saldo)