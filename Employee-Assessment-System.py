Employee Assessment System
from flask import Flask, render_template_string, request, redirect, url_for
import csv
import os
app = Flask(name)
Dataset (embedded in the script)
EMPLOYEES_CSV = "employees.csv"
if not os.path.exists(EMPLOYEES_CSV):
with open(EMPLOYEES_CSV, mode='w', newline='') as file:
writer = csv.writer(file)
writer.writerow(['id', 'name', 'department', 'performance_score', 'attendance'])
writer.writerows([
[1, 'John Doe', 'Engineering', 85, 95],
[2, 'Jane Smith', 'Marketing', 90, 90],
[3, 'Alice Johnson', 'Sales', 78, 85],
[4, 'Bob Brown', 'HR', 88, 92],
[5, 'Charlie Davis', 'Engineering', 82, 88]
])
Load employee data from CSV
def load_employees():
employees = []
with open(EMPLOYEES_CSV, mode='r') as file:
reader = csv.DictReader(file)
for row in reader:
employees.append(row)
return employees

Save employee data to CSV
def save_employees(employees):
with open(EMPLOYEES_CSV, mode='w', newline='') as file:
fieldnames = ['id', 'name', 'department', 'performance_score', 'attendance']
writer = csv.DictWriter(file, fieldnames=fieldnames)
writer.writeheader()
for employee in employees:
writer.writerow(employee)
HTML Templates (embedded in the script)
INDEX_HTML = """
@app.route('/')
def index():
employees = load_employees()
return render_template_string(INDEX_HTML, employees=employees)
Assess an employee
@app.route('/assess/int:employee_id')
def assess(employee_id):
employees = load_employees()
employee = next((emp for emp in employees if int(emp['id']) == employee_id), None)
if employee:
return render_template_string(ASSESS_HTML, employee=employee)
return redirect(url_for('index'))
Update an employee's assessment
@app.route('/update/int:employee_id', methods=['POST'])
def update(employee_id):
employees = load_employees()
employee = next((emp for emp in employees if int(emp['id']) == employee_id), None)
if employee:
employee['performance_score'] = request.form['performance_score']
employee['attendance'] = request.form['attendance']
save_employees(employees)
return redirect(url_for('index'))
Run the application
if name == 'main':
app.run(debug=True)
Data set
id,name,department,performance_score,attendance
1,John Doe,Engineering,85,95
2,Jane Smith,Marketing,90,90

3,Alice Johnson,Sales,78,85
4,Bob Brown,HR,88,92
5,Charlie Davis,Engineering,82,88
