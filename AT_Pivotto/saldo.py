import matplotlib.pyplot as plt

def exibir_grafico(x, y):
  plt.plot(x, y)
  plt.title('Rendimentos')
  plt.xlabel('Rendimentos do valor inicial')
  plt.ylabel('prazo de rendimento')
  plt.show()

def calcular_juros():
  depositos = []
  prazos = []
  saldo = deposito
  mes = 1
  while mes <= prazo:
      saldo = saldo + (saldo * (taxa / 100)) + investimento
      print("Após %d períodos(s), o montante será de R$%5.2f" % (mes, saldo))
      mes += 1
      prazos.append(mes)
      depositos.append(saldo)
  print('===============================================')    
  print("Ao final do período o seu saldo é de R$%8.2f" % (saldo))
  print('===============================================')
  exibir_grafico(depositos, prazos)

try:
  deposito = float(input("Valor inicial: R$ "))
  taxa = float(input("Taxa de juros(%): "))
  investimento = float(input("Depósito mensal: R$ "))
  prazo = int( input('Período de rendimento: '))
except Exception as erro:
  print(f'Valor inválido! :( O erro aconteceu em {erro.__class__}.')
else:
  calcular_juros()
finally:
  print('')
  print('Obrigado! :) Volte Sempre.')