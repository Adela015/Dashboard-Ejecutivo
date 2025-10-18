# ===== IMPORTACIÓN DE BIBLIOTECAS =====
# Estas son las herramientas que necesitamos para que el programa funcione

from re import template  # Esta línea no se usa en el código, probablemente quedó de pruebas anteriores
import streamlit as st  # Streamlit: biblioteca para crear aplicaciones web interactivas
import pandas as pd  # Pandas: biblioteca para trabajar con tablas de datos
import plotly.express as px  # Plotly Express: biblioteca para crear gráficos interactivos de forma simple
import plotly.graph_objects as go  # Plotly Graph Objects: biblioteca para crear gráficos más personalizados

# ===== CONFIGURACIÓN DE LA PÁGINA WEB =====
# Aquí definimos cómo se verá nuestra aplicación web
st.set_page_config(page_title = "My Dashboard",  # Título que aparece en la pestaña del navegador
                   layout = "wide",  # Hace que el contenido ocupe todo el ancho de la pantalla
                   page_icon = "📊")  # Ícono que aparece en la pestaña del navegador

# ===== CREACIÓN DE DATOS DE EJEMPLO =====
# Creamos un diccionario (como una tabla) con información de ventas
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],  # Lista de meses
    'Ventas': [45000, 52000, 48000, 61000, 58000, 67000],  # Cantidad de ventas en cada mes
    'Clientes': [120, 145, 133, 167, 156, 189],  # Número de clientes en cada mes
    'Región': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Norte']  # Región de donde provienen las ventas
}

# ===== CONVERTIR LOS DATOS EN UN DATAFRAME =====
# Un DataFrame es como una tabla de Excel que podemos manipular fácilmente
df = pd.DataFrame(data)

# ===== TÍTULO Y SUBTÍTULO DEL DASHBOARD =====
st.title("📊 Dashboard Ejecutivo")  # Título principal grande
st.markdown("### Análisis en Tiempo Real de Performance")  # Subtítulo (los ### hacen que sea más pequeño)

# ===== CREACIÓN DE TARJETAS DE MÉTRICAS =====
# Dividimos la pantalla en 4 columnas para mostrar 4 indicadores importantes
col1, col2, col3, col4 = st.columns(4)

# COLUMNA 1: Muestra las ventas totales
with col1:
    # st.metric crea una tarjeta con un número grande y un pequeño cambio porcentual
    # df['Ventas'].sum() suma todas las ventas
    # f"${...:,}" formatea el número con comas (ejemplo: 331,000)
    st.metric("Ventas Totales", f"${df['Ventas'].sum():,}", "12%")

# COLUMNA 2: Muestra el total de clientes
with col2:
    # df['Clientes'].sum() suma todos los clientes
    st.metric("Clientes Activos", df['Clientes'].sum(), "23") 
    
# COLUMNA 3: Muestra el promedio de ventas mensuales
with col3:
    # df['Ventas'].mean() calcula el promedio de ventas
    # :.0f formatea el número sin decimales
    st.metric("Promedio Mensual", f"${df['Ventas'].mean():.0f}", "8%")

# COLUMNA 4: Muestra el ROI (Return on Investment - Retorno de Inversión)
with col4:
    st.metric("ROI", "245%", "15%")   
    
# ===== GRÁFICO DE LÍNEAS: EVOLUCIÓN DE VENTAS =====
# Creamos un gráfico de líneas para ver cómo cambian las ventas mes a mes
fig = px.line(df, x = 'Mes', y = 'Ventas',  # x = eje horizontal (meses), y = eje vertical (ventas)
              title = 'Evolución de Ventas Mensuales',  # Título del gráfico
              markers = True)  # markers = True agrega puntos en cada valor
fig.update_layout(template = 'plotly_dark')  # Aplica un tema oscuro al gráfico

# Muestra el gráfico en la página, use_container_width hace que ocupe todo el ancho disponible
st.plotly_chart(fig, use_container_width = True)

# ===== GRÁFICO DE TORTA: DISTRIBUCIÓN DE CLIENTES =====
# Creamos un gráfico circular para ver qué porcentaje de clientes hay en cada región
fig2 = px.pie(df, values='Clientes', names='Región',  # values = tamaño de cada porción, names = etiquetas
              title='Distribución de Clientes por Región')

# Muestra el gráfico de torta en la página
st.plotly_chart(fig2, use_container_width = True)

# ===== BARRA LATERAL CON FILTROS INTERACTIVOS =====
# La barra lateral (sidebar) aparece a la izquierda de la pantalla

# FILTRO 1: Selector de mes
# st.sidebar.selectbox crea una lista desplegable donde el usuario puede elegir un mes
mes_seleccionado = st.sidebar.selectbox("Selecciona un mes:", df['Mes'])

# FILTRO 2: Selector múltiple de regiones
# st.sidebar.multiselect permite seleccionar varias opciones a la vez
# df['Región'].unique() obtiene todas las regiones sin repetir
region_filtro = st.sidebar.multiselect("Filtrar por región:", df['Región'].unique())

# ===== MOSTRAR DATOS FILTRADOS =====
# Si el usuario seleccionó al menos una región en el filtro
if region_filtro:
    # Filtramos el DataFrame para mostrar solo las filas de las regiones seleccionadas
    # df['Región'].isin(region_filtro) verifica qué filas tienen las regiones seleccionadas
    datos_filtrados = df[df['Región'].isin(region_filtro)]
    # Mostramos la tabla filtrada en la pantalla
    st.dataframe(datos_filtrados, use_container_width=True)
