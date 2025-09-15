# Analizador de Tiempo de Respuesta

El `ResponseTimeAnalyzer` es una herramienta diseñada para analizar datos de tiempo de respuesta, proporcionando información sobre la distribución y diferencias entre dos conjuntos de datos. Incluye funcionalidades para limpiar datos, describir métricas del conjunto de datos y probar hipótesis sobre los tiempos de respuesta.

## Características

- **Limpieza de Datos**: Elimina valores atípicos de los conjuntos de datos que difieren más de 2 desviaciones estándar de la media.
- **Descripción del Conjunto de Datos**: Describe las métricas del conjunto de datos como la mediana, tamaño, promedio, mínimo, máximo y desviación estándar.
- **Pruebas de Hipótesis**: Prueba la hipótesis sobre las diferencias de tiempo de respuesta utilizando pruebas estadísticas adecuadas.

## Uso

1. **Inicialización**: Crea una instancia de `ResponseTimeAnalyzer` pasando dos objetos Series de pandas que representan los conjuntos de datos a analizar.
   ```python
   analyzer = ResponseTimeAnalyzer(pp_data, pia_data)
   ```

2. **Análisis**: Llama al método `analyze` para realizar un análisis completo, que incluye limpiar los conjuntos de datos, describirlos y analizar la hipótesis.
   ```python
   analyzer.analyze()
   ```

## Métodos

- `clean_datasets()`: Limpia los conjuntos de datos eliminando valores atípicos.
- `describe_datasets()`: Imprime una descripción de los conjuntos de datos.
- `analyze_response_time_hypothesis()`: Analiza la hipótesis utilizando la prueba estadística adecuada.

## Pruebas Estadísticas

- **Prueba de Shapiro-Wilk**: Prueba la normalidad de los conjuntos de datos.
- **Prueba T**: Se utiliza si ambos conjuntos de datos son distribuidos normalmente.
- **Prueba de Mann-Whitney U**: Se utiliza si uno o ambos conjuntos de datos no son distribuidos normalmente.

## Dependencias

- `pandas`
- `numpy`
- `scipy`
- `tabulate`

Asegúrate de que estos paquetes estén instalados en tu entorno de Python para usar el `ResponseTimeAnalyzer`. Puedes instalarlos usando pip:
```bash
pip install pandas numpy scipy tabulate
```

## Criterios de Limpieza del Conjunto de Datos

- **Eliminación de Nulos**: Se eliminan las filas con valores nulos.
- **Eliminación de Duplicados**: Se eliminan las filas duplicadas.
- **Filtrado por Idioma**: Se filtran las filas para incluir solo hablantes nativos de español.
- **Eliminación de Outliers**: Se eliminan los valores atípicos que difieren más de 3 desviaciones estándar de la media.
