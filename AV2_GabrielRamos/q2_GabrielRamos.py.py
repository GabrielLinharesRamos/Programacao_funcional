login=input('Qual o seu usuário de login?')
senha=input('Qual a sua senha?')
dados = open('dados.txt', 'r')
flag=0

palavras = dados.read().split('\n')
logins=palavras[0].split(' ')
senhas=palavras[1].split(' ')

b=lambda senha,possivelSenha,senhas: [print('SUCESSO') if senhas[possivelSenha]==senha else print('FRACASSO')]
a=lambda logins,login,senha,senhas: [b(senha,logins.index(login),senhas) if login in logins else print('FRACASSO')]


a(logins,login,senha,senhas)


