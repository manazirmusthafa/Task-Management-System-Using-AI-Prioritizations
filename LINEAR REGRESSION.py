#!/usr/bin/env python
# coding: utf-8

# In[4]:


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
file_path = r'D:\minor project\task.csv'
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


# In[ ]:





# In[ ]:





# In[ ]:




