import random
from secretsanta.file_handler import FileHandler

class SantaAssigner:
    """Handles the Secret Santa assignment logic."""
    
    def __init__(self, employees_file, previous_results_file, output_file):
        self.employees_file = employees_file
        self.previous_results_file = previous_results_file
        self.output_file = output_file
        self.employees = []
        self.previous_assignments = {}
        self.current_assignments = {}
    
    def load_data(self):
        """Loads employee data and previous assignments."""
        self.employees = FileHandler.load_employees(self.employees_file)
        self.previous_assignments = FileHandler.load_previous_assignments(self.previous_results_file)
    
    def assign_secret_santa(self):
        """Assigns Secret Santa while avoiding self-matching and previous year’s assignments."""
        employees = self.employees.copy()
        random.shuffle(employees)
        
        available_children = set(employees)
        for emp in employees:
            possible_choices = available_children - {emp} - {self.previous_assignments.get(emp[0])}
            
            if not possible_choices:
                return False  # Restart the process if no valid assignments found
            
            chosen_child = random.choice(list(possible_choices))
            self.current_assignments[emp] = chosen_child
            available_children.remove(chosen_child)
        return True
    
    def generate_assignments(self):
        """Retries assignment until a valid configuration is found."""
        success = False
        while not success:
            self.current_assignments.clear()
            success = self.assign_secret_santa()
    
    def run(self):
        """Runs the full Secret Santa assignment process."""
        self.load_data()
        self.generate_assignments()
        FileHandler.save_results(self.output_file, self.current_assignments)
        print("Secret Santa assignment completed successfully!")
