
'''This script runs the Dike model using problem formulation 3 for 1000 scenarios
and 100 random policies. A multiprocessing evaluator is utilized to perform the experiments.
The script saves the complete outcomes and experiments data to CSV files in the data/output directory.
'''

import pandas as pd
import networkx as nx
import random
from ema_workbench import ema_logging, MultiprocessingEvaluator
from problem_formulation import get_model_for_problem_formulation

def main():
    # Set random seed for reproducibility
    random.seed(1234)

    # Enable logging
    ema_logging.log_to_stderr(ema_logging.INFO)

    # Retrieve the Dike model and planning steps for problem formulation 3
    dike_model, planning_steps = get_model_for_problem_formulation(3)

    # Define the number of scenarios and random policies
    n_scenarios = 1000
    n_random_policies = 1000

    # Perform experiments using the MultiprocessingEvaluator
    with MultiprocessingEvaluator(dike_model) as evaluator:
        results_random = evaluator.perform_experiments(n_scenarios, n_random_policies)

    # Unpack the results into experiments and outcomes
    experiments_random, outcomes_random = results_random

    # Extract policy names from experiments
    policy_names = experiments_random['policy']

    # Convert outcomes to DataFrame and add the policy column
    outcomes_df = pd.DataFrame.from_dict(outcomes_random)
    outcomes_df['policy'] = policy_names

    # Save the complete outcomes and experiments to CSV files
    outcomes_df.to_csv('data/output/open_exploration_outcomes_random.csv', index=False)
    experiments_random.to_csv('data/output/open_exploration_experiments_random.csv', index=False)

# Entry point of the script
if __name__ == "__main__":
    main()
