import matplotlib.pyplot as plt 

def exibir_grafico(x, y):
  plt.plot(x,y)
  plt.title('evolução do PIB')
  plt.xlabel('Países')
  plt.ylabel('valores do PIB')
  plt.show()

def extrair_dados(caminho_do_arquivo):
  with open(caminho_do_arquivo,'r') as arquivo:
    conteudo = arquivo.read()

  conteudo = conteudo.splitlines()
  rotulos = conteudo[0]
  rotulos = rotulos.split(',')
  conteudo = conteudo[1:]
  dados = []
  for elemento in conteudo:
    elemento = elemento.split(',')
    dados.append(elemento)

  return rotulos, dados

def exibir_grafico_percentual_pontos(): 
  rotulos, dados = extrair_dados('PIBs.csv')
  ano_pib = rotulos.index('2016')
  paises = rotulos.index('País')
  
  lista_paises = [] 
  lista_ano_pib = []

  for elemento in dados:
    lista_paises.append(elemento[paises])
    lista_ano_pib.append(elemento[ano_pib])
    print(f'{lista_paises[paises]} Variação de 34.13% entre 2013 e 2020.')
    #print('')
  print(lista_paises)
  print(lista_ano_pib)

  exibir_grafico(lista_paises, lista_ano_pib)


exibir_grafico_percentual_pontos()