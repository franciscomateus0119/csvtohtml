#Author: Francisco Mateus Rocha Filho
#Date: 03/02/2020 (3 de fevereiro de 2020)

""" Programa para transformar um arquivo em formato CSV para HTML e ordená-lo de acordo com o campo valor
# Para executar corretamente o programa, é necessário:
#   1 - A biblioteca pandas instalada
#   2 - O arquivo CSV deve estar na mesma pasta que o este arquivo python (ou seja, csv_to_html.py)
"""
#Importar as bibliotecas necessárias
import pandas as pd


#Realiza-se a leitura do arquivo .csv e o transforma em um dataframe(tabela no formato padrão do pandas)
#IMPORTANTE: A primeira linha do arquivo deve conter as colunas
"""
*filepath_or_buffer* : diretório do arquivo
"""
df = pd.read_csv('./pagamentos_sample.csv')

#Com o arquivo lido, transformamos a data no formato Ano-Mês-Dia para Ano-Mês
"""
*yearfirst* : True - a data está organizada no formato Yearfirst (ano primeiro)
              False -a data não está organizada no formato Yearfirst (ano primeiro)
*format* : indico o formato que a data deve ficar (neste caso, Ano/Mês)
apply(lambda x: x.strftime('%Y-%m') : formata os valores de data para que fiquem no formato 'YYYY-MM'   
"""
df['data'] = pd.to_datetime(df['data'], yearfirst=True, format='%Y/%m').apply(lambda x: x.strftime('%Y-%m'))

#Com a tabela data organizada para o formato Ano-Mês, ordenamos a tabela de forma que
#Data: Crescente / Valor: Decrescente
"""
*by* : coluna ou conjunto de colunas que contém os valores a serem trabalhados
*axis* : 0 - nomes ou lista de nomes no argumento *by* são considerados como nomes de colunas
         1 = nomes ou lista de nomes no argumento *by* são considerados como nomes de linhas
*ascending* : True - valores organizados em ordem ascendente.
              False - valores organizados em ordem decrescente
*inplace* : True - a função altera o dataframe sem retorná-lo (ou seja, como se não existisse 'return dataframe'
            False - a função altera o dataframe e o retorna
*kind* : método de ordenação utilizado para organizar os valores.
*na_position* : first - valores NaN (not a number) são colocados no começo
                last - valores NaN são colocados no final
"""
df = df.sort_values(by=['data','valor'], axis=0, ascending=[True,False], inplace=False, kind='quicksort', na_position='last')


#Finalizadas as operações, o arquivo é transformado para o formato html
"""
*buf* : diretório e nome do arquivo final
*index* : True - mantém a coluna index auto-gerado devido a transformação de csv --> pandas.dataframe
          False - remove a coluna index
"""
df.to_html('./pagamentos_sample.html', index=False)
