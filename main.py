from experiment import Experiment


def main():
    experiment = Experiment()
    experiment.describe()
    pp_dataset, pia_dataset = experiment.split()
    experiment.analyze_identification(pp_dataset, pia_dataset)
    experiment.analyze_response_time(pp_dataset, pia_dataset)
    experiment.analyze_correlation()


if __name__ == "__main__":
    main()

