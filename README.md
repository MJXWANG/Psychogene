# Psychophysics

**Psychophysics** is a Python project designed for generating experimental data and stimuli for Flanker and Stroop experiments. The project provides functionality to create datasets (in Excel format) and generate corresponding images for experimental use.

## Project Structure

plaintext
Psychophysics/
├── Psycho/
│   ├── Main.py              # Main entry script containing interactive mode and data/image generation functions
│   ├── __init__.py          # Package initialization file (can be empty or include package-level variables)
│   └── generation/          # Additional modules for data generation (if any)
├── examples/
│   ├── example_usage.py     # Demonstrates interactive usage of Main.py
│   └── researcher_workflow.py  # A workflow example for generating experimental data and images (Stroop example)
├── legacy/                  # Archive of older or deprecated code (if any)
├── .gitignore               # Git ignore file to exclude unnecessary files
├── pyproject.toml           # Project configuration and dependency management (using flit)
└── README.md                # This file


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MJXWANG/psychophysics.git
   ```

2. **Change into the Project Directory:**
   ```bash
   cd psychophysics
   ```

3. **(Optional) Create and Activate a Virtual Environment:**

   **For Linux/MacOS:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   **For Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies:**

   This project requires Python 3.12 or later. The main dependencies are:
   - `pandas`
   - `matplotlib`
   - `openpyxl`

   If you are using [flit](https://flit.readthedocs.io/), simply run:
   ```bash
   flit install --deps develop
   ```
   Otherwise, install the dependencies manually:
   ```bash
   pip install pandas matplotlib openpyxl
   ```

## Usage

### Interactive Mode

Run the main interactive program which will prompt you to choose the experiment type and generate the corresponding data and images:
```bash
python Psycho/Main.py
```

Alternatively, run the example usage script:
```bash
python examples/example_usage.py
```

### Researcher Workflow Example

For a complete workflow demonstration (using the Stroop experiment as an example), run the researcher workflow script:
```bash
python examples/researcher_workflow.py
```

This script will:
- Generate a Stroop dataset (Excel file) using a specified type (e.g., `type1`).
- Create an output directory for experiment stimuli.
- Generate Stroop images based on the generated dataset.

## Dependencies

This project depends on the following libraries:
- [pandas](https://pandas.pydata.org/) – Data manipulation and analysis
- [matplotlib](https://matplotlib.org/) – Plotting and image generation
- [openpyxl](https://openpyxl.readthedocs.io/) – Reading and writing Excel files

The project requires **Python 3.12** or newer.

## Contributing

Contributions are welcome! If you find any issues or would like to contribute improvements or new features, please follow these guidelines:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

Feel free to open issues for any bugs or feature requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries, please contact:

**Majunxian Wang** – [mjx@example.com](mailto:mjx@example.com)
```