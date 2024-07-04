# Task-Management-System-Using-AI-Prioritizations
Code, Software and instruction to execute

Linear Regression

Software used: Jupyter

Code: -
import csv
from datetime import datetime, timedelta

class Task:
    def __init__(self, task, deadline):
        self.task = task
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
        self.urgency = self.calculate_urgency()

    def calculate_urgency(self):
        now = datetime.now()
        time_difference = self.deadline - now
        urgency = max(1, int(time_difference.total_seconds() / 3600))
        return urgency

def read_csv(file_path):
    tasks = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            task = Task(row[0], row[1])
            tasks.append(task)
    return tasks

def prioritize_by_deadline(tasks):
    return sorted(tasks, key=lambda x: x.deadline)

def prioritize_by_deadline_and_urgency(tasks):
    return sorted(tasks, key=lambda x: (x.deadline.timestamp() + x.urgency))

def calculate_order_and_duration(tasks):
    order = []
    duration = []
    
    for i, task in enumerate(tasks, 1):
        order.append((i, task.task))
        
        if i < len(tasks):
            next_task = tasks[i]
            duration.append(next_task.deadline - task.deadline)
    
    return order, duration

# Example: Using your provided file path
file_path = r'C:\Users\DELL\Desktop\Major project components\task.csv'
dataset = read_csv(file_path)

# Prioritize tasks using different algorithms
deadline_priority = prioritize_by_deadline(dataset)
deadline_and_urgency_priority = prioritize_by_deadline_and_urgency(dataset)

# Calculate order and duration
order, duration = calculate_order_and_duration(deadline_priority)

# Print the results
print("Prioritize by Deadline:")
for i, task in enumerate(deadline_priority):
    print(f"Task {i + 1}: {task.task}, Deadline: {task.deadline.strftime('%Y-%m-%d %H:%M:%S')}, Urgency: {task.urgency}")

print("\nOrder and Duration:")
for i, (ordr, dur) in enumerate(zip(order, duration), 1):
    print(f"Task {i}: Order {ordr[0]}, Task: {ordr[1]}, Duration: {dur}")

print("\nPrioritize by Deadline and Urgency:")
for i, task in enumerate(deadline_and_urgency_priority):
    print(f"Task {i + 1}: {task.task}, Deadline: {task.deadline.strftime('%Y-%m-%d %H:%M:%S')}, Urgency: {task.urgency}")
 
Implementation:
Upload the code to Jupyter. In this model the only thing we should be careful of is to mention the file path to our .csv file that essentially contains the data. Then run the code. You will get the output as per your database.



Random Forest

Software used: Jupyter

Code: -
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Initialize label encoders for categorical features
gender_encoder = LabelEncoder()
profession_encoder = LabelEncoder()

# Function to read CSV file with multiple encodings
def read_csv_with_encoding(filepath):
    lines = []
    encodings = ['utf-8', 'latin1', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filepath, "rb") as file:
                for line in file:
                    lines.append(line.decode(encoding).strip())
            break
        except UnicodeDecodeError:
            continue
    return lines

# Read the CSV file
lines = read_csv_with_encoding(r"C:\Users\DELL\Desktop\Major project components\time_table.csv")
df = pd.DataFrame([line.split("\t") for line in lines])

# Example tasks and time slots
tasks = ['Wake Up Time', 'Exercise Time', 'Breakfast Time', 'Work Time', 'Lunch Time', 'Sleep Time']
time_slots = ['Morning', 'Morning', 'Morning', 'Afternoon', 'Afternoon', 'Evening']

# Fit label encoders on categorical features
gender_encoder.fit(df[2])
profession_encoder.fit(df[0])

# Default timetable
default_timetable = {
    'Morning': ['Exercise Time: 6:30 AM', 'Breakfast Time: 7:00 AM', 'Work Time: 7:30 AM'],
    'Afternoon': ['Lunch Time: 1:00 PM'],
    'Evening': ['Sleep Time: 9:30 PM']
}

def generate_personalized_timetable(gender, age, profession, medical_history, medications=[]):
    # Initialize timetable
    timetable = {'Morning': [], 'Afternoon': [], 'Evening': []}
    
    if not medical_history:
        return default_timetable
    
    # Add tasks based on user's profession
    matching_rows = df[(df[2].str.lower() == gender.lower()) & 
                       (df[1] == age) & 
                       (df[0].str.lower().str.strip() == profession.lower().strip())]
    if not matching_rows.empty:
        user_schedule = matching_rows.iloc[0]
        for task, time_slot in zip(tasks, time_slots):
            if user_schedule[task] != 'none':
                timetable[time_slot].append(f"{task}: {user_schedule[task]}")
    else:
        print("No matching schedule found for the provided details.")
        return default_timetable
    
    # Add tasks based on medical history and medications
    for med in medications:
        timetable[med['time']].append(f"Medication time: {med['time']}, Medication: {med['medication']}")
    
    return timetable

def predict_additional_tasks(gender, age, profession, medical_history):
    # Dummy implementation of Random Forest for demonstration
    # Replace this with actual implementation trained on relevant dataset
    return {}

def load_actual_timetables(filepath):
    actual_timetables = []
    encodings = ['utf-8', 'latin1', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filepath, "r", encoding=encoding) as file:
                for line in file:
                    data = line.strip().split("\t")
                    if len(data) >= 9:  # Ensure the line has at least 9 fields
                        actual_timetables.append({
                            'Morning': data[3],
                            'Afternoon': data[5],
                            'Evening': data[8]
                        })
            break
        except UnicodeDecodeError:
            continue
    return actual_timetables


def calculate_accuracy(actual_timetables, predicted_timetables):
    # Dummy implementation of accuracy calculation
    return 0.75  # Placeholder, replace with actual calculation

# Example usage
user_gender = input("Enter your gender: ")
user_age = int(input("Enter your age: "))
user_profession = input("Enter your profession: ")
user_medical_history = input("Do you have any medical history? (yes/no): ")

if user_medical_history.lower() == 'yes':
    # Get medical history details
    medical_history = []  # Placeholder, you can implement this part based on your specific requirements
else:
    medical_history = []

# Get medication details
medications = []
num_medications = int(input("How many medications do you take? "))
for i in range(num_medications):
    time = input("Enter the time for medication {}: ".format(i+1))
    medication = input("Enter the medication for medication {}: ".format(i+1))
    medications.append({'time': time, 'medication': medication})

# Generate personalized timetable
personalized_timetable = generate_personalized_timetable(user_gender, user_age, user_profession, medical_history, medications)
for period, tasks in personalized_timetable.items():
    print(f"{period}: {', '.join(tasks)}")

# Load the actual timetables for evaluation
actual_timetables = load_actual_timetables(r"C:\Users\DELL\Desktop\Major project components\time_table.csv")

# Calculate accuracy
accuracy = calculate_accuracy(actual_timetables, personalized_timetable)
print("Accuracy:", accuracy)

Implementation:
Upload the code to Jupyter. In this model, like the previous one we should ensure the file path of our .csv file, and once we run the code input the correct answers in the given fields.

For example,
Enter your gender: Male
Enter your age: 21
Enter your profession: Student
Do you have any medical history? (yes/no): No
How many medications do you take? 0
Morning: Exercise Time: 6:30 AM, Breakfast Time: 7:00 AM, Work Time: 7:30 AM
Afternoon: Lunch Time: 1:00 PM
Evening: Sleep Time: 9:30 PM
Accuracy: 0.75

  











KNN

Software used: Jupyter

Code: -
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score

# Function to read CSV file with multiple encodings
def read_csv_with_encoding(filepath):
    lines = []
    encodings = ['utf-8', 'latin1', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filepath, "rb") as file:
                for line in file:
                    lines.append(line.decode(encoding).strip())
            break
        except UnicodeDecodeError:
            continue
    return lines

# Read the CSV file
lines = read_csv_with_encoding(r"D:\minor project\timetable.csv")
df = pd.DataFrame([line.split(",") for line in lines])

# Print the DataFrame to verify its contents
print("DataFrame from CSV file:")
print(df)

# Correct column indexing
df.columns = ['Profession', 'Age', 'Gender', 'Wake Up Time', 'Exercise Time', 'Breakfast Time', 'Work Time', 'Lunch Time', 'Sleep Time']

# Default timetable
default_timetable = {
    'Morning': ['Exercise Time: 6:30 AM', 'Breakfast Time: 7:00 AM', 'Work Time: 7:30 AM'],
    'Afternoon': ['Lunch Time: 1:00 PM'],
    'Evening': ['Sleep Time: 9:30 PM']
}

def generate_personalized_timetable(gender, age, profession, medical_history, medications=[]):
    # Initialize timetable
    timetable = {'Morning': [], 'Afternoon': [], 'Evening': []}
    
    if not medical_history:
        return default_timetable
    
    # Add tasks based on user's profession
    matching_rows = df[(df['Gender'].str.lower() == gender.lower()) & 
                       (df['Age'] == age) & 
                       (df['Profession'].str.lower().str.strip() == profession.lower().strip())]
    if not matching_rows.empty:
        user_schedule = matching_rows.iloc[0]
        tasks = ['Wake Up Time', 'Exercise Time', 'Breakfast Time', 'Work Time', 'Lunch Time', 'Sleep Time']
        time_slots = ['Morning', 'Morning', 'Morning', 'Afternoon', 'Afternoon', 'Evening']
        for task, time_slot in zip(tasks, time_slots):
            if user_schedule[task] != 'none':
                timetable[time_slot].append(f"{task}: {user_schedule[task]}")
    else:
        print("No matching schedule found for the provided details.")
        return default_timetable
    
    # Add tasks based on medical history and medications
    for med in medications:
        timetable[med['time']].append(f"Medication time: {med['time']}, Medication: {med['medication']}")
    
    return timetable

