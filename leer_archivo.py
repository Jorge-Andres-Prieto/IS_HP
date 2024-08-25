import streamlit as st
import pandas as pd
import openpyxl
import re


def process_excel_file(uploaded_file):
    # Leer el archivo de Excel
    df = pd.read_excel(uploaded_file, sheet_name='CORRIENTE')

    # Crear una lista para almacenar los nuevos dataframes
    new_dfs = []

    # Iterar sobre cada fila
    for index, row in df.iterrows():
        recibos = str(row['RECIBO']).split('-')

        # Verificar si la columna VALOR contiene una fórmula con operaciones matemáticas
        if isinstance(row['VALOR'], str) and re.match(r"^=[\d+\-\*/]+$", row['VALOR']):
            # Extraer los números de la fórmula
            valores = re.findall(r'\d+', row['VALOR'])
            if len(valores) == len(recibos):
                for i, recibo in enumerate(recibos):
                    new_row = row.copy()
                    new_row['RECIBO'] = recibo
                    new_row['VALOR'] = valores[i]
                    new_dfs.append(new_row)
            else:
                # Si no coincide la cantidad de recibos con los valores, usar el valor completo
                for recibo in recibos:
                    new_row = row.copy()
                    new_row['RECIBO'] = recibo
                    new_dfs.append(new_row)
        else:
            for recibo in recibos:
                new_row = row.copy()
                new_row['RECIBO'] = recibo
                new_dfs.append(new_row)

    # Concatenar los nuevos dataframes en uno solo
    new_df = pd.DataFrame(new_dfs)

    # Crear un nuevo nombre de archivo
    file_name = uploaded_file.name
    new_file_name = "A" + file_name

    # Guardar el nuevo dataframe en un nuevo archivo de Excel
    with pd.ExcelWriter(new_file_name) as writer:
        new_df.to_excel(writer, sheet_name='CORRIENTE', index=False)

    # Descargar el archivo
    with open(new_file_name, "rb") as f:
        st.download_button(
            label="Descargar archivo procesado",
            data=f,
            file_name=new_file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


# Interfaz de usuario de Streamlit
st.title("Procesador de Excel")

uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    process_excel_file(uploaded_file)
