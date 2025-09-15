import pandas as pd
from analyzers.response_time_analizer import ResponseTimeAnalyzer
from analyzers.identification_analyzer import IdentificationAnalyzer
from analyzers.correlations_analyzer import CorrelationsAnalyzer
from utils.utils import print_separator
from constants import *


class Experiment:
    def __init__(self):
        self.data = pd.read_csv(DATA_FILE_PATH)
        self.data = self.clean_data()

    def clean_data(self) -> pd.DataFrame:
        data = self.data.dropna()
        data = data.drop_duplicates()

        # Remove non spanish speakers
        data = data[data[NATIVE_LANGUAGE_COLUMN] == "Español"]
        
        return data

    def describe(self):
        print_separator()
        self.describe_dataset(self.data)

    def describe_dataset(self, data: pd.DataFrame) -> None:
        print("Describiendo conjunto de datos...")
        print("Número total de filas:", data.shape[0])
        total_pp_rows = data[data[CONDITION_COLUMN] == "P-P"].shape[0]
        total_pia_rows = data[data[CONDITION_COLUMN] == "P-IA"].shape[0]
        print("Número total de filas P-P:", total_pp_rows)
        print("Número total de filas P-IA:", total_pia_rows)

    def split(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        pp_dataset = self.data[self.data[CONDITION_COLUMN] == "P-P"]
        pia_dataset = self.data[self.data[CONDITION_COLUMN] == "P-IA"]
        return pp_dataset, pia_dataset

    def analyze_identification(self, pp_dataset: pd.DataFrame, pia_dataset: pd.DataFrame):
        print_separator()
        identification_analyzer = IdentificationAnalyzer(pp_dataset[IDENTIFICATION_COLUMN], pia_dataset[IDENTIFICATION_COLUMN])
        identification_analyzer.analyze()

    def analyze_response_time(self, pp_dataset: pd.DataFrame, pia_dataset: pd.DataFrame):
        print_separator()
        response_time_analyzer = ResponseTimeAnalyzer(pp_dataset[RESPONSE_TIME_COLUMN], pia_dataset[RESPONSE_TIME_COLUMN])
        response_time_analyzer.analyze()

    def analyze_correlations(self, data: pd.DataFrame):
        print_separator()
        correlations_analyzer = CorrelationsAnalyzer(data)
        correlations_analyzer.analyze()
