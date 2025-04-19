# Program Name: Assignment5.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: Caitlin Johnson
# Assignment Number: Lab5
# Due Date: 04/18/ 2025
# Purpose: What does the program do (in a few sentences)? This Python program reads daily temperature data from an external text file and stores it in a SQLite database. 
# List Specific resources used to complete the assignment:  Python.org, W3Schools, Stack Overflow, SQLite.org

import sqlite3
import os


conn = sqlite3.connect('Assignment5_temperatures.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS temperatures (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Day_Of_Week TEXT NOT NULL,
        Temperature_Value REAL NOT NULL
    )
''')


input_file = 'Assignment5input.txt'

if os.path.exists(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                print(f"Skipping malformed line: {line.strip()}")
                continue
            day, temp = parts
            try:
                cursor.execute(
                    'INSERT INTO temperatures (Day_Of_Week, Temperature_Value) VALUES (?, ?)',
                    (day, float(temp))
                )
            except ValueError:
                print(f"Skipping bad data: {line.strip()}")
else:
    print(f"File not found: {input_file}")
    conn.close()
    exit()

conn.commit()

for day in ['Sunday', 'Thursday']:
    cursor.execute('SELECT AVG(Temperature_Value) FROM temperatures WHERE Day_Of_Week = ?', (day,))
    avg_temp = cursor.fetchone()[0]
    if avg_temp is not None:
        print(f'Average temperature for {day}: {avg_temp:.2f}°F')
    else:
        print(f'No temperature data for {day}')


conn.close()
