import streamlit as st
import pandas as pd
import openpyxl


def evaluate_formula(formula):
    # Evaluar la fórmula para obtener el resultado numérico
    return eval(formula)


def process_excel_file(uploaded_file):
    # Leer el archivo de Excel
    df = pd.read_excel(uploaded_file, sheet_name='CORRIENTE')

    # Crear una lista para almacenar los nuevos dataframes
    new_dfs = []

    # Iterar sobre cada fila
    for index, row in df.iterrows():
        recibos = str(row['RECIBO']).split('-')
        valor = row['VALOR']

        # Verificar si el valor es una fórmula y procesarla
        if isinstance(valor, str) and valor.startswith('='):
            # Quitar el signo '=' y separar la fórmula en base a '+' o '-'
            if '+' in valor:
                operandos = valor[1:].split('+')
            elif '-' in valor:
                operandos = valor[1:].split('-')
            else:
                operandos = [valor[1:]]

            # Evaluar los operandos
            operandos = [evaluate_formula(op.strip()) for op in operandos]
        else:
            operandos = [valor]

        # Asegurar que tenemos suficientes valores para asignar a los recibos
        while len(operandos) < len(recibos):
            operandos.append(0)  # O algún otro valor por defecto

        # Crear nuevas filas con los recibos y valores correspondientes
        for i, recibo in enumerate(recibos):
            new_row = row.copy()
            new_row['RECIBO'] = recibo
            new_row['VALOR'] = operandos[i] if i < len(operandos) else operandos[-1]
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
