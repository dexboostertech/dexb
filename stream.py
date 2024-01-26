import streamlit as st
import requests

# Realizar la solicitud a la API
response = requests.get('https://open-api.dextools.io/free/v2/dex/arbitrum?sort=name&order=asc', 
                        headers={'accept': 'application/json', 'X-BLOBR-KEY': 'Kf8DMH7o176auOp0jD9YYHNnyqEzJc6P'})

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    results = data['data']['results']

    # Mostrar los datos en una tabla utilizando Streamlit
    st.write("Datos obtenidos de la API:")
    st.table(results)
else:
    st.write(f"Error al obtener los datos de la API. Código de estado: {response.status_code}")

