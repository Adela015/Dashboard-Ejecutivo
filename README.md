# 📊 Dashboard Ejecutivo Interactivo

Dashboard web interactivo desarrollado con Streamlit para visualización de datos de ventas, clientes y análisis de performance empresarial en tiempo real.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Características

- **📈 Métricas en tiempo real**: Visualización de KPIs clave (ventas totales, clientes activos, promedios, ROI)
- **📊 Gráficos interactivos**: 
  - Gráfico de líneas para evolución de ventas mensuales
  - Gráfico de torta para distribución de clientes por región
- **🔍 Filtros dinámicos**: Selección por mes y región en barra lateral
- **📱 Diseño responsivo**: Interfaz adaptable a diferentes tamaños de pantalla
- **🎨 Tema oscuro**: Visualizaciones con estética profesional

## 🖼️ Vista Previa

El dashboard incluye:
- 4 tarjetas de métricas principales
- Gráfico de evolución temporal de ventas
- Distribución geográfica de clientes
- Panel de filtros interactivos

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona el repositorio** (o descarga los archivos)
```bash
git clone https://github.com/tu-usuario/dashboard-ejecutivo.git
cd dashboard-ejecutivo
```

2. **Crea un entorno virtual** (recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

## 📦 Dependencias

Crea un archivo `requirements.txt` con el siguiente contenido:

```txt
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
```

## 💻 Uso

1. **Ejecuta la aplicación**
```bash
streamlit run dashboard.py
```

2. **Abre tu navegador**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre, copia y pega la URL que aparece en la terminal

3. **Interactúa con el dashboard**
   - Observa las métricas principales en las tarjetas superiores
   - Explora los gráficos interactivos
   - Utiliza los filtros en la barra lateral para segmentar los datos

## 📁 Estructura del Proyecto

```
dashboard-ejecutivo/
│
├── dashboard.py          # Archivo principal de la aplicación
├── requirements.txt      # Dependencias del proyecto
├── README.md            # Este archivo
└── .gitignore           # Archivos a ignorar en git
```

## 🎨 Personalización

### Modificar los Datos

Los datos se encuentran en el diccionario `data` dentro del archivo `dashboard.py`:

```python
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': [45000, 52000, 48000, 61000, 58000, 67000],
    'Clientes': [120, 145, 133, 167, 156, 189],
    'Región': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Norte']
}
```

### Cambiar Colores

Para modificar el tema del gráfico, edita la línea:
```python
fig.update_layout(template = 'plotly_dark')
```

Opciones disponibles: `plotly`, `plotly_white`, `plotly_dark`, `ggplot2`, `seaborn`, `simple_white`

### Agregar Nuevas Métricas

Crea nuevas columnas usando `st.columns()` y agrega métricas con `st.metric()`:
```python
with col5:
    st.metric("Tu Métrica", "Valor", "Cambio%")
```

## 📊 Datos de Ejemplo

El dashboard utiliza datos de ejemplo que incluyen:
- **6 meses** de información (Enero - Junio)
- **Ventas** por mes
- **Número de clientes** mensuales
- **3 regiones**: Norte, Sur, Centro

Para usar datos reales, reemplaza el diccionario `data` con:
- Lectura de archivos CSV: `pd.read_csv('datos.csv')`
- Conexión a bases de datos
- APIs externas

## 🛠️ Tecnologías Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para crear aplicaciones web de datos
- **[Pandas](https://pandas.pydata.org/)**: Manipulación y análisis de datos
- **[Plotly](https://plotly.com/)**: Visualizaciones interactivas
