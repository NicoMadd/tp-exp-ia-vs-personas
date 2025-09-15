import pandas as pd
import numpy as np
from tabulate import tabulate
from scipy.stats import chi2_contingency, fisher_exact
from utils.utils import print_empty_line
import matplotlib.pyplot as plt
import os

class IdentificationAnalyzer:

    pp_data: np.array
    pia_data: np.array

    def __init__(self, pp_data: pd.Series, pia_data: pd.Series):
        self.pp_data = pp_data.to_numpy()
        self.pia_data = pia_data.to_numpy()

    def _count_si_no(self, arr: np.array) -> tuple[int, float, int, float, int]:
            unique, counts = np.unique(arr, return_counts=True)
            count_dict = dict(zip(unique, counts))
            total = len(arr)
            si_count = count_dict.get("SI", 0)
            no_count = count_dict.get("NO", 0)
            si_pct = (si_count / total) * 100 if total > 0 else 0
            no_pct = (no_count / total) * 100 if total > 0 else 0
            return si_count, si_pct, no_count, no_pct, total

    def describe_datasets(self) -> None:
        """
        Describe the identification answers (SI/NO) in both datasets.
        Shows the count and percentage of SI and NO answers.
        """
        print("Describiendo respuestas de identificación (SI/NO) en los conjuntos de datos...")
        print_empty_line()

        pp_si, pp_si_pct, pp_no, pp_no_pct, pp_total = self._count_si_no(self.pp_data)
        pia_si, pia_si_pct, pia_no, pia_no_pct, pia_total = self._count_si_no(self.pia_data)

        metrics = [
            ["SI", pp_si, f"{pp_si_pct:.1f}%", pia_si, f"{pia_si_pct:.1f}%"],
            ["NO", pp_no, f"{pp_no_pct:.1f}%", pia_no, f"{pia_no_pct:.1f}%"],
            ["Total", pp_total, "", pia_total, ""]
        ]
        print(tabulate(metrics, headers=["Respuesta", "Conteo PP", "% PP", "Conteo P-IA", "% P-IA"]))
        print_empty_line()

        # Plotting
        labels = ['SI', 'NO']
        pp_counts = [pp_si, pp_no]
        pia_counts = [pia_si, pia_no]

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, pp_counts, width, label='PP')
        rects2 = ax.bar(x + width/2, pia_counts, width, label='P-IA')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Conteos')
        ax.set_title('Conteos por grupo y respuesta')
        ax.set_xticks(x)
        ax.set_xticklabels(['Sí', 'No'])
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        fig.tight_layout()

        # Save plot
        os.makedirs('images', exist_ok=True)
        plt.savefig('images/identification_analysis.png', dpi=300, bbox_inches='tight')

        plt.show()
    
    def create_contingency_table(self) -> np.array:
        """
        Create a contingency table from the identification answers.
        """
        cont_table = np.array([[np.count_nonzero(self.pp_data == "SI"), np.count_nonzero(self.pp_data == "NO")], [np.count_nonzero(self.pia_data == "SI"), np.count_nonzero(self.pia_data == "NO")]])
        
        printable_contingency_table = [
            ["PP", cont_table[0][0], cont_table[0][1]],
            ["PIA", cont_table[1][0], cont_table[1][1]]
        ]
        print(tabulate(printable_contingency_table, headers=["Grupo", "SI", "NO"]))
        print_empty_line()
        return cont_table

    def analyze_identification_hypothesis(self, contingency_table: np.array):
        """
        Analyze the identification hypothesis.

        Use chi-square test to analyze the hypothesis if samples sizes are greater than 5.

        else use fisher exact test.
        """
        print("Analizando la hipótesis de identificación...")

        if len(self.pp_data) > 5 and len(self.pia_data) > 5:
            print_empty_line()
            is_significant_diff = self.analyze_identification_hypothesis_chi_square(contingency_table)
        else:
            print_empty_line()
            is_significant_diff = self.analyze_identification_hypothesis_fisher_exact(contingency_table)

        if is_significant_diff:
            print("Hay una diferencia significativa entre los dos grupos.")
            print("Los dos grupos tienen diferentes tasas de acierto.")
            print("Rechazamos la hipótesis nula.")
        else:
            print("No hay una diferencia significativa entre los dos grupos.")
            print("No se rechaza la hipótesis nula.")
        print_empty_line()

    def analyze_identification_hypothesis_chi_square(self, contingency_table: np.array):
        """
        Analyze the identification hypothesis using chi-square test.
        """
        print("Analizando la hipótesis de identificación usando la prueba de chi-cuadrado...")
        print_empty_line()

        chi2, p, dof, _ = chi2_contingency(contingency_table, correction=False)
        print(f"Chi2={chi2:.3f}, p={p:.4f}")

        return p < 0.05

    def analyze_identification_hypothesis_fisher_exact(self, contingency_table: np.array):
        """
        Analyze the identification hypothesis using fisher exact test.
        """
        print("Analizando la hipótesis de identificación usando la prueba exacta de Fisher...")
        print_empty_line()

        oddsratio, p = fisher_exact(contingency_table)
        print(f"Odds ratio={oddsratio:.3f}, p={p:.4f}")

        return p < 0.05

    def analyze(self):
        self.describe_datasets()
        contingency_table = self.create_contingency_table()
        self.analyze_identification_hypothesis(contingency_table)
