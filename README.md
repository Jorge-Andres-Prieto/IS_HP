# 🧾 Organizador de Informes Bancarios

### 🌐 [Haz clic aquí para ir a la App](https://proyecto-empresa.streamlit.app/)
<p align="center">
  <a href="https://proyecto-empresa.streamlit.app/">
    <img src="https://img.shields.io/badge/Organizador%20de%20Informes%20Bancarios-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Organizador de Informes Bancarios" style="vertical-align: middle;">
  </a>
</p>

## 🗂️ Tabla de Contenido
- [📄 Acerca de la Aplicación](#-acerca-de-la-aplicación)
- [⚙️ Cómo Funciona](#️-cómo-funciona)
- [💻 Uso de Tecnologías](#-uso-de-tecnologías)

## 📄 Acerca de la Aplicación

**Organizador de Informes Bancarios** es una aplicación desarrollada como parte del proyecto de la materia **Ingeniería de Software** de la **Universidad Nacional**. La app facilita la organización y procesamiento de datos de informes bancarios, permitiendo sumar valores de recibos y realizar búsquedas y filtros específicos en archivos Excel.

## ⚙️ Cómo Funciona

1. **Procesador de Excel**:
   - Asegúrate de que el archivo de Excel que deseas procesar contenga una hoja llamada **"CORRIENTE"**.
   - Esta hoja debe incluir las columnas **"RECIBO"** y **"VALOR"**, sin espacios, comas o puntos en los nombres de las columnas.
   - El procesador generará una **copia organizada** de los datos; **no modifica el documento original**.

2. **Sumar Datos**:
   - Para sumar los valores en el documento, verifica que las columnas **"RECIBO"** y **"VALOR"** sean de tipo **número**.

3. **Filtrar Información**:
   - Puedes buscar datos específicos ingresando la **sede** o el **método de pago** que deseas filtrar.
   - Asegúrate de utilizar el nombre exacto que aparece en el archivo.
   - Ejemplo: Para buscar consignaciones, ingresa **CONSIGNACION CORRESPONSAL CB**.

## 💻 Uso de Tecnologías

**Organizador de Informes Bancarios** utiliza las siguientes tecnologías:

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Openpyxl-000000?style=for-the-badge&logo=openpyxl&logoColor=white"/>
</p>
