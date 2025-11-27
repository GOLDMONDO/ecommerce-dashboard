# Procedimiento Completo: Generación de Datos y Ejecución del Dashboard de Streamlit

## 1. Preparación del Entorno

*   **Asegúrate de tener Python instalado** en tu sistema.
*   **Crea o activa tu entorno virtual de Python** (opcional pero recomendado para aislar dependencias).
*   **Instala las bibliotecas necesarias**. Abre una terminal (puedes usar la de PyCharm) en la carpeta del proyecto y ejecuta:
    ```bash
    pip install streamlit pandas plotly
    ```
    *   `streamlit`: Para crear el dashboard interactivo.
    *   `pandas`: Para manipulación de datos.
    *   `plotly`: Para generar gráficos interactivos.

## 2. Estructura del Proyecto

Asegúrate de que tu carpeta `ecommerce-dashboard` contenga los siguientes archivos (o nombres similares):

*   `generate_data.py` (o `generador_datos.py`, etc.): Script para generar los datos de ejemplo.
*   `dashboard_802.py` (o `app.py`, `main.py`, etc.): Script principal de Streamlit que crea el dashboard.
*   `sales_data_800.csv` (Este archivo se generará **después** de correr `generate_data.py`).

## 3. Generación de Datos

1.  Abre la **Terminal integrada de PyCharm** (`View` -> `Tool Windows` -> `Terminal`).
2.  Asegúrate de que el **directorio de trabajo** sea la carpeta de tu proyecto (`ecommerce-dashboard`). La línea de comandos debe terminar con `ecommerce-dashboard>`.
3.  Ejecuta el script de generación de datos:
    ```bash
    python generate_data.py
    ```
    *   Asegúrate de reemplazar `generate_data.py` con el **nombre exacto** de tu archivo de generación de datos.
    *   Este proceso creará (o sobrescribirá) el archivo `sales_data_800.csv` en la misma carpeta.
4.  Verifica que el archivo `sales_data_800.csv` se haya generado correctamente y contenga datos.

## 4. Ejecución del Dashboard de Streamlit

1.  **Manteniéndote en la misma terminal** del paso anterior (asegurándote de estar en la carpeta `ecommerce-dashboard`).
2.  Ejecuta el script de Streamlit:
    ```bash
    streamlit run dashboard_802.py
    ```
    *   Asegúrate de reemplazar `dashboard_802.py` con el **nombre exacto** de tu archivo principal de Streamlit.
3.  El servidor de Streamlit iniciará y **debería abrirse automáticamente una pestaña en tu navegador web** con la URL `http://localhost:8501`.
4.  **¡Listo!** Ahora puedes interactuar con tu dashboard. Si aplicaste la corrección para el eje X, verás que el gráfico de "Ventas Diarias" abarca todo el rango de fechas del archivo (por ejemplo, enero a diciembre de 2024), mostrando valores de 0 para los días sin ventas (como noviembre y diciembre si no hay datos para esas fechas en el archivo CSV).

## 5. Posibles Errores y Soluciones

*   **Error de extensión:** Asegúrate de que los comandos `python nombre_archivo.py` o `streamlit run nombre_archivo.py` usen el **nombre exacto** del archivo, incluyendo la extensión `.py`.
*   **No se abre navegador:** Copia la URL `http://localhost:8501` (o similar) que aparece en la consola de PyCharm y pégala en tu navegador.
*   **No encuentra 'streamlit':** Asegúrate de haber instalado `streamlit` en tu entorno (`pip install streamlit`).
*   **No encuentra 'sales_data_800.csv':** Asegúrate de haber corrido `generate_data.py` antes de `dashboard_802.py`, y que ambos archivos estén en la misma carpeta.
*   **Avisos de `use_container_width`:** Son avisos de deprecación. Puedes ignorarlos temporalmente o actualizar tu código cambiando `use_container_width=True` por `width='stretch'` en las líneas de `st.plotly_chart()`.
*   **Asegurarnos de que la terminal de PyCharm se abra directamente en la carpeta de tu proyecto actual (`ecommerce-dashboard`). Esto facilitará la ejecución de comandos como `streamlit run dashboard_802.py`.

Sigue estos pasos:

1.  **Abre PyCharm** y asegúrate de tener abierto el proyecto correcto (`ecommerce-dashboard`).
2.  **Ve al menú `File` (Archivo)`.**
3.  Selecciona `Settings` (Configuración) (en Windows/Linux) o `PyCharm` -> `Preferences` (Preferencias) (en macOS).
4.  En la ventana de configuración que se abre, busca en el panel izquierdo la opción `Tools` (Herramientas).
5.  Dentro de `Tools`, selecciona `Terminal`.
6.  En el panel derecho, busca la sección **"Shell path"**.
7.  **Importante:** Busca una casilla de verificación que dice **"Shell integration"** o algo similar como **"Start directory:"** o una opción relacionada con el directorio inicial. Lo que buscas es una opción que diga **"Start directory: Project Directory"** o **"Start directory: [Carpeta de tu proyecto]"**. Si no está seleccionada, **actívala**. A veces dice "Start directory: Project Root" o "Start directory: [Variable] $ProjectFileDir$". La idea es que esté configurada para usar la carpeta del proyecto.
8.  **Haz clic en `OK`** para guardar los cambios.
9.  **Cierra y vuelve a abrir** la terminal integrada de PyCharm. Puedes hacerlo cerrando la pestaña/panel de la terminal actual y luego yendo a `View` -> `Tool Windows` -> `Terminal` de nuevo.

**Después de aplicar esta configuración:**

*   Cada vez que abras la terminal integrada de PyCharm, **debería abrirse automáticamente en la carpeta raíz de tu proyecto actual**.
*   En la línea de comandos de la terminal, deberías ver la ruta de tu carpeta `ecommerce-dashboard` (por ejemplo, `(venv) C:\Users\xxxxxxxxxxx\PycharmProjects\RemoteJobGo\Github Raíz\ecommerce-dashboard>`).

Con la terminal en la carpeta correcta, puedes ejecutar el comando `streamlit run dashboard_802.py` directamente.