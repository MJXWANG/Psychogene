# Psychophysics

**Psychophysics** is a Python project designed for generating experimental data and stimuli for Flanker and Stroop experiments. The project provides functionality to create datasets (in Excel format) and generate corresponding images for experimental use.

## Project Structure

Psychophysics/
├── Psycho/
│   ├── Main.py             # Main entry script containing interactive mode and data/image generation functions
│   ├── __init__.py         # Package initialization file (can be empty or include package-level variables)
│   └── generation/         # Additional modules for data generation (if any)
├── examples/
│   ├── example_usage.py    # Demonstrates interactive usage of Main.py
│   └── researcher_workflow.py  # A workflow example for generating experimental data and images (Stroop example)
├── legacy/                # Archive of older or deprecated code (if any)
├── .gitignore             # Git ignore file to exclude unnecessary files
├── pyproject.toml         # Project configuration and dependency management (using flit)
└── README.md              # This file

bash
Copy

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MJXWang/psychophysics.git
Change into the Project Directory:

bash
Copy
cd psychophysics
(Optional) Create and Activate a Virtual Environment:

bash
Copy
python -m venv venv
# For Linux/MacOS:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
Install Dependencies:

This project requires Python 3.12 or later. The main dependencies are:

pandas
matplotlib
openpyxl
If you are using flit, simply run:

bash
Copy
flit install --deps develop
Otherwise, install the dependencies manually:

bash
Copy
pip install pandas matplotlib openpyxl
Usage
Interactive Mode
Run the main interactive program which will prompt you to choose the experiment type and generate the corresponding data and images:

bash
Copy
python Psycho/Main.py
Alternatively, run the example usage script:

bash
Copy
python examples/example_usage.py
Researcher Workflow Example
For a complete workflow demonstration (using the Stroop experiment as an example), run the researcher workflow script:

bash
Copy
python examples/researcher_workflow.py
This script will:

Generate a Stroop dataset (Excel file) using a specified type (e.g., type1).
Create an output directory for experiment stimuli.
Generate Stroop images based on the generated dataset.
Dependencies
This project depends on the following libraries:

pandas – Data manipulation and analysis.
matplotlib – Plotting and image generation.
openpyxl – Reading and writing Excel files.
The project requires Python 3.12 or newer.

Contributing
Contributions are welcome! If you find any issues or would like to contribute improvements or new features, please follow these guidelines:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a clear description of your changes.
Also, feel free to open issues for any bugs or feature requests.

License
This project is licensed under the MIT License.

Contact
For any inquiries, please contact:

Maijunxian Wang – wmjx224@gmail.com