import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu, shapiro, ttest_ind
from constants import *
from tabulate import tabulate
from utils.utils import print_separator, print_empty_line


class ResponseTimeAnalyzer:

    def __init__(self, pp_data: pd.Series, pia_data: pd.Series):
        self.pp_data = pp_data.to_numpy()
        self.pia_data = pia_data.to_numpy()

    def analyze(self):
        self.clean_datasets()
        self.describe_datasets()
        self.analyze_response_time_hypothesis()

    def clean_datasets(self) -> None:
        """
        Clean the datasets from outliers.
        """
        # Remove outliers that differ more than 3 standard deviations from the mean
        self.pp_data = self.pp_data[self.pp_data < self.pp_data.mean() + 2 * self.pp_data.std()]
        self.pp_data = self.pp_data[self.pp_data > self.pp_data.mean() - 2 * self.pp_data.std()]
        self.pia_data = self.pia_data[self.pia_data < self.pia_data.mean() + 2 * self.pia_data.std()]
        self.pia_data = self.pia_data[self.pia_data > self.pia_data.mean() - 2 * self.pia_data.std()]


    def describe_datasets(self) -> None:
        """
        Describe the dataset metrics using tabulate library.
        Shows the median, size, avg, min, max and std.
        """
        print("Describing datasets...")
        print_empty_line()

        metrics = [
            ["Median", np.median(self.pp_data), np.median(self.pia_data)],
            ["Size", len(self.pp_data), len(self.pia_data)],
            ["Avg", np.mean(self.pp_data), np.mean(self.pia_data)],
            ["Min", np.min(self.pp_data), np.min(self.pia_data)],
            ["Max", np.max(self.pp_data), np.max(self.pia_data)],
            ["Std", np.std(self.pp_data), np.std(self.pia_data)]
        ]
        print(tabulate(metrics, headers=["Metric", "PP dataset", "P-IA dataset"]))
        print_empty_line()

    def test_normality_of_response_time(self) -> None:
        """
        Test the normality of the response time using Shapiro-Wilk test.
        """
        print("Testing normality of response time...")
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
        print(f"T-test statistic: {t:.3f}, p={p:.4f}")
        return p < 0.05

    def analyze_response_time_mann_whitney_u_test(self) -> bool:
        """
        Analyze the response time using Mann-Whitney U test.
        """
        u, p = mannwhitneyu(self.pp_data, self.pia_data)
        print(f"Mann-Whitney U test statistic: {u:.3f}, p={p:.4f}")
        return p < 0.05

    def analyze_response_time_hypothesis(self) -> None:
        """
        Analyze the response time hypothesis.
        """
        print("Analyzing Response Time Hypothesis...")
        print_empty_line()

        both_normal_datasets = self.test_normality_of_response_time()

        print_separator()
        print_empty_line()

        if both_normal_datasets:
            print("Using t-test...")
            print_empty_line()
            is_significant_diff = self.analyze_response_time_t_test()
        else:
            print("Using Mann-Whitney U test...")
            print_empty_line()
            is_significant_diff = self.analyze_response_time_mann_whitney_u_test()

        if is_significant_diff:
            print("There is a significant difference between the two groups.")
            print("The differences in response time are statistically significant and differ.")
            print("We reject the null hypothesis.")
        else:
            print("There is no significant difference between the two groups.")
            print("We fail to reject the null hypothesis.")

        print_empty_line()
