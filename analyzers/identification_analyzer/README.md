# Analizador de Identificación

El `IdentificationAnalyzer` es una herramienta diseñada para analizar datos de identificación, centrándose específicamente en las respuestas categorizadas como "SI" (sí) y "NO" (no). Proporciona información estadística sobre los datos y prueba hipótesis sobre las diferencias entre dos conjuntos de datos.

## Características

- **Descripción de Datos**: Describe las respuestas de identificación en ambos conjuntos de datos, mostrando el conteo y porcentaje de respuestas "SI" y "NO".
- **Tabla de Contingencia**: Crea una tabla de contingencia a partir de las respuestas de identificación.
- **Análisis de Hipótesis**: Analiza la hipótesis de identificación utilizando la prueba de chi-cuadrado o la prueba exacta de Fisher, dependiendo del tamaño de la muestra.

## Uso

1. **Inicialización**: Crea una instancia de `IdentificationAnalyzer` pasando dos objetos Series de pandas que representan los conjuntos de datos a analizar.
   ```python
   analyzer = IdentificationAnalyzer(pp_data, pia_data)
   ```

2. **Análisis**: Llama al método `analyze` para realizar un análisis completo, que incluye describir los conjuntos de datos, crear una tabla de contingencia y analizar la hipótesis.
   ```python
   analyzer.analyze()
   ```

## Métodos

- `describe_datasets()`: Imprime una descripción de los conjuntos de datos.
- `create_contingency_table()`: Devuelve una tabla de contingencia como un array de numpy.
- `analyze_identification_hypothesis(contingency_table)`: Analiza la hipótesis utilizando la prueba estadística adecuada.

## Pruebas Estadísticas

- **Prueba de Chi-Cuadrado**: Se utiliza cuando ambos conjuntos de datos tienen más de 5 muestras.
- **Prueba Exacta de Fisher**: Se utiliza cuando uno o ambos conjuntos de datos tienen 5 o menos muestras.

## Dependencias

- `pandas`
- `numpy`
- `scipy`
- `tabulate`

Asegúrate de que estos paquetes estén instalados en tu entorno de Python para usar el `IdentificationAnalyzer`. Puedes instalarlos usando pip:
```bash
pip install pandas numpy scipy tabulate
```
