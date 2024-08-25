import pandas as pd
import streamlit as st

def separar_recibos(file):
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Verificar si la columna 'RECIBO' existe
    if 'RECIBO' not in df.columns:
        st.error("La columna 'RECIBO' no se encontró en el archivo.")
        return None

    # Crear una lista para almacenar los nuevos DataFrames
    new_dfs = []

    for index, row in df.iterrows():
        recibos = row['RECIBO'].split('-')
        for recibo in recibos:
            new_row = row.copy()
            new_row['RECIBO'] = recibo
            new_dfs.append(new_row)

    # Concatenar los nuevos DataFrames en uno solo
    new_df = pd.DataFrame(new_dfs)

    return new_df

def main():
    st.title("Separador de Recibos")

    uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        if st.button("Separar Recibos"):
            new_df = separar_recibos(uploaded_file)
            st.dataframe(new_df)

            # Crear el nombre del nuevo archivo
            new_filename = "A_" + uploaded_file.name

            # Descargar el nuevo archivo
            csv = new_df.to_csv(index=False)
            st.download_button(
                label="Descargar archivo modificado",
                data=csv,
                file_name=new_filename,
                mime='text/csv',
            )

if __name__ == "__main__":
    main()