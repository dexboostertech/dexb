import streamlit as st
import requests
import pandas as pd

# Realizar la solicitud a la API
response = requests.get('https://open-api.dextools.io/free/v2/dex/arbitrum?sort=name&order=asc', 
                        headers={'accept': 'application/json', 'X-BLOBR-KEY': 'Kf8DMH7o176auOp0jD9YYHNnyqEzJc6P'})

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    results = data['data']['results']

    # Crear un DataFrame con los resultados
    df = pd.DataFrame(results)

    # Agrupar por "name" y sumar los volúmenes
    grouped_df = df.groupby('name')['volume24h'].sum().reset_index()

    # Mostrar los datos agrupados en una tabla utilizando Streamlit
    st.write("Datos agrupados por 'name' y sumando los volúmenes:")
    st.table(grouped_df)

    # Crear un gráfico de barras del volumen por "name"
    st.bar_chart(grouped_df.set_index('name')['volume24h'])
else:
    st.write(f"Error al obtener los datos de la API. Código de estado: {response.status_code}")
