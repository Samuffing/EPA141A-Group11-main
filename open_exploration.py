'''
This script runs the Dike model using problem formulation 3 for 20,000 scenarios
and a 'do nothing' zero policy. A multiprocessing evaluator is utilized to perform the experiments.
The script saves the complete outcomes and experiments data to CSV files in the data/output directory.
'''

import pandas as pd
import networkx as nx
import random
from ema_workbench import ema_logging, MultiprocessingEvaluator, Policy
from problem_formulation import get_model_for_problem_formulation

def main():
    # Set random seed for reproducibility
    random.seed(1234)

    # Enable logging
    ema_logging.log_to_stderr(ema_logging.INFO)

    # Retrieve the Dike model and planning steps for problem formulation 3
    dike_model, planning_steps = get_model_for_problem_formulation(3)

    # Define number of scenarios to run
    n_scenarios = 20000

    # Create a 'do nothing' zero policy dictionary
    def generate_zero_policy():
        return {lever.name: 0 for lever in dike_model.levers}

    # Instantiate policies list with a zero policy
    zero_policy = Policy("policy 0", **generate_zero_policy())
    policies = [zero_policy]

    # Perform experiments using the MultiprocessingEvaluator
    with MultiprocessingEvaluator(dike_model) as evaluator:
        results_zero = evaluator.perform_experiments(n_scenarios, policies)

    # Unpack the results into experiments and outcomes
    experiments_zero, outcomes_zero = results_zero

    # Extract policy names from experiments
    policy_names = experiments_zero['policy']

    # Convert outcomes to DataFrame and add the policy column
    outcomes_df = pd.DataFrame.from_dict(outcomes_zero)
    outcomes_df['policy'] = policy_names

    # Save the complete outcomes and experiments to CSV files
    outcomes_df.to_csv('data/output/open_exploration_outcomes_zero.csv', index=False)
    experiments_zero.to_csv('data/output/open_exploration_experiments_zero.csv', index=False)

# Entry point of the script
if __name__ == "__main__":
    main()