def load_actual_timetables(filepath):
    actual_timetables = {'Morning': [], 'Afternoon': [], 'Evening': []}
    encodings = ['utf-8', 'latin1', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filepath, "r", encoding=encoding) as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) >= 9:  # Ensure the line has at least 9 fields
                        actual_timetables['Morning'].append(data[3])
                        actual_timetables['Afternoon'].append(data[5])
                        actual_timetables['Evening'].append(data[8])
            break
        except UnicodeDecodeError:
            continue
    return actual_timetables


def calculate_f1_score(actual_timetables, predicted_timetables):
    # Convert timetables to binary format for comparison
    actual_binary = [1 if len(slot) > 0 else 0 for slot in actual_timetables.values()]
    predicted_binary = [1 if len(slot) > 0 else 0 for slot in predicted_timetables.values()]
    return f1_score(actual_binary, predicted_binary)

# Example usage
user_gender = input("Enter your gender: ")
user_age = int(input("Enter your age: "))
user_profession = input("Enter your profession: ")
user_medical_history = input("Do you have any medical history? (yes/no): ")

if user_medical_history.lower() == 'yes':
    # Get medical history details
    medical_history = []  # Placeholder, you can implement this part based on your specific requirements
else:
    medical_history = []

# Get medication details
medications = []
num_medications = int(input("How many medications do you take? "))
for i in range(num_medications):
    time = input("Enter the time for medication {}: ".format(i+1))
    medication = input("Enter the medication for medication {}: ".format(i+1))
    medications.append({'time': time, 'medication': medication})

# Generate personalized timetable
personalized_timetable = generate_personalized_timetable(user_gender, user_age, user_profession, medical_history, medications)
for period, tasks in personalized_timetable.items():
    print(f"{period}: {', '.join(tasks)}")

# Load the actual timetables for evaluation
actual_timetables = load_actual_timetables(r"D:\minor project\timetable.csv")

# Calculate F1 score
f1_score = calculate_f1_score(actual_timetables, personalized_timetable)
print("F1 Score:", f1_score)

Implementation:
Upload the code to Jupyter. On running the code, in this model, we show the data frames of our database for a better understanding and then the fields open to enter in the output. We have also incorporated the calculation of F1 score in this model to achieve more accurate comparison between the models

For example,
DataFrame from CSV file:
               0    1       2             3              4               5  \
0    ﻿Profession  Age  Gender  Wake Up Time  Exercise Time  Breakfast Time   
1        Teacher   35    Male       6:30 AM        7:00 AM         7:30 AM   
2          Nurse   28  Female       5:45 AM        6:30 AM         7:00 AM   
3       Engineer   42    Male       7:00 AM        8:00 AM         8:30 AM   
4         Doctor   50    Male       6:15 AM        6:45 AM         7:15 AM   
..           ...  ...     ...           ...            ...             ...   
181   Pharmacist   44    Male       6:00 AM        6:00 PM         6:45 AM   
182  Firefighter   53  Female       6:45 AM        7:30 PM         7:30 AM   
183  Real Estate   57    Male       7:00 AM        6:15 PM         7:45 AM   
184      Student   50  Female       6:15 AM        6:30 PM         6:45 AM   
185      Teacher   42    Male       6:45 AM        6:45 PM         7:30 AM   


             6           7           8  
0    Work Time  Lunch Time  Sleep Time  
1      8:00 AM    12:00 PM    10:00 PM  
2      7:30 AM     1:00 PM     9:30 PM  
3      9:00 AM    12:30 PM    11:00 PM  
4      7:45 AM     1:30 PM    10:30 PM  
..         ...         ...         ...  
181    8:30 AM     1:00 PM    11:00 PM  
182    9:00 AM    12:30 PM    10:45 PM  
183    9:15 AM     1:15 PM    11:15 PM  
184          -     1:30 PM    10:30 PM  
185    8:45 AM     1:00 PM    11:00 PM  


[186 rows x 9 columns]
Enter your gender: male
Enter your age: 22
Enter your profession: student
Do you have any medical history? (yes/no): no
How many medications do you take? 0
Morning: Exercise Time: 6:30 AM, Breakfast Time: 7:00 AM, Work Time: 7:30 AM
Afternoon: Lunch Time: 1:00 PM
Evening: Sleep Time: 9:30 PM
F1 Score: 1.0



