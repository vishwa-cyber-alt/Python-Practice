
import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Establishing a connection to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="vishwa"
)
cursor = connection.cursor()

# Function to create a new record
def create_record():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    if not name or not age or not email:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be an integer")
        return
    
    sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    cursor.execute(sql, val)
    connection.commit()
    messagebox.showinfo("Success", "Record inserted successfully")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to read records from the table
def read_records():
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    if not records:
        messagebox.showinfo("Info", "No records found")
    else:
        record_text = "\n".join([f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}" for record in records])
        messagebox.showinfo("Records", record_text)

# Create a Tkinter window
window = tk.Tk()
window.title("Database Operations")

# Create labels and entry fields
tk.Label(window, text="Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Age:").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(window, text="Email:").grid(row=2, column=0, sticky="e")
email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons for insert and read operations
insert_button = tk.Button(window, text="Insert Record", command=create_record)
insert_button.grid(row=3, column=0, columnspan=2, pady=5)

read_button = tk.Button(window, text="Read Records", command=read_records)
read_button.grid(row=4, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
window.mainloop()

# Close the connection
connection.close()
