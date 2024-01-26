import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Crear desplegable para que el usuario elija la red
network = st.selectbox('Selecciona la red', ('Ethereum', 'Polygon', 'Arbitrum'))

# Definir la URL base y la red elegida por el usuario
base_url = 'https://open-api.dextools.io/free/v2/dex/'
if network == 'Ethereum':
    network_url = 'ethereum'
elif network == 'Polygon':
    network_url = 'polygon'
else:  # Si la red elegida es Arbitrum
    network_url = 'arbitrum'

# Crear la URL final para la solicitud a la API
url = base_url + network_url + '?sort=name&order=asc'

# Realizar la solicitud a la API
response = requests.get(url, headers={'accept': 'application/json', 'X-BLOBR-KEY': 'Kf8DMH7o176auOp0jD9YYHNnyqEzJc6P'})

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    results = data['data']['results']
    
    # Crear un DataFrame con los resultados
    df = pd.DataFrame(results)
    
    # Crear el gráfico de barras con el valor de volume24h
    st.write("Gráfico de Barras - Volumen (24h)")
    fig, ax = plt.subplots()
    ax.bar(df['name'], df['volume24h'])
    plt.xticks(rotation=90)
    st.pyplot(fig)
else:
    st.write(f"Error al obtener los datos de la API. Código de estado: {response.status_code}")
