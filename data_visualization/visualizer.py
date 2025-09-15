import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

class Visualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def plot_age_distribution(self):
        plt.figure(figsize=(12, 6))
        sns.histplot(self.data['edad'], bins=10, kde=True, color='skyblue')
        plt.title('Distribución de Edad')
        plt.xlabel('Edad')
        plt.ylabel('Frecuencia')
        os.makedirs('images', exist_ok=True)
        plt.savefig('images/edad_distribution.png', dpi=300, bbox_inches='tight')
        plt.show()

    def plot_familiarity_with_ai(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(data=self.data, x='familiaridad_IA_1a5', palette='viridis')
        plt.title('Familiaridad con IA')
        plt.xlabel('Familiaridad (1 a 5)')
        plt.ylabel('Conteo')
        plt.savefig('images/familiaridad_IA.png', dpi=300, bbox_inches='tight')
        plt.show()

    def plot_digital_literacy(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(data=self.data, x='alfabetización_digital_1a5', palette='magma')
        plt.title('Alfabetización Digital')
        plt.xlabel('Alfabetización (1 a 5)')
        plt.ylabel('Conteo')
        plt.savefig('images/alfabetizacion_digital.png', dpi=300, bbox_inches='tight')
        plt.show()

    def plot_education(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(data=self.data, x='educación_1a5', palette='coolwarm')
        plt.title('Educación')
        plt.xlabel('Educación (1 a 5)')
        plt.ylabel('Conteo')
        plt.savefig('images/educacion.png', dpi=300, bbox_inches='tight')
        plt.show()
