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
        correlation_matrix = self.data.corr()

        print("Matriz de correlación:")
        print(correlation_matrix)

        # plot graph of correlation between variables
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        plt.show()
