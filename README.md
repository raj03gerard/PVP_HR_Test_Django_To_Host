# PVP Project Documentation

The PVP project is developed using Python and the Django framework. It utilizes Python for backend functionality, HTML/CSS/JS for the frontend, and SQLite database for data storage.

## TLDR

- **Category class**: Creates categories like SCIENCE, HUMANITIES, ARTS, etc.
  - Each category has a passing mark, and students in a category must get a total of this passing mark or more in 2 subjects of that category.
  - By default, it has 2 categories - SCIENCE and HUMANITIES.

- **Subject class**: Creates subjects that belong to a category.
  - By default, it has 5 subjects: Maths, Biology, Japanese, English, History.

- **Student class**: Creates students that belong to a category.

- **TestConditions class**: Creates test conditions that evaluate if a student passes or fails.

- **Evaluation_Strategy class**: Creates evaluation strategies for determining if a student passes or fails.

## Project Directory Structure

```
PVP_students_test_app/        # Main project directory
|-- templates/                # Contains the HTML files
|-- static/                   # Contains all the CSS/JS files
|-- Modules/                  # Contains the Python modules/classes
|   |-- urls.py               # Contains routing information for different URLs
|   |-- views.py              # Starting point for the execution of the app
|   |-- Views_container/      # Contains other views files handling functionalities
|   |   |-- category_views.py # Handles creation of new categories
|   |   |-- student_views.py  # Handles creation of new students
|   |   |-- subject_views.py  # Handles creation of new subjects
|   |   |-- test_condition_views.py  # Handles updating test conditions
|   |-- models.py             # Contains classes for Student, Subject, Category, and Test_Conditions
|   |-- forms.py              # Creates individual forms for Student, Subject, and Category models
|   |-- apps.py               # Configures the app to run
|   |-- admin.py              # Registers models to the Django admin console
|-- evaluations/              # Evaluation related classes
|   |-- Evaluate_Results.py   # Handles evaluation of each student’s result
|   |-- evaluation_strategies.py/  # Contains different evaluation strategies
|   |   |-- Evaluation_Strategy.py      # Abstract class for evaluation strategies
|   |   |-- Evaluate_By_Total_Score.py  # Inherits Evaluation_Strategy class, evaluates based on total_score
|   |   |-- Evaluate_By_Marks_In_Category.py  # Inherits Evaluation_Strategy class, evaluates marks in category
|-- data_state_handle/        # Contains functions and data for default data creation
|   |-- default_data_creation.py   # Contains functions to create default data for the app
|   |-- default_data/         # Contains some default data (enums, colors, etc.)
|-- Migrations/               # Contains Django-generated files during data migration
```

## How to Use

- To get started, make sure you have Python and Django installed.
- Clone the project repository.
- Navigate to the project directory and run the development server.
- Access the app via the provided URLs.

Feel free to explore and modify the project as needed!
