"""
This script performs Sobol sensitivity analysis on a specified model using the EMA Workbench framework.
The analysis aims to evaluate the impact of uncertainties on the outcomes by sampling different scenarios.

Key Steps:
1. Import necessary libraries and modules: pandas, random, ema_logging, Samplers, MultiprocessingEvaluator, Policy, and the model formulation function.
2. Define the `perform_sobol_analysis` function:
    - Set the random seed for reproducibility and enable logging.
    - Initialize the model and specify the number of scenarios for Sobol sampling.
    - Define a baseline policy where all decision levers are set to zero.
    - Use `MultiprocessingEvaluator` to perform Sobol sampling across multiple processes.
    - Save the resulting experiments and outcomes to CSV files for further analysis.
3. Execute the `perform_sobol_analysis` function when the script is run directly.

Usage:
- Ensure the necessary modules are installed and the model formulation function is correctly implemented.
- Run the script to generate Sobol sensitivity analysis results, which will be saved in the 'data/output/' directory.
"""


import pandas as pd
import random
from ema_workbench.util import ema_logging
from ema_workbench import Samplers, MultiprocessingEvaluator, Policy
from problem_formulation import get_model_for_problem_formulation

def perform_sobol_analysis():
    # Set the random seed for reproducibility and enable logging
    random.seed(1234)
    ema_logging.log_to_stderr(ema_logging.INFO)

    # Initialize the model and specify the number of scenarios
    model, _ = get_model_for_problem_formulation(3)
    scenarios_count = 1024  # Number of scenarios for Sobol sampling

    # Define a baseline policy with all levers set to zero
    baseline_policy = {lever.name: 0 for lever in model.levers}
    policies = [Policy("Baseline Policy", **baseline_policy)]

    # Execute Sobol sampling with multiple processes
    with MultiprocessingEvaluator(model, n_processes=-1) as evaluator:
        experiments, outcomes = evaluator.perform_experiments(scenarios_count, policies,
                                                              uncertainty_sampling=Samplers.SOBOL)

    # Save the results to CSV files
    experiments.to_csv('data/output/sobol_experiments_results.csv')
    pd.DataFrame.from_dict(outcomes).to_csv('data/output/sobol_outcomes_results.csv')

if __name__ == "__main__":
    perform_sobol_analysis()
