import pandas as pd
from openpyxl import load_workbook
import streamlit as st

def process_excel_file(file):
    # Cargar el archivo de Excel
    wb = load_workbook(file)
    ws = wb['Corriente']

    # Crear un nuevo DataFrame para almacenar los datos procesados
    df = pd.DataFrame(ws.values, columns=ws[1])

    # Convertir la columna 'RECIBO' a string para facilitar el procesamiento
    df['RECIBO'] = df['RECIBO'].astype(str)

    # Función para dividir los números de recibo y crear nuevas filas
    def split_recibos(row):
        recibos = row['RECIBO'].split('-')
        return pd.DataFrame([row.to_dict() | {'RECIBO': recibo}] for recibo in recibos)

    # Aplicar la función a cada fila y concatenar los resultados
    df = pd.concat(df.apply(split_recibos, axis=1).tolist(), ignore_index=True)

    # Crear un nuevo nombre de archivo
    new_filename = 'A' + file.name

    # Guardar el nuevo DataFrame en un archivo de Excel
    with pd.ExcelWriter(new_filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

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