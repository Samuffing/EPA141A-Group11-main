# Room for the River Project

## A Model Based Approach for Dike Ring 4 Gorssel 

Prepared for [EPA141a Model-Based Decision-Making]

| Team Member         | Student Number     |
|---------------------|--------------------|
| [Annette Kerkhoven] | [4793242]          |
| [Emiel Gemke]       | [4955358]          |
| [Sam Uffing]        | [4933192]          |
| [Stijn Blaas]       | [4666771]          |


## Table of Contents

- [Dike Model Analysis and Optimization Project](#dike-model-analysis-and-optimization-project)
  - [File Structure](#file-structure)
    - [Directories](#directories)
    - [Model & Workbench Files](#model--workbench-files)
    - [Experimentation & Analysis Files (Usage)](#experimentation--analysis-files-usage)
    - [Supporting Files](#supporting-files)
  - [Modeling Pipeline](#modeling-pipeline)
    - [Step 1: Initial Open Exploration](#step-1-initial-open-exploration)
    - [Step 2: Sensitivity Analysis](#step-2-sensitivity-analysis)
    - [Step 3: Multi-Objective Robust Decision Making (MORDM)](#step-3-multi-objective-robust-decision-making-mordm)
        - [Step 3a: Generating Alternatives](#step-3a-generating-alternatives)
        - [Step 3b: Scenario Discovery](#step-3b-scenario-discovery)
        - [Step 3c: Robustness Analysis](#step-3c-robustness-analysis)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Execution](#execution)
  - [Contributing](#contributing)
  - [License](#license)

## File Structure

### Directories

- **data**: Contains input and output CSV files for the model simulations and analyses.
- **scripts**: Python scripts used for model execution and analysis.
- **notebooks**: Jupyter notebooks for various stages of the analysis and decision-making process.

### Model & Workbench Files

- **problem_formulation.py**: Defines the problem formulation for the Dike model.
- **dike_model_simulation.py**: Core simulation functions for the Dike model.
- **dike_model_sensitivity.py**: Sensitivity analysis functions for the Dike model.
- **dike_model_function.py**: Core functions for Dike model operations.
- **funs_dikes.py**: Utility functions related to dike operations.
- **funs_economy.py**: Utility functions related to economic calculations.
- **funs_generate_network.py**: Functions to generate network structures for the Dike model.
- **funs_hydrostat.py**: Utility functions related to hydrological statistics.

### Experimentation & Analysis Files (Usage)

1. **open_exploration.py**
   - **Purpose**: Runs the Dike model for 20,000 scenarios with a "do nothing" policy.
   - **Usage**: Generates CSV files with outcomes and experiments data.

2. **open_exploration_policies.py**
   - **Purpose**: Runs the Dike model for 1,000 scenarios with 100 random policies.
   - **Usage**: Generates CSV files with outcomes and experiments data.

3. **open_exploration_SOBOL.py**
   - **Purpose**: Performs Sobol analysis as part of the open exploration.
   - **Usage**: Generates Sobol analysis results.

4. **MORDM_directed_search.py**
   - **Purpose**: Uses MOEA to find Pareto optimal lever combinations.
   - **Usage**: Saves results and convergence data to CSV files.

5. **MORDM_scen_discovery.py**
   - **Purpose**: Evaluates selected policies over 10,000 random scenarios.
   - **Usage**: Saves outcomes and experiments data to CSV files.

### Supporting Files

- **README.md**: This file, providing an overview of the project structure and usage.
- **LICENSE**: License information for the project.

## Modeling Pipeline

### Step 1: Initial Open Exploration

1. **Run the Dike model with no policies** using `open_exploration.py`.
2. **Analyze the results** using `open_exploration_plots_markdown.ipynb`.

### Step 2: Sensitivity Analysis

1. **Perform Sobol sensitivity analysis** using `open_exploration_SOBOL.py`.
2. **Review the results** using `SOBOL_global_sensitivity_analysis.ipynb`.

### Step 3: Multi-Objective Robust Decision Making (MORDM)

#### Step 3a: Generating Alternatives

1. **Generate policy alternatives** using `MORDM_generate_alternatives.ipynb`.

#### Step 3b: Scenario Discovery

1. **Discover scenarios** using `MORDM_Scen_Discovery.ipynb` and `MORDM_scen_discovery.py`.

#### Step 3c: Robustness Analysis

1. **Analyze the robustness** of policies using `MORDM_Robusteness.ipynb`.

## Getting Started

### Prerequisites

Ensure you have the following libraries installed:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `ema_workbench`
- `SALib`
- `networkx`
- `random`

### Installation

Clone the repository and install the required libraries.

### Execution

Run the scripts and notebooks in the specified order to replicate the analyses.

```bash
python scripts/open_exploration.py
python scripts/open_exploration_policies.py
python scripts/open_exploration_SOBOL.py
python scripts/MORDM_directed_search.py
python scripts/MORDM_scen_discovery.py
```

Open the Jupyter notebooks in your preferred environment and run the cells sequentially to perform the analyses and visualizations.

## Contributing

Feel free to contribute by submitting pull requests or opening issues for any bugs or enhancements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

