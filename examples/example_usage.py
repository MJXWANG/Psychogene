# example_usage.py
# This file is an example script that demonstrates how to use the main functionality of the project (interactive mode).
# Since example_usage.py is located in Psychophysics\examples and Main.py is in Psychophysics\Psycho,
# we need to add the Psycho directory to sys.path.

import sys
import os

# Get the root directory of Psychophysics (the parent directory of example_usage.py)
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Construct the absolute path to the Psycho directory (ensure the directory name is "Psycho")
psycho_dir = os.path.join(root_dir, "Psycho")
if psycho_dir not in sys.path:
    sys.path.insert(0, psycho_dir)

# Debug: Print the contents of the Psycho directory to confirm that Main.py exists
print("Added to sys.path:", psycho_dir)
print("Contents of Psycho directory:", os.listdir(psycho_dir))

# Import the Main module (case-sensitive)
import Main

if __name__ == "__main__":
    Main.main()
