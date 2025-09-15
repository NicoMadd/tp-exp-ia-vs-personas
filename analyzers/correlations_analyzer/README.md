# Analizador de Correlaciones

El `CorrelationsAnalyzer` es una herramienta diseñada para analizar las correlaciones entre variables en un conjunto de datos. Proporciona información sobre las relaciones entre diferentes variables utilizando matrices de correlación y visualizaciones.

## Características

- **Matriz de Correlación**: Calcula y muestra la matriz de correlación para el conjunto de datos.
- **Visualización**: Grafica un mapa de calor de la matriz de correlación para facilitar la visualización de las relaciones.

## Uso

1. **Inicialización**: Crea una instancia de `CorrelationsAnalyzer` pasando un DataFrame de pandas que representa el conjunto de datos a analizar.
   ```python
   analyzer = CorrelationsAnalyzer(data)
   ```

2. **Análisis**: Llama al método `analyze` para realizar el análisis de correlación, que incluye calcular y visualizar la matriz de correlación.
   ```python
   analyzer.analyze()
   ```

## Métodos

- `analyze_correlation_between_variables()`: Calcula e imprime la matriz de correlación, y muestra un mapa de calor.

## Dependencias

- `pandas`
- `seaborn`
- `matplotlib`

Asegúrate de que estos paquetes estén instalados en tu entorno de Python para usar el `CorrelationsAnalyzer`. Puedes instalarlos usando pip:
```bash
pip install pandas seaborn matplotlib
```
