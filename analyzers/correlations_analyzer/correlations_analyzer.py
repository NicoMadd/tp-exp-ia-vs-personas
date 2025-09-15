import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class CorrelationsAnalyzer:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def analyze(self):
        self.analyze_correlation_between_variables()

    def analyze_correlation_between_variables(self):
        print("Analizando la correlación entre variables...")
        # Select only relevant numeric columns for correlation analysis
        relevant_columns = [
            'edad',
            'familiaridad_IA_1a5',
            'alfabetización_digital_1a5',
            'educación_1a5',
            'tiempo_respuesta_ms',
            'confianza_identificación_1a5',
            'percepción_humanidad_1a5'
        ]
        numeric_data = self.data[relevant_columns]
        correlation_matrix = numeric_data.corr()

        # Map column names to proper Spanish labels
        column_labels = {
            'edad': 'Edad',
            'familiaridad_IA_1a5': 'Familiaridad IA',
            'alfabetización_digital_1a5': 'Alfabetización Digital',
            'educación_1a5': 'Educación',
            'tiempo_respuesta_ms': 'Tiempo de Respuesta',
            'confianza_identificación_1a5': 'Confianza Identificación',
            'percepción_humanidad_1a5': 'Percepción de Humanidad'
        }
        correlation_matrix.rename(columns=column_labels, index=column_labels, inplace=True)

        print("Matriz de correlación:")
        print(correlation_matrix)

        # plot graph of correlation between variables
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title('Mapa de Calor de Correlaciones')
        # Save heatmap
        plt.savefig('images/correlation_heatmap.png')
        plt.show()
