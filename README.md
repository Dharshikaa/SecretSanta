# Secret Santa Assignment

## Overview

This project automates the process of assigning Secret Santa pairings for employees while ensuring that no one is assigned to themselves or their previous year's recipient.

## Folder Structure

```
│── secretsanta/
│   ├── __init__.py
│   ├── file_handler.py       # Handles file operations
│   ├── santa_assigner.py     # Main logic for assignment
│   ├── errors.py             # Custom error handling
│── tests/
│   ├── test_santa_assigner.py   # Unit tests
│── README.md
│── requirements.txt
│── main.py                   # Entry point
│── Employee_List.xlsx
│── Secret-Santa-Game-Result-2023.xlsx
│── .gitignore
```

## Requirements

Ensure you have Python installed (version 3.x recommended) and the necessary dependencies installed.

### Install Dependencies

```bash
pip install -r requirements.txt
```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd <folder_name>
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Input Files

- **Employee\_List.xlsx**: Contains the list of employees participating in Secret Santa.
- **Secret-Santa-Game-Result-2023.xlsx**: Last year's Secret Santa assignments to prevent duplicate pairings.

## Output File

- **Secret-Santa-Game-Result-2024.csv**: The generated Secret Santa pairings for the current year.

## Features

- Ensures no self-assignment
- Prevents assigning the same recipient as the previous year
- Outputs assignments in a CSV format

## Error Handling

- Handles missing input files with appropriate error messages.
- Catches file read/write errors.

## Running Tests

Run the unit tests using:

```bash
pytest tests/
```

## Version Control

Ensure you commit changes and push to GitHub:

```bash
git add .
git commit -m "Updated Secret Santa assignments"
git push origin main
```

## Author

Dharshika Arivalagan

