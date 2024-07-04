#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
lines = read_csv_with_encoding("D:/minor project/time_table.csv")
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
actual_timetables = load_actual_timetables("D:/minor project/time_table.csv")

# Calculate accuracy
accuracy = calculate_accuracy(actual_timetables, personalized_timetable)
print("Accuracy:", accuracy)


# In[3]:


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


# In[ ]:




