manifestacoes = [ ]
opcao = 8

while opcao != 7:
  print('-' * 70)
  print('{}Seja bem vindo à ouvidoria da Celgon{}'.format('\033[1;34m', '\033[m'))
  print('-' * 70)
  print()
  print('Menu do Sistema')
  print()
  print('Opcões:')
  print()
  print('Digite 1 para acessar seu cadastro')
  print('Digite 2 para criar uma manifestação')
  print('Digite 3 para ver a lista de manifestações')
  print('Digite 4 para excluir algum item da lista de manifestações')
  print('Digite 5 para apagar toda a lista de manifestações')
  print('Digite 6 para ser encaminhado à um atendente')
  print('Digite 7 para sair')
  print()
  opcao = int(input('Digite a sua opção: '))


  if opcao == 1:
    e = input('{}Digite o seu email: {}'.format('\033[1;34m', '\033[m'))
    s = input('{}Digite a sua senha: {}'.format('\033[1;34m', '\033[m'))
    n = input('{}Digite seu nome: {}'.format('\033[1;34m', '\033[m'))
    print('{}Olá, seja bem vindo {}{}'.format('\033[1;34m', '\033[m', n.title()))


  elif opcao == 2:
    print('{}Agora vamos criar uma manifestação:{}'.format('\033[1;34m', '\033[m'))
    titulo = input('{}Qual a sua manifestação: {}'.format('\033[1;34m', '\033[m'))
    manifestacoes.append(titulo)


  elif opcao == 3:
    print('{}Listagem das manifestações:{}'.format('\033[1;34m', '\033[m'))
    for item in manifestacoes:
      print(('{}- {}' + item).format('\033[1;34m', '\033[m'))
    print()
    print('{}Fim da lista!{}'.format('\033[1;34m', '\033[m'))


  elif opcao == 4:
    itemexcluido = int(input('Digite qual valor da lista você deseja apagar: '))
    del(manifestacoes[itemexcluido])
    print('{}O item selecionado foi apagado.{}'.format('\033[1;34m', '\033[m'))


  elif opcao == 5:
    manifestacoes.clear()
    print('{}Sua lista de manifestações foi apagada.{}'.format('\033[1;34m', '\033[m'))


  elif opcao == 6:
    print('{}Você será redirecionado para um atendente, por favor aguarde...{}'.format('\033[1;34m', '\033[m'))
    print('{}Olá meu nome é Sérgio, em que posso ajudar?{}'.format('\033[1;34m', '\033[m'))


print('{}Por favor, avalie o nosso atendimento com uma nota de 0 a 10.{}'.format('\033[1;34m', '\033[m'))
nota = input('Qual a sua nota para o nosso atendimento: ')
print('{}Obrigado pela sua atenção, a Celgon agradece!{}'.format('\033[1;34m', '\033[m'))
print('-' * 70)