import pandas as pd
import plotly.express as px

# codigo feito para rodar no google colab
# importando tabela e configurando idioma
tabela = pd.read_csv('ClientesBanco.csv', encoding='latin1')

# excluindo tabela irrelevante e conferido
tabela = tabela.drop('CLIENTNUM', axis=1)
display(tabela)

# tratando dados nulos e conferindo
tabela = tabela.dropna()
display(tabela.info())
# diminuindo casas decimais
display(tabela.describe().round(1))

# comparando a quantidade de clientes e cartoes cancelados
qtd = tabela['Categoria'].value_counts()
display(qtd)
# exibindo percentual
porcentagem = tabela['Categoria'].value_counts(normalize=True)
display(porcentagem)

# criando graficos de diagnosticos
for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color='Categoria')
  grafico.show()