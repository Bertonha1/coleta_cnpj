#%%
import time
import pandas as pd
import requests

df = pd.read_csv("cnpjs.csv")
# %%
def consulta_cnpj(cnpj):
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'Erro {response.status_code}'}
    except Exception as e:
        return {'error': str(e)}
    
# %%
dados_enriquecidos = []
for cnpj in df:
    print(f"Consultando CNPJ: {cnpj}")
    info = consulta_cnpj(cnpj)
    dados_enriquecidos.append(info)
     # Respeitar o limite de requisições (evitar sobrecarregar a API)
    time.sleep(1)  # Pausa de 1 segundo entre as consultas
# %%
#converter essa lista dos dados em um data frame
df_enriquecido = pd.DataFrame(dados_enriquecidos)
df_resultado = pd.concat([df.reset_index(drop=True), df_enriquecido], axis=1)
df_resultado

# %%
