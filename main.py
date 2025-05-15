import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("USD_BRL_hist.csv") 
df['Data'] = pd.to_datetime(df['Data'], format='%d.%m.%Y')
df = df.sort_values('Data')

plt.figure(figsize=(10, 5))
plt.plot(df['Data'], df['USD_BRL'], color='blue')
plt.title('Cotação do Dólar ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Dólar (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df['USD_BRL'], bins=20, color='orange', edgecolor='black')
plt.title('Distribuição das Cotações do Dólar')
plt.xlabel('Faixas de Cotação (R$)')
plt.ylabel('Frequência')
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
plt.scatter(df['Data'], df['USD_BRL'], color='green', alpha=0.6)
plt.title('Dispersão das Cotações por Data')
plt.xlabel('Data')
plt.ylabel('Dólar (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()