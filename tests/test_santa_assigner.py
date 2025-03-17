import unittest
from secretsanta.santa_assigner import SantaAssigner
from secretsanta.file_handler import FileHandler

class TestSantaAssigner(unittest.TestCase):
    """Unit tests for the SantaAssigner class."""
    
    def setUp(self):
        """Set up test data."""
        self.employees_file = "test_employees.xlsx"
        self.previous_results_file = "test_previous_results.xlsx"
        self.output_file = "test_output.csv"
        self.assigner = SantaAssigner(self.employees_file, self.previous_results_file, self.output_file)
    
    def test_load_data(self):
        """Test loading employee data and previous assignments."""
        self.assigner.load_data()
        self.assertGreater(len(self.assigner.employees), 0, "Employees should be loaded.")
    
    def test_assign_secret_santa(self):
        """Test Secret Santa assignment logic."""
        self.assigner.load_data()
        success = self.assigner.assign_secret_santa()
        self.assertTrue(success, "Secret Santa assignment should be successful.")
        self.assertEqual(len(self.assigner.current_assignments), len(self.assigner.employees), "Every employee should be assigned a Secret Santa.")
    
    def test_generate_assignments(self):
        """Test generating valid assignments."""
        self.assigner.load_data()
        self.assigner.generate_assignments()
        self.assertEqual(len(self.assigner.current_assignments), len(self.assigner.employees), "Assignments should be generated correctly.")
    
    def test_save_results(self):
        """Test saving results to a CSV file."""
        self.assigner.load_data()
        self.assigner.generate_assignments()
        FileHandler.save_results(self.output_file, self.assigner.current_assignments)
        with open(self.output_file, 'r') as f:
            content = f.read()
        self.assertTrue(len(content) > 0, "Output file should not be empty.")

if __name__ == '__main__':
    unittest.main()
