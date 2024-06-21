
"""
This script  performs the directed search based on the criteria made in the MORDM_Generate_Alternatives.ipynb file

The EpsilonProgress from ema_workbench is used to evaluate performance of the policies in comparison to the earlyer defined worst case scenario

A total of 10,000 function evaluations (nfe) are specified for the optimization process.
The MultiprocessingEvaluator is used to perform this computationally intensive task efficiently.
 he optimization seeks to identify the best policy levers by searching over the defined space and evaluating each candidate policy against the reference scenario.

At the end of the analysis all policies are stored in a csv file
"""

from ema_workbench.util import ema_logging
from ema_workbench.em_framework.optimization import EpsilonProgress
from ema_workbench import (MultiprocessingEvaluator, Scenario)
from problem_formulation import get_model_for_problem_formulation
import random

if __name__ == "__main__":
    random.seed(1234)

    ema_logging.log_to_stderr(ema_logging.INFO)

    model, steps = get_model_for_problem_formulation(3)

    # Define reference values of uncertainty analysis
    reference_values = {
        "A.1_Bmax": 124.161608,
        "A.1_Brate": 10,
        "A.1_pfail": 0.972902,
        "A.2_Bmax": 208.516404,
        "A.2_Brate": 1.0,
        "A.2_pfail": 0.940094,
        "A.3_Bmax": 184.814021,
        "A.3_Brate": 10,
        "A.3_pfail": 0.733796,
        "A.4_Bmax": 318.749226,
        "A.4_Brate": 1.0,
        "A.4_pfail": 0.005997,
        "A.5_Bmax": 216.896388,
        "A.5_Brate": 1.5,
        "A.5_pfail": 0.043729,
        "discount rate 0": 1.5,
        "discount rate 1": 1.5,
        "discount rate 2": 1.5,
        "A.0_ID flood wave shape": 35,
    }

    ref_scenario = Scenario("reference", **reference_values)

    convergence_metrics = [EpsilonProgress()]

    epsilon = [1e3] * len(model.outcomes)

    nfe = 10000


    # Perform model evaluation
    with MultiprocessingEvaluator(model) as evaluator:
        results, convergence = evaluator.optimize(
            nfe=nfe,
            searchover="levers",
            epsilons=epsilon,
            convergence=convergence_metrics,
            reference=ref_scenario,
        )

    # Write results and convergence to csv
    results.to_csv('data/output/MOEA_10000_results.csv')
    convergence.to_csv('data/output/MOEA_10000_convergence.csv')