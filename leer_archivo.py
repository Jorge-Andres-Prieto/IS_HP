import pandas as pd
from openpyxl import load_workbook
import streamlit as st

def process_excel_file(file):
    # Cargar el archivo de Excel
    wb = load_workbook(file)
    ws = wb['Corriente']

    # Crear un DataFrame solo con la columna 'RECIBO'
    df_recibos = pd.DataFrame(ws['RECIBO'])

    # Convertir la columna a string y dividir los valores
    df_recibos['RECIBO'] = df_recibos['RECIBO'].astype(str).str.split('-')

    # Crear un nuevo DataFrame para almacenar los recibos individuales
    df_new = pd.DataFrame(df_recibos['RECIBO'].explode())

    # Crear un nuevo nombre de archivo
    new_filename = 'A' + file.name

    # Guardar el nuevo DataFrame en un archivo de Excel
    with pd.ExcelWriter(new_filename, engine='openpyxl') as writer:
        df_new.to_excel(writer, index=False, header=['RECIBO'])

    # Descargar el archivo
    with open(new_filename, "rb") as f:
        st.download_button(
            label="Descargar archivo procesado",
            data=f,
            file_name=new_filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Interfaz de usuario de Streamlit
st.title("Procesador de Excel")

uploaded_file = st.file_uploader("Sube tu archivo de Excel", type=["xlsx"])

if uploaded_file is not None:
    process_excel_file(uploaded_file)