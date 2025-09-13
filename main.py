import pandas as pd
import numpy as np
from experiment import Experiment
from scipy.stats import shapiro, levene, ttest_ind, chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    experiment = Experiment()
    experiment.describe()
    pp_dataset, pia_dataset = experiment.split()
    experiment.analyze_identification()
    experiment.analyze_response_time(pp_dataset, pia_dataset)
    experiment.analyze_correlation()


if __name__ == "__main__":
    main()

