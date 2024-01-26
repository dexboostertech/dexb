import streamlit as st
import requests

# Función para obtener datos de usuarios
def get_user_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    data = response.json()
    return data

# Interfaz de usuario con Streamlit
st.title('Información de Usuario')
user_id = st.text_input('Introduce el ID del usuario (1-10)')
if user_id:
    try:
        user_data = get_user_data(user_id)
        st.write(f"ID: {user_data['id']}")
        st.write(f"Nombre de usuario: {user_data['username']}")
        st.write(f"Nombre: {user_data['name']}")
        st.write(f"Email: {user_data['email']}")
        st.write(f"Teléfono: {user_data['phone']}")
    except Exception as e:
        st.write('Error al obtener datos del usuario. Por favor, introduce un ID válido (1-10).')

