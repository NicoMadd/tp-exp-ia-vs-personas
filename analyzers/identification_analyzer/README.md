# Identification Analyzer

The `IdentificationAnalyzer` is a tool designed to analyze identification data, specifically focusing on the responses categorized as "SI" (yes) and "NO" (no). It provides statistical insights into the data and tests hypotheses regarding the differences between two datasets.

## Features

- **Data Description**: Describes the identification answers in both datasets, showing the count and percentage of "SI" and "NO" answers.
- **Contingency Table**: Creates a contingency table from the identification answers.
- **Hypothesis Analysis**: Analyzes the identification hypothesis using either the chi-square test or Fisher's exact test, depending on the sample size.

## Usage

1. **Initialization**: Create an instance of `IdentificationAnalyzer` by passing two pandas Series objects representing the datasets to be analyzed.
   ```python
   analyzer = IdentificationAnalyzer(pp_data, pia_data)
   ```

2. **Analysis**: Call the `analyze` method to perform a full analysis, which includes describing the datasets, creating a contingency table, and analyzing the hypothesis.
   ```python
   analyzer.analyze()
   ```

## Methods

- `describe_datasets()`: Prints a description of the datasets.
- `create_contingency_table()`: Returns a contingency table as a numpy array.
- `analyze_identification_hypothesis(contingency_table)`: Analyzes the hypothesis using the appropriate statistical test.

## Statistical Tests

- **Chi-Square Test**: Used when both datasets have more than 5 samples.
- **Fisher's Exact Test**: Used when one or both datasets have 5 or fewer samples.

## Dependencies

- `pandas`
- `numpy`
- `scipy`
- `tabulate`

Ensure these packages are installed in your Python environment to use the `IdentificationAnalyzer`. You can install them using pip:
```bash
pip install pandas numpy scipy tabulate
```
