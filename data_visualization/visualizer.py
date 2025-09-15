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

    def plot_all(self):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Visualización de Datos', fontsize=16)

        # Plot Age Distribution
        sns.histplot(self.data['edad'], bins=10, kde=True, color='skyblue', ax=axes[0, 0])
        axes[0, 0].set_title('Distribución de Edad')
        axes[0, 0].set_xlabel('Edad')
        axes[0, 0].set_ylabel('Frecuencia')

        # Plot Familiarity with AI
        sns.countplot(data=self.data, x='familiaridad_IA_1a5', palette='viridis', ax=axes[0, 1])
        axes[0, 1].set_title('Familiaridad con IA')
        axes[0, 1].set_xlabel('Familiaridad (1 a 5)')
        axes[0, 1].set_ylabel('Conteo')

        # Plot Digital Literacy
        sns.countplot(data=self.data, x='alfabetización_digital_1a5', palette='magma', ax=axes[1, 0])
        axes[1, 0].set_title('Alfabetización Digital')
        axes[1, 0].set_xlabel('Alfabetización (1 a 5)')
        axes[1, 0].set_ylabel('Conteo')

        # Plot Education
        sns.countplot(data=self.data, x='educación_1a5', palette='coolwarm', ax=axes[1, 1])
        axes[1, 1].set_title('Educación')
        axes[1, 1].set_xlabel('Educación (1 a 5)')
        axes[1, 1].set_ylabel('Conteo')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig('images/all_visualizations.png', dpi=300, bbox_inches='tight')
        plt.show()
