import pandas as pd
from analyzers.response_time_analizer import ResponseTimeAnalyzer
from analyzers.identification_analyzer import IdentificationAnalyzer
from constants import *
from utils.utils import print_separator


class Experiment:
    def __init__(self):
        self.data = pd.read_csv(DATA_FILE_PATH)
        self.data = self.clean_data(self.data)

    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        data = data.dropna()
        data = data.drop_duplicates()

        # Remove outliers that differ more than 3 standard deviations from the mean
        data = data[data[RESPONSE_TIME_COLUMN] < data[RESPONSE_TIME_COLUMN].mean() + 3 * data[RESPONSE_TIME_COLUMN].std()]
        data = data[data[RESPONSE_TIME_COLUMN] > data[RESPONSE_TIME_COLUMN].mean() - 3 * data[RESPONSE_TIME_COLUMN].std()]

        ## Remove non spanish speakers
        data = data[data[NATIVE_LANGUAGE_COLUMN] == "Español"]

        # Remove rows that differ from defined test conditions
        return data

    def describe(self):
        print_separator()
        self.describe_dataset(self.data)

    def describe_dataset(self, data: pd.DataFrame) -> None:
        print("Describing dataset...")
        print("Total number of rows:", data.shape[0])
        total_pp_rows = data[data[CONDITION_COLUMN] == "P-P"].shape[0]
        total_pia_rows = data[data[CONDITION_COLUMN] == "P-IA"].shape[0]
        print("Total number of P-P rows:", total_pp_rows)
        print("Total number of P-IA rows:", total_pia_rows)

    def split(self):
        return self.split_dataset(self.data)

    def split_dataset(self, data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        pp_dataset = data[data[CONDITION_COLUMN] == "P-P"]
        pia_dataset = data[data[CONDITION_COLUMN] == "P-IA"]
        return pp_dataset, pia_dataset

    def analyze_identification(self, pp_dataset: pd.DataFrame, pia_dataset: pd.DataFrame):
        print_separator()
        identification_analyzer = IdentificationAnalyzer(pp_dataset[IDENTIFICATION_COLUMN], pia_dataset[IDENTIFICATION_COLUMN])
        identification_analyzer.analyze()

    def analyze_response_time(self, pp_dataset: pd.DataFrame, pia_dataset: pd.DataFrame):
        print_separator()
        response_time_analyzer = ResponseTimeAnalyzer(pp_dataset[RESPONSE_TIME_COLUMN], pia_dataset[RESPONSE_TIME_COLUMN])
        response_time_analyzer.analyze()

    def analyze_correlation(self):
        print_separator()
        #self.analyze_correlation_between_variables(self.data)

    def analyze_identification_hypothesis(self, data: pd.DataFrame) -> None:
        print("Analyzing identification hypothesis...")
        pp_data = data[data[CONDITION_COLUMN] == "P-P"]
        pia_data = data[data[CONDITION_COLUMN] == "P-IA"]

        pp_correct = pp_data[TARGET_COLUMN].value_counts(normalize=True).get("SI", 0)
        pia_correct = pia_data[TARGET_COLUMN].value_counts(normalize=True).get("SI", 0)

        pp_total_answers = len(pp_data)
        pia_total_answers = len(pia_data)

        table = [
            [pp_correct, pp_total_answers-pp_correct],
            [pia_correct, pia_total_answers-pia_correct],
        ]

        chi2, p, dof, _ = chi2_contingency(table, correction=False)

        print(f"Chi2={chi2:.3f}, p={p:.4f}")

        if p < 0.05:
            print("Reject the null hypothesis. There is a significant difference between the two groups.")
            print("The two groups have different hit rates.")
        else:
            print("Fail to reject the null hypothesis. There is no significant difference between the two groups.")
            print("The two groups have the same hit rate.")

    def analyze_correlation_between_variables(self, data: pd.DataFrame) -> None:
        print("Analyzing correlation between variables...")
        pp_data = data[data[CONDITION_COLUMN] == "P-P"][CORRELATION_COLUMNS]
        pia_data = data[data[CONDITION_COLUMN] == "P-IA"][CORRELATION_COLUMNS]

        pp_correlation_matrix = pp_data.corr()
        pia_correlation_matrix = pia_data.corr()

        print("PP correlation matrix:")
        print(pp_correlation_matrix)

        print("P-IA correlation matrix:")
        print(pia_correlation_matrix)

        # plot graph of correlation between variables
        sns.heatmap(pp_correlation_matrix, annot=True, cmap="coolwarm")
        plt.show()
        sns.heatmap(pia_correlation_matrix, annot=True, cmap="coolwarm")
        plt.show()
