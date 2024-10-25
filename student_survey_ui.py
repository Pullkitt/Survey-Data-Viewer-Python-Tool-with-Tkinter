import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Function to load CSV file
def load_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            global df
            df = pd.read_csv('E:/python/survey_results.csv')
            messagebox.showinfo("Success", "CSV file loaded successfully!")
            update_table(df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {e}")

# Function to update table based on filters
def update_table(data):
    for row in table.get_children():
        table.delete(row)
    
    for index, row in data.iterrows():
        table.insert("", "end", values=list(row))

# Function to apply filters
def apply_filters():
    filtered_df = df.copy()
    
    # Age Filter
    age_value = age_var.get()
    if age_value != "All":
        filtered_df = filtered_df[filtered_df['What is your age?'] == age_value]
    
    # Gender Filter
    gender_value = gender_var.get()
    if gender_value != "All":
        filtered_df = filtered_df[filtered_df['What is your gender?'] == gender_value]

    # Year of Study Filter
    year_value = year_var.get()
    if year_value != "All":
        filtered_df = filtered_df[filtered_df['What year of study are you in?'] == year_value]
    
    update_table(filtered_df)

# Create the main window
root = tk.Tk()
root.title("Survey Data Viewer")
root.geometry("800x600")

# Load Button
load_button = tk.Button(root, text="Load CSV", command=load_csv)
load_button.pack(pady=10)

# Filters
frame = tk.Frame(root)
frame.pack(pady=10)

# Age Filter
tk.Label(frame, text="Age:").grid(row=0, column=0, padx=10)
age_var = tk.StringVar(value="All")
age_options = ["All", "16-18", "18-20", "21-23", "24-26", "27+"]
age_menu = ttk.Combobox(frame, textvariable=age_var, values=age_options, state="readonly")
age_menu.grid(row=0, column=1, padx=10)

# Gender Filter
tk.Label(frame, text="Gender:").grid(row=0, column=2, padx=10)
gender_var = tk.StringVar(value="All")
gender_options = ["All", "Male", "Female", "Non Binary", "Prefer not to say"]
gender_menu = ttk.Combobox(frame, textvariable=gender_var, values=gender_options, state="readonly")
gender_menu.grid(row=0, column=3, padx=10)

# Year of Study Filter
tk.Label(frame, text="Year of Study:").grid(row=1, column=0, padx=10)
year_var = tk.StringVar(value="All")
year_options = ["All", "First Year", "Second Year", "Third Year", "Fourth Year", "Graduate Student"]
year_menu = ttk.Combobox(frame, textvariable=year_var, values=year_options, state="readonly")
year_menu.grid(row=1, column=1, padx=10)

# Apply Filter Button
apply_button = tk.Button(frame, text="Apply Filters", command=apply_filters)
apply_button.grid(row=1, column=3, padx=10)

# Data Table
columns = ["What is your age?*", "What is your gender?*", "What year of study are you in?*", "What is your major field of study?",
           "On average, how many hours per day do you spend on academic work outside of class?*",
           "How often do you use a planner or digital calendar to organize your schedule?*",
           "Do you prioritize your tasks? If yes, how?", "How often do you find yourself procrastinating on important tasks?*",
           "What are your top 3 time-wasting activities?*", "How often do you feel overwhelmed by your workload?*",
           "Which of the following time management techniques have you tried?*"]

table = ttk.Treeview(root, columns=columns, show='headings', height=15)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor=tk.CENTER)

table.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
