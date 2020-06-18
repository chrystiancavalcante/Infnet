def diagnosticar_orcamento_mensal(renda_mensal, gasto_com_moradia, gasto_com_educacao, gasto_com_transporte):
  diagnostico = '\n'
  moradia = renda_mensal * 30/100
  educacao = renda_mensal * 20/100
  transporte = renda_mensal * 15/100
  renda_comprometida_moradia = (gasto_com_moradia / renda_mensal) * 100
  renda_comprometida_educacao = (gasto_com_educacao / renda_mensal) * 100
  renda_comprometida_transporte = (gasto_com_transporte / renda_mensal) * 100

  if gasto_com_moradia <= moradia:
    diagnostico += f'Seus gastos totais com moradia comprometem {renda_comprometida_moradia:.2f}% de sua renda total.\n O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada.\n\n'
  else:
    diagnostico += f'Seus gastos totais com moradia comprometem {renda_comprometida_moradia:.2f}% de sua renda total.\n O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {moradia:.2f}.\n\n '
  if gasto_com_educacao <= educacao:
    diagnostico += f'Seus gastos totais com educação comprometem {renda_comprometida_educacao:.2f}% de sua renda total.\n O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada.\n\n'
  else:
    diagnostico += f'Seus gastos totais com educação comprometem {renda_comprometida_educacao:.2f}% de sua renda total.\n O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {educacao:.2f}.\n\n'  
  if gasto_com_transporte <= transporte:
    diagnostico += f'Seus gastos totais com transporte comprometem {renda_comprometida_transporte:.2f}% de sua renda total.\n O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada.\n'
  else:
    diagnostico += f'Seus gastos totais com transporte comprometem {renda_comprometida_transporte:.2f}% de sua renda total.\n O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {transporte:.2f}.\n\n' 
  return diagnostico

try:
  renda_mensal = float(input('Renda mensal total: R$ '))
  gasto_com_moradia = float(input('Gastos totais com moradia: R$ '))
  gasto_com_educacao = float(input('Gastos totais com educação: R$ '))
  gasto_com_transporte = float(input('Gastos totais com transporte: R$ '))
except Exception as erro:
  print(f'Valor inválido! :( O erro ocorreu em {erro.__class__}.')
else:  
  diagnostico = diagnosticar_orcamento_mensal(renda_mensal, gasto_com_moradia, gasto_com_educacao, gasto_com_transporte)
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
  print(diagnostico)
  print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
finally:
  print('Obrigado! :) Volte Sempre.')
