from ema_workbench import (
    Model, MultiprocessingEvaluator, Policy, Scenario, perform_experiments, save_results
)
from ema_workbench.em_framework.samplers import sample_levers, sample_uncertainties
from ema_workbench.util import ema_logging
from problem_formulation import get_model_for_problem_formulation
import pandas as pd

if __name__ == "__main__":
    ema_logging.log_to_stderr(ema_logging.INFO)

    # Get the model
    dike_model, planning_steps = get_model_for_problem_formulation(5)

    # Generate random policies and scenarios using Latin Hypercube Sampling (LHS)
    n_policies = 5
    n_scenarios = 10

    policies = sample_levers(dike_model, n_policies)
    scenarios = sample_uncertainties(dike_model, n_scenarios)

    # Run the experiments
    with MultiprocessingEvaluator(dike_model) as evaluator:
        results = evaluator.perform_experiments(scenarios=scenarios, policies=policies)

    experiments, outcomes = results


    # Create dataframes for experiments and outcomes
    df_experiments = pd.DataFrame(experiments)
    df_outcomes = pd.DataFrame({k: v.flatten() for k, v in outcomes.items()})

    # Combine experiments and outcomes for saving
    combined_df = pd.concat([df_experiments, df_outcomes], axis=1)

    # Save the combined dataframe to a CSV file
    combined_df.to_csv('open_exploration_data._small.csv', index=False)
    print("Combined data saved to 'open_exploration_data.csv'.")


