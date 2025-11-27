# Complete Procedure: Data Generation and Static Dashboard Creation

## 1. Environment Setup
- Ensure you have Python installed on your system.
- Create or activate your Python virtual environment (optional but recommended to isolate dependencies).
- Install the required libraries. Open a terminal (you can use PyCharm's terminal) in the project folder and run:
  ```bash
  pip install pandas matplotlib seaborn scipy
    ```
    *   `pandas`: For data manipulation.
    *   `matplotlib`: For generating static charts.
    *   `scipy`: For smoothing lines in the daily sales chart.
    *   `seaborn`: For enhanced visual styling.

## 2. Project Structure 

Make sure your ecommerce-dashboard folder contains the following files: 

*   `generate_data.py`: Script to generate the sample CSV data file.
*   `dashboard.py`: Script that reads the CSV and generates the three PNG charts.
*   `sales_data.csv` (This file will be generated after running `generate_data.py`).

## 3. Data Generation

   *   Open PyCharm's integrated Terminal (View -> Tool Windows -> Terminal).
   *   Ensure the working directory is your project folder `ecommerce-dashboard`. The command line should end with `ecommerce-dashboard>`.
   *   Run the data generation script:
    ```bash
    python generate_data.py
    ```
   *   This process will create (or overwrite) the `sales_data.csv` file in the same folder.
   *   Verify that the `sales_data.csv` file was generated correctly and contains data.


## 4. Running the Static Dashboard Generator

   *   Stay in the same terminal from the previous step (ensuring you are in the `ecommerce-dashboard` folder).
   *   Run the dashboard script:
    ```bash
    python dashboard.py
    ```
   *   This script will read sales_data.csv and generate three PNG files:
       *   total_sales_by_day.png
       *   monthly_sales.png
       *   top_products.png
         
   *   The script will print a confirmation message once the charts are created.

   *   Done! Your charts are now saved as PNG files in the same folder.

## 5. Possible Errors and Solutions

   *   File extension error: Ensure that the command `python nombre_archivo.py` uses the exact file name, including the `.py` extension.
   *   `sales_data.csv` not found: Ensure you have run `generate_data.py` before `dashboard.py`, and that both files are in the same folder.
   *   'ModuleNotFoundError': Ensure you have installed all required libraries (`pandas`, `matplotlib`, `seaborn`, `scipy`).
   *   PyCharm terminal starts in wrong directory: See section 6 to configure the terminal to start in the project folder.

## 6. Configuring PyCharm Terminal to Start in Project Directory 

To ensure the PyCharm terminal opens directly in your current project folder (`ecommerce-dashboard`), facilitating commands like `python dashboard.py`: 

   1. Open PyCharm and ensure your project (`ecommerce-dashboard`) is open.
   2. Go to the menu `File`.
   3. Select `Settings` (on Windows/Linux) or `PyCharm` -> `Preferences` (on macOS).
   4. In the settings window, look for the `Tools` option in the left panel.
   5. Under `Tools`, select `Terminal`.
   6. In the right panel, look for the "Shell path" section.
   7. Important: Look for an option like "Start directory:" or "Shell integration". What you are looking for is an option that says "Start directory: Project Directory" or "Start directory: Project Root" or "Start directory: [Variable] ProjectFileDir ". Ensure this is set to use the project folder.
   8. Click `OK` to save the changes.
   9. Close and reopen the integrated terminal in PyCharm. You can do this by closing the current terminal tab/panel and then going to `View` -> `Tool Windows` -> `Terminal` again.
   10. After applying this setting:
        * Every time you open the integrated terminal in PyCharm, it should open automatically in the root folder of your current project.
        * In the terminal command line, you should see the path to your `ecommerce-dashboard` folder `(e.g., (venv) C:\Users\xxxxxxxxxxx\PycharmProjects\Project Folder\ecommerce-dashboard>`).
        * With the terminal in the correct folder, you can run the command `python dashboard.py` directly.
         
     