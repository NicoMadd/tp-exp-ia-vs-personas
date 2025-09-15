# Response Time Analyzer

The `ResponseTimeAnalyzer` is a tool designed to analyze response time data, providing insights into the distribution and differences between two datasets. It includes functionality for cleaning data, describing dataset metrics, and testing hypotheses about response times.

## Features

- **Data Cleaning**: Removes outliers from the datasets that differ more than 2 standard deviations from the mean.
- **Dataset Description**: Describes the dataset metrics such as median, size, average, minimum, maximum, and standard deviation.
- **Hypothesis Testing**: Tests the hypothesis regarding response time differences using appropriate statistical tests.

## Usage

1. **Initialization**: Create an instance of `ResponseTimeAnalyzer` by passing two pandas Series objects representing the datasets to be analyzed.
   ```python
   analyzer = ResponseTimeAnalyzer(pp_data, pia_data)
   ```

2. **Analysis**: Call the `analyze` method to perform a full analysis, which includes cleaning the datasets, describing them, and analyzing the hypothesis.
   ```python
   analyzer.analyze()
   ```

## Methods

- `clean_datasets()`: Cleans the datasets by removing outliers.
- `describe_datasets()`: Prints a description of the datasets.
- `analyze_response_time_hypothesis()`: Analyzes the hypothesis using the appropriate statistical test.

## Statistical Tests

- **Shapiro-Wilk Test**: Tests the normality of the datasets.
- **T-Test**: Used if both datasets are normally distributed.
- **Mann-Whitney U Test**: Used if one or both datasets are not normally distributed.

## Dependencies

- `pandas`
- `numpy`
- `scipy`
- `tabulate`

Ensure these packages are installed in your Python environment to use the `ResponseTimeAnalyzer`. You can install them using pip:
```bash
pip install pandas numpy scipy tabulate
```
