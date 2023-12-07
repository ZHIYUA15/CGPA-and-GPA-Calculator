import json


class CGPACalculator:
    def __init__(self, file_path, grading_scale):
        self.file_path = file_path
        self.grading_scale = grading_scale

    def read_grades(self):
        courses = []
        with open(self.file_path, 'r') as file:
            for line in file:
                # Skip lines that don't start with a curly brace
                if not line.strip().startswith('{'):
                    continue

                # Use json.loads instead of eval for safety
                try:
                    course = json.loads(line.strip().rstrip(','))
                    courses.append(course)
                except json.JSONDecodeError:
                    # Handle or log the error if needed
                    pass
        return courses

    def calculate_cgpa(self):
        courses = self.read_grades()
        total_grade_points = sum(
            self.grading_scale[course["grade"]] * course["units"] for course in courses)
        total_units = sum(course["units"] for course in courses)
        return total_grade_points / total_units if total_units != 0 else 0


# Define the grading scale
grading_scale = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0
}

# Path to the grades file
file_path = r'C:\Users\LiZhiyuan\OneDrive - lixiaomi2002\桌面\CGPA\grades.txt'

# Create an instance of the CGPACalculator
cgpa_calculator = CGPACalculator(file_path, grading_scale)

# Calculate the CGPA
cgpa = cgpa_calculator.calculate_cgpa()

# Print the CGPA
print(f"\n----------------------------------\n")
print(f"Calculated CGPA: {cgpa:.1f}")
print(f"\n----------------------------------\n")
