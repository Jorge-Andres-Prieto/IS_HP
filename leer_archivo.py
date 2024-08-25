import pandas as pd
import streamlit as st
from io import BytesIO
import openpyxl

def process_excel(uploaded_file):
    # Leer el archivo Excel
    df = pd.read_excel(uploaded_file)

    # Encontrar el índice de la columna 'RECIBO' (asumiendo que el nombre está en formato numérico)
    recibo_col = df.columns[df.columns.astype(str) == 'RECIBO'].tolist()[0]

    # Función para separar los valores de RECIBO y crear nuevas filas
    def split_recibos(row):
        recibos = str(row[recibo_col]).split('-')
        return pd.DataFrame([row.to_dict() | {'RECIBO': r} for r in recibos])

    # Aplicar la función a cada fila y concatenar los resultados
    new_df = pd.concat(df.apply(split_recibos, axis=1).tolist(), ignore_index=True)

    # Crear un buffer para guardar el nuevo DataFrame en Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        new_df.to_excel(writer, index=False)

    # Descargar el archivo
    output.seek(0)
    return output

def main():
    st.title("Separador de Recibos en Excel")

    uploaded_file = st.file_uploader("Selecciona un archivo Excel", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df.head())

        if st.button("Procesar archivo"):
            processed_data = process_excel(uploaded_file)
            st.download_button(
                label="Descargar archivo procesado",
                data=processed_data,
                file_name=f"A_{uploaded_file.name}"
            )

if __name__ == "__main__":
    main()