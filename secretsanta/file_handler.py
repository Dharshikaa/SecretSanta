import pandas as pd
import os

class FileHandler:
    """Handles file operations like reading employee data and previous results."""
    
    @staticmethod
    def load_employees(file_path):
        """Loads employee data from an Excel file."""
        try:
            df = pd.read_excel(file_path)
            return list(df.itertuples(index=False, name=None))
        except Exception as e:
            print(f"Error loading employees file: {e}")
            return []
    
    @staticmethod
    def load_previous_assignments(file_path):
        """Loads last year's Secret Santa assignments."""
        if not os.path.exists(file_path):
            return {}
        try:
            df = pd.read_excel(file_path)
            return {row[0]: row[2] for row in df.itertuples(index=False, name=None)}
        except Exception as e:
            print(f"Error loading previous assignments: {e}")
            return {}
    
    @staticmethod
    def save_results(output_file, assignments):
        """Saves the new Secret Santa assignments to a CSV file."""
        try:
            results = [(emp[0], emp[1], child[0], child[1]) for emp, child in assignments.items()]
            df = pd.DataFrame(results, columns=["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
            df.to_csv(output_file, index=False)
            print(f"Secret Santa assignments saved to {output_file}")
        except Exception as e:
            print(f"Error saving results: {e}")
