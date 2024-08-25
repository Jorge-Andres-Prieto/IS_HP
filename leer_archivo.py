import pandas as pd
import streamlit as st

def separar_recibos(file):
    # Leer el archivo Excel
    df = pd.read_excel(file)

    # Verificar si la columna 'RECIBO' existe
    if 'RECIBO' not in df.columns:
        st.error("La columna 'RECIBO' no se encontró en el archivo.")
        return None

    # Resto del código...

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