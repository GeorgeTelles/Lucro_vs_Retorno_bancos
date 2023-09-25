"""
Esse codigo é um modelo de investimentos que analisa se o lucro dos bancos acompanha o crescimento do mesmo
na bolsa de valores, ou seja, o banco que mais lucrou foi o que mais cresceu de valor na bolsa de valores?

By: George Telles
+55 11 93290-7425
"""


import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


dados_bancarios = yf.download(["ITUB4.SA","BBAS3.SA", "SANB4.SA", "BBDC4.SA", "^BVSP"], start = "2010-01-01", end = "2023-08-01")["Adj Close"]

lucros_bancos = pd.read_excel("G:/Meu Drive/2. Documentos/dock/Finance/lucro bancos.xlsx", index_col = "data")

itau = dados_bancarios["ITUB4.SA"]
bancobrasil = dados_bancarios["BBAS3.SA"]
santander = dados_bancarios["SANB4.SA"]
bradesco = dados_bancarios["BBDC4.SA"]
ibov = dados_bancarios["^BVSP"]

def retorno(lista):
    retorno = lista[-10]/lista[0] -1
    return retorno

retorno_itau = retorno(itau)
retorno_bancobrasil = retorno(bancobrasil)
retorno_santander = retorno(santander)
retorno_bradesco = retorno(bradesco)
retorno_ibov = retorno(ibov)

retorno_itau, retorno_bancobrasil, retorno_santander, retorno_bradesco, retorno_ibov

df_retornos = pd.DataFrame(data = {"retornos": [retorno_itau, retorno_bancobrasil, retorno_santander, retorno_bradesco, retorno_ibov]}, index = ["Itau", "Banco_do_brasil", "Bradesco", "Santander", "Ibovespa"])

df_retornos["retornos"] = df_retornos["retornos"] * 100

df_retornos = df_retornos.sort_values("retornos", ascending=False)

var_lucro_bancos = lucros_bancos.iloc[-1]/lucros_bancos.iloc[0] - 1

var_lucro_bancos = var_lucro_bancos * 100

var_lucro_bancos = var_lucro_bancos.sort_values(ascending=False)


fig, ax = plt.subplots()

ax.bar(df_retornos.index, df_retornos["retornos"])
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.xticks(fontsize=9)
plt.title('Retorno dos Bancos', fontsize=14)  # Adicione um título a esta figura


#plt.show()

fig, ax = plt.subplots()

ax.bar(var_lucro_bancos.index, var_lucro_bancos)
ax.yaxis.set_major_formatter(mtick.PercentFormatter())

plt.xticks(fontsize=9)
plt.title('Lucro dos Bancos', fontsize=14)  # Adicione um título a esta figura


plt.show()







