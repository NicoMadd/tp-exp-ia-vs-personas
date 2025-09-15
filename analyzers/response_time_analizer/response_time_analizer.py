import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu, shapiro, ttest_ind
from constants import *
from tabulate import tabulate
from utils.utils import print_separator, print_empty_line
import matplotlib.pyplot as plt
import os


class ResponseTimeAnalyzer:

    def __init__(self, pp_data: pd.Series, pia_data: pd.Series):
        self.pp_data: np.array = pp_data.to_numpy()
        self.pia_data: np.array = pia_data.to_numpy()

    def analyze(self):
        self.clean_datasets()
        self.describe_datasets()
        self.analyze_response_time_hypothesis()

    def clean_datasets(self) -> None:
        """
        Clean the datasets from outliers.
        """
        # Remove outliers that differ more than 3 standard deviations from the mean
        self.pp_data = self.pp_data[self.pp_data < self.pp_data.mean() + 3 * self.pp_data.std()]
        self.pp_data = self.pp_data[self.pp_data > self.pp_data.mean() - 3 * self.pp_data.std()]
        self.pia_data = self.pia_data[self.pia_data < self.pia_data.mean() + 3 * self.pia_data.std()]
        self.pia_data = self.pia_data[self.pia_data > self.pia_data.mean() - 3 * self.pia_data.std()]


    def describe_datasets(self) -> None:
        """
        Describe the dataset metrics using tabulate library.
        Shows the median, size, avg, min, max and std.
        """
        print("Describiendo conjuntos de datos...")
        print_empty_line()

        metrics = [
            ["Median", np.median(self.pp_data), np.median(self.pia_data)],
            ["Size", len(self.pp_data), len(self.pia_data)],
            ["Avg", np.mean(self.pp_data), np.mean(self.pia_data)],
            ["Min", np.min(self.pp_data), np.min(self.pia_data)],
            ["Max", np.max(self.pp_data), np.max(self.pia_data)],
            ["Std", np.std(self.pp_data), np.std(self.pia_data)]
        ]
        print(tabulate(metrics, headers=["Métrica", "Conjunto de Datos PP", "Conjunto de Datos P-IA"]))
        print_empty_line()

        # Plotting
        labels = ['Mediana', 'Tamaño', 'Promedio', 'Mínimo', 'Máximo', 'Desv. Estándar']
        pp_metrics = [np.median(self.pp_data), len(self.pp_data), np.mean(self.pp_data), np.min(self.pp_data), np.max(self.pp_data), np.std(self.pp_data)]
        pia_metrics = [np.median(self.pia_data), len(self.pia_data), np.mean(self.pia_data), np.min(self.pia_data), np.max(self.pia_data), np.std(self.pia_data)]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, pp_metrics, width, label='PP')
        rects2 = ax.bar(x + width/2, pia_metrics, width, label='P-IA')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Valores')
        ax.set_title('Métricas por grupo')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        # Save plot
        os.makedirs('images', exist_ok=True)
        plt.savefig('images/response_time_metrics.png')

        plt.show()

        # Box Plot
        fig, ax = plt.subplots()
        ax.boxplot([self.pp_data, self.pia_data], labels=['PP', 'P-IA'])
        ax.set_title('Distribución del Tiempo de Respuesta')
        ax.set_ylabel('Tiempo de Respuesta (ms)')

        # Save box plot
        plt.savefig('images/response_time_distribution.png')

        plt.show()

    def test_normality_of_response_time(self) -> None:
        """
        Test the normality of the response time using Shapiro-Wilk test.
        """
        print("Probando la normalidad del tiempo de respuesta...")
        print_empty_line()

        both_normal_datasets = True
        results = []

        w_pp, p_pp = shapiro(self.pp_data)
        normal_pp = "Yes" if p_pp >= 0.05 else "No"
        if p_pp < 0.05:
            both_normal_datasets = False
        results.append([
            "PP response time",
            f"{w_pp:.3f}",
            f"{p_pp:.4f}",
            normal_pp
        ])

        w_pia, p_pia = shapiro(self.pia_data)
        normal_pia = "Yes" if p_pia >= 0.05 else "No"
        if p_pia < 0.05:
            both_normal_datasets = False
        results.append([
            "P-IA response time",
            f"{w_pia:.3f}",
            f"{p_pia:.4f}",
            normal_pia
        ])

        print(tabulate(
            results,
            headers=["Dataset", "Shapiro-Wilk W", "p-value", "Normally Distributed?"]
        ))

        return both_normal_datasets

    def analyze_response_time_t_test(self) -> bool:
        """
        Analyze the response time using t-test.
        """
        t, p = ttest_ind(self.pp_data, self.pia_data)
        print(f"Estadístico de la prueba T: {t:.3f}, p={p:.4f}")
        return p < 0.05

    def analyze_response_time_mann_whitney_u_test(self) -> bool:
        """
        Analyze the response time using Mann-Whitney U test.
        """
        u, p = mannwhitneyu(self.pp_data, self.pia_data)
        print(f"Estadístico de la prueba de Mann-Whitney U: {u:.3f}, p={p:.4f}")
        return p < 0.05

    def analyze_response_time_hypothesis(self) -> None:
        """
        Analyze the response time hypothesis.
        """
        print("Analizando la hipótesis de tiempo de respuesta...")
        print_empty_line()

        both_normal_datasets = self.test_normality_of_response_time()

        print_separator()
        print_empty_line()

        if both_normal_datasets:
            print("Usando la prueba T...")
            print_empty_line()
            is_significant_diff = self.analyze_response_time_t_test()
        else:
            print("Usando la prueba de Mann-Whitney U...")
            print_empty_line()
            is_significant_diff = self.analyze_response_time_mann_whitney_u_test()

        if is_significant_diff:
            print("Hay una diferencia significativa entre los dos grupos.")
            print("Las diferencias en el tiempo de respuesta son estadísticamente significativas y difieren.")
            print("Rechazamos la hipótesis nula.")
        else:
            print("No hay una diferencia significativa entre los dos grupos.")
            print("No se rechaza la hipótesis nula.")

        print_empty_line()
