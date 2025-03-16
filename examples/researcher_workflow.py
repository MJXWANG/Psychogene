# researcher_workflow.py
# This example demonstrates how to utilize the functions encapsulated in the Psycho project
# to complete a full Stroop experiment workflow:
#   1. Generate a Stroop dataset (Excel file).
#   2. Create an output directory for the generated images.
#   3. Generate Stroop images based on the Excel data.

import sys
import os

# Step 0: Add the "Psycho" folder from the Psychophysics root directory to sys.path
# For example: C:\Users\wmjx2\Desktop\Psychophysics\Psycho
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
psycho_dir = os.path.join(root_dir, "Psycho")
if psycho_dir not in sys.path:
    sys.path.insert(0, psycho_dir)

# Debug: Print the contents of the Psycho folder to confirm that the Main module exists
print("Added to sys.path:", psycho_dir)
print("Contents of Psycho directory:", os.listdir(psycho_dir))

# Step 1: Import the Main module (Main.py contains data and image generation functions)
import Main

def run_stroop_experiment_workflow():
    # Step 1: Generate the Stroop dataset (choosing type1 version)
    print("Step 1: Generating Stroop dataset (type1)...")
    excel_file = Main.generate_stroop_letter_type1()
    print(f"Stroop dataset generated, file path: {excel_file}")

    # Step 2: Create an output directory for images (for example, a folder named "experiment_stimuli")
    output_dir = os.path.join(os.getcwd(), "experiment_stimuli")
    os.makedirs(output_dir, exist_ok=True)
    print(f"Image output directory created: {output_dir}")

    # (Optional) If you want the images to be saved in a custom directory, you can modify the storage logic
    # inside Main.generate_stroop_images_from_excel. Otherwise, this function will by default save images
    # to Data-set-Image/Stroop-Letter-image/<dataset_type>/.

    # Step 3: Generate Stroop images based on the generated Excel dataset
    print("Step 3: Generating Stroop images based on the dataset...")
    # Parameter description:
    #   excel_file: The generated Excel dataset file path.
    #   task: Fixed value "stroop".
    #   style: For Stroop experiments, fixed as "letter".
    #   dataset_type: Here, choose "type1".
    Main.generate_stroop_images_from_excel(excel_file, "stroop", "letter", "type1")
    print("Stroop images generation completed!")

if __name__ == "__main__":
    run_stroop_experiment_workflow()
