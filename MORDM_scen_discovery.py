"""
This script is designed to evaluate a set of selected policies under a specified problem formulation using the EMA Workbench,
The script begins by initializing the random seed to ensure reproducibility of results and setting up logging to display informational messages.
Then problem formulation 3(with adjustments) is innitiated

Next, the script loads a predefined set of policies from a CSV file. The policies are selected in the MORDM_Generate_Alternative.ipynb file.

These policies are evaluated using the MultiprocessingEvaluator and stored in a CSV file

"""

import pandas as pd
from ema_workbench.util import ema_logging
from ema_workbench import (MultiprocessingEvaluator, Policy)
from problem_formulation import get_model_for_problem_formulation
import random



if __name__ == "__main__":
    random.seed(1234)

    ema_logging.log_to_stderr(ema_logging.INFO)

    model, steps = get_model_for_problem_formulation(3)

    n_scenarios = 10000

    selected_policies = pd.read_csv('data/output/MOEA_10000_selected_policies.csv')

    policies_to_evaluate = []
    for i, policy in selected_policies.iterrows():
        policies_to_evaluate.append(Policy(str(i), **policy.to_dict()))


    with MultiprocessingEvaluator(model) as evaluator:
        results_uncertainty = evaluator.perform_experiments(n_scenarios, policies_to_evaluate)

    experiments, outcomes = results_uncertainty

    # Select policies from experiments dataframe
    policies = experiments['policy']

    # Convert outcomes to dataframe
    outcomes_uncertainties = pd.DataFrame.from_dict(outcomes)
    # Add policy column to outcomes dataframe
    outcomes_uncertainties['policy'] = policies

    # Write outcomes and experiments to csv
    experiments.to_csv('data/output/MOEA_test_experiments.csv')
    outcomes_uncertainties.to_csv('data/output/MOEA_test_outcomes.csv')