import pandas as pd
import numpy as np
from ema_workbench import (Model, RealParameter, perform_experiments, MultiprocessingEvaluator)
from ema_workbench.util import ema_logging
from SALib.sample import saltelli
from SALib.analyze import sobol

# Assuming flood_risk_function is defined and implemented
def flood_risk_function(rainfall_intensity, river_capacity, dike_strength):
    # Placeholder function; replace with the actual model
    total_cost = (rainfall_intensity / river_capacity) * (1 - dike_strength)
    return {'total_cost': total_cost}

# Define the model
model = Model('FloodRiskModel', function=flood_risk_function)
model.uncertainties = [RealParameter('rainfall_intensity', 0, 100),
                       RealParameter('river_capacity', 100, 1000),
                       RealParameter('dike_strength', 0, 1)]
model.outcomes = ['total_cost']

# Perform experiments with a high number of samples for sensitivity analysis
ema_logging.log_to_stderr(ema_logging.INFO)

# Define the problem for SALib
problem = {
    'num_vars': len(model.uncertainties),
    'names': [uncert.name for uncert in model.uncertainties],
    'bounds': [[uncert.dist.ppf(0), uncert.dist.ppf(1)] for uncert in model.uncertainties]
}

# Generate samples using Saltelli's sampling method
param_values = saltelli.sample(problem, 1024)

# Create scenarios in the format expected by EMA Workbench
scenarios = [dict(zip(problem['names'], sample)) for sample in param_values]

# Perform experiments using the generated samples
with MultiprocessingEvaluator(model) as evaluator:
    results = evaluator.perform_experiments(scenarios=scenarios)

experiments, outcomes = results

# Extract the outcome of interest
total_cost = outcomes['total_cost']

# Perform Sobol sensitivity analysis using SALib
Si = sobol.analyze(problem, np.array(total_cost), print_to_console=True)

# Convert results to DataFrame for easier interpretation
sobol_indices = pd.DataFrame({
    'ST': Si['ST'],
    'ST_conf': Si['ST_conf'],
    'S1': Si['S1'],
    'S1_conf': Si['S1_conf'],
    'S2': Si['S2'].flatten(),
    'S2_conf': Si['S2_conf'].flatten()
}, index=problem['names'])

# Save results to CSV
sobol_indices.to_csv('sobol_sensitivity_indices.csv')

# Print results
print(sobol_indices)