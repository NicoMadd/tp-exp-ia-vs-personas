import pandas as pd
import numpy as np
from constants import *
from scipy.stats import shapiro, levene, ttest_ind, chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()
    data = data.drop_duplicates()

    # Remove outliers above p99 and below p1
    data = data[data[RESPONSE_TIME_COLUMN] < data[RESPONSE_TIME_COLUMN].quantile(0.99)]
    data = data[data[RESPONSE_TIME_COLUMN] > data[RESPONSE_TIME_COLUMN].quantile(0.01)]

    ## Remove non spanish speakers
    data = data[data[NATIVE_LANGUAGE_COLUMN] == "Español"]

    # Remove rows that differ from defined test conditions


    return data

def analyze_identification_hypothesis(data: pd.DataFrame) -> None:
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

def analyze_response_time_hypothesis(pp_data: pd.DataFrame, pia_data: pd.DataFrame) -> None:
    print("Analyzing response time hypothesis...")

    pp_response_time = pp_data[RESPONSE_TIME_COLUMN].to_numpy()
    pia_response_time = pia_data[RESPONSE_TIME_COLUMN].to_numpy()

    # Test normality of response time using Shapiro-Wilk
    w, p = shapiro(pp_response_time)
    print(f"Shapiro-Wilk test statistic for PP response time: {w:.3f}, p={p:.4f}")
    if p < 0.05:
        print("Is not normally distributed")
    else:
        print("Is normally distributed")

    w, p = shapiro(pia_response_time)
    print(f"Shapiro-Wilk test statistic for P-IA response time: {w:.3f}, p={p:.4f}")
    if p < 0.05:
        print("Is not normally distributed")
    else:
        print("Is normally distributed")


    print("Values:")
    print(f"PP response time: {pp_response_time}")
    print(f"P-IA response time: {pia_response_time}")
   



def analyze_correlation_between_variables(data: pd.DataFrame) -> None:
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

def describe_dataset(data: pd.DataFrame) -> None:
    print("Describing dataset...")
    print("Total number of rows:", data.shape[0])
    total_pp_rows = data[data[CONDITION_COLUMN] == "P-P"].shape[0]
    total_pia_rows = data[data[CONDITION_COLUMN] == "P-IA"].shape[0]
    print("Total number of P-P rows:", total_pp_rows)
    print("Total number of P-IA rows:", total_pia_rows)

def split_dataset(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pp_dataset = data[data[CONDITION_COLUMN] == "P-P"]
    pia_dataset = data[data[CONDITION_COLUMN] == "P-IA"]
    return pp_dataset, pia_dataset

def main():
    data = pd.read_csv(DATA_FILE_PATH)
    data = clean_data(data)

    print("--------------------------------")
    describe_dataset(data)

    pp_dataset, pia_dataset = split_dataset(data)

    print("--------------------------------")
    #analyze_identification_hypothesis(data)

    print("--------------------------------")
    analyze_response_time_hypothesis(pp_dataset, pia_dataset)

    print("--------------------------------")
    #analyze_correlation_between_variables(data)



if __name__ == "__main__":
    main()

