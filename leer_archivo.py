import streamlit as st
import pandas as pd
import openpyxl


def process_excel_file(uploaded_file):
    # Leer el archivo de Excel
    df = pd.read_excel(uploaded_file, sheet_name='CORRIENTE')

    # Crear una lista para almacenar los nuevos dataframes
    new_dfs = []

    # Iterar sobre cada fila
    for index, row in df.iterrows():
        recibos = str(row['RECIBO']).split('-')
        valores = None

        # Si la celda en 'VALOR' contiene una fórmula
        if isinstance(row['VALOR'], str) and '-' in row['VALOR']:
            valores = row['VALOR'].split('-')

        for i, recibo in enumerate(recibos):
            new_row = row.copy()
            new_row['RECIBO'] = recibo

            # Asignar el valor correcto a la nueva fila
            if valores:
                if i < len(valores):
                    new_row['VALOR'] = valores[i]
                else:
                    new_row['VALOR'] = valores[-1]  # Usar el último valor si hay menos valores que recibos
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
