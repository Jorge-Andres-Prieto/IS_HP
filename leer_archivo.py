import pandas as pd
import streamlit as st
from io import BytesIO


# Función para procesar el archivo de Excel
def procesar_excel(archivo):
    # Leer el archivo de Excel
    df = pd.read_excel(archivo, sheet_name='CORRIENTE')

    # Crear una lista para almacenar los datos procesados
    filas = []

    # Iterar sobre cada fila del DataFrame original
    for index, row in df.iterrows():
        # Verificar si hay dos recibos en la columna 'RECIBO'
        recibos = str(row['RECIBO']).split('-')
        for recibo in recibos:
            nueva_fila = row.copy()
            nueva_fila['RECIBO'] = recibo
            filas.append(nueva_fila)

    # Crear un nuevo DataFrame a partir de la lista de filas
    nuevo_df = pd.DataFrame(filas)

    return nuevo_df


# Función para descargar el archivo modificado
def descargar_excel(df, nombre_archivo):
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    buffer.seek(0)
    return buffer


# Interfaz de Streamlit
st.title('Procesador de Recibos')

# Subir el archivo de Excel
archivo_subido = st.file_uploader('Sube tu archivo de Excel', type=['xlsx'])

if archivo_subido:
    # Procesar el archivo
    df_procesado = procesar_excel(archivo_subido)

    # Mostrar el DataFrame procesado en la app
    st.write('Archivo procesado:')
    st.dataframe(df_procesado)

    # Descargar el archivo modificado
    nombre_archivo = 'A' + archivo_subido.name
    buffer = descargar_excel(df_procesado, nombre_archivo)
    st.download_button(label='Descargar archivo modificado', data=buffer, file_name=nombre_archivo,
                       mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
