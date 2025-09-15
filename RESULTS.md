# Resultados del Experimento

## Análisis de Identificación

### Descripción del Conjunto de Datos
- **Número total de filas**: 119
- **Número total de filas P-P**: 50
- **Número total de filas P-IA**: 69

### Respuestas de Identificación (SI/NO)

| Respuesta | Conteo PP | % PP  | Conteo P-IA | % P-IA |
|-----------|-----------|-------|-------------|--------|
| SI        | 34        | 68.0% | 37          | 53.6%  |
| NO        | 16        | 32.0% | 32          | 46.4%  |
| Total     | 50        |       | 69          |        |

### Tabla de Contingencia

| Grupo | SI | NO |
|-------|----|----|
| PP    | 34 | 16 |
| PIA   | 37 | 32 |

### Análisis de Hipótesis
- **Chi2**: 2.490
- **p-valor**: 0.1146
- **Conclusión**: No hay una diferencia significativa entre los dos grupos. No rechazamos la hipótesis nula.

## Análisis de Tiempo de Respuesta

### Métricas del Conjunto de Datos

| Métrica | Conjunto de Datos PP | Conjunto de Datos P-IA |
|---------|----------------------|------------------------|
| Mediana | 6851                 | 7255                   |
| Tamaño  | 48                   | 67                     |
| Promedio| 6930.6               | 7221.75                |
| Mínimo  | 3694                 | 3547                   |
| Máximo  | 9671                 | 10914                  |
| Desv. Estándar | 1557.37       | 1878.12                |

### Análisis de Hipótesis

#### Prueba de Normalidad

| Conjunto de Datos   | Shapiro-Wilk W | p-valor | ¿Distribuido Normalmente? |
|---------------------|----------------|---------|---------------------------|
| Tiempo de respuesta PP | 0.968        | 0.2163  | Sí                        |
| Tiempo de respuesta P-IA | 0.981      | 0.4105  | Sí                        |

#### Prueba T
- **Estadístico de la prueba T**: -0.871
- **p-valor**: 0.3854
- **Conclusión**: No hay una diferencia significativa entre los dos grupos. No rechazamos la hipótesis nula.
