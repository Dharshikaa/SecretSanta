from secretsanta.santa_assigner import SantaAssigner

def main():
    employees_file = "Employee-List.xlsx"
    previous_results_file = "Secret-Santa-Game-Result-2023.xlsx"
    output_file = "Secret-Santa-Assignments-2024.csv"
    
    assigner = SantaAssigner(employees_file, previous_results_file, output_file)
    assigner.run()

if __name__ == "__main__":
    main()
