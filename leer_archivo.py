import pandas as pd
import streamlit as st

def separar_recibos(file):
    """Separa los recibos en una nueva fila por cada valor de recibo.

    Args:
        file: El archivo Excel a procesar.

    Returns:
        Un nuevo DataFrame con los recibos separados, o None si no se encuentra la columna 'RECIBO'.
    """

    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Buscar la columna 'RECIBO' en cualquier posición
    try:
        recibo_col = df.columns[df.columns.str.contains('RECIBO', case=False)].tolist()[0]
    except IndexError:
        st.error("La columna 'RECIBO' no se encontró en el archivo.")
        return None

    # Crear una lista para almacenar los nuevos DataFrames
    new_dfs = []

    for index, row in df.iterrows():
        recibos = str(row[recibo_col]).split('-')
        for recibo in recibos:
            new_row = row.copy()
            new_row[recibo_col] = recibo
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

            if new_df is not None:
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
            else:
                st.error("No se pudo separar los recibos debido a la ausencia de la columna 'RECIBO'.")

if __name__ == "__main__":
    main()