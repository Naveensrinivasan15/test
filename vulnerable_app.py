# vulnerable_app.py
# Intentionally Vulnerable Application
# For Educational Security Testing Only

import pickle
import sqlite3
import subprocess

tasks = []

# CRITICAL: Unsafe Deserialization
def load_tasks(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)


# HIGH: SQL Injection
def search_task(task_name):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE name = '" + task_name + "'"
    cursor.execute(query)

    results = cursor.fetchall()
    conn.close()

    return results


# CRITICAL: Command Injection
def ping_host(host):
    command = "ping -c 1 " + host
    return subprocess.getoutput(command)


# MEDIUM: Hardcoded Credentials
DATABASE_PASSWORD = "admin123"
SECRET_KEY = "my_secret_key_123"


# LOW: Missing Input Validation
def add_task(task):
    tasks.append(task)
    print("Task added:", task)


# Application Menu
if __name__ == "__main__":

    print("===== VULNERABLE TO-DO APPLICATION =====")
    print("1. Add Task")
    print("2. Search Task")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        name = input("Search task: ")
        print(search_task(name))

    elif choice == "3":
        print("Exiting application!")

    else:
        print("Invalid choice!")
