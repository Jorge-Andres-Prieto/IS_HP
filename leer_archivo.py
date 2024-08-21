import streamlit as st
import pandas as pd
from io import BytesIO


# Función para procesar el archivo Excel
def procesar_excel(archivo):
    df = pd.read_excel(archivo)

    # Crear un DataFrame vacío para almacenar los datos procesados
    df_nuevo = pd.DataFrame(columns=df.columns)

    # Iterar sobre cada fila en el DataFrame original
    for index, row in df.iterrows():
        # Separar los recibos si hay más de uno en la misma celda
        recibos = str(row['RECIBO']).split('-')

        for recibo in recibos:
            # Crear una nueva fila con el recibo separado y la misma información
            nueva_fila = row.copy()
            nueva_fila['RECIBO'] = recibo.strip()  # Eliminar espacios en blanco si los hay
            df_nuevo = df_nuevo.append(nueva_fila, ignore_index=True)

    return df_nuevo


# Título de la aplicación
st.title("Procesador de Excel para RECIBOS y VALOR")

# Subir archivo
archivo_subido = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if archivo_subido is not None:
    # Procesar el archivo subido
    df_procesado = procesar_excel(archivo_subido)

    # Mostrar la tabla procesada
    st.write("Vista previa del archivo procesado:")
    st.write(df_procesado)

    # Botón para descargar el archivo procesado
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        df_procesado.to_excel(writer, index=False)
        writer.save()

    buffer.seek(0)

    st.download_button(
        label="Descargar archivo procesado",
        data=buffer,
        file_name='A' + archivo_subido.name,
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
