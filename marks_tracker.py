# VITyarthi-project

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# data storage list
students_data = []
# making 8 courses
courses = [f"Course_{i+1}" for i in range(8)]
# saving data to excel
def save_to_excel():
    if not students_data:
        messagebox.showerror("Error", "No data to save!")
        return
    
df = pd.DataFrame(students_data)
df.to_excel("Marks_Tracker.xlsx", index=False)
    
messagebox.showinfo("Success", "Data saved to Excel successfully!")
  # adding student record
def add_record():

  student_id = entry_student_id.get()

  if not student_id:
      messagebox.showerror("Error", "Enter Student ID")
      return

  marks = []
  try:
      for e in entries:
          marks.append(int(e.get()))
  except:
      messagebox.showerror("Error", "All marks must be integers!")
      return

  total_marks = sum(marks)
  # making dictionary to store data
  data = {"Student_ID": student_id}
  for i in range(8):
      data[courses[i]] = marks[i]
  data["Total"] = total_marks

  students_data.append(data)
  
  # Insert in Treeview
  tree.insert("", tk.END, values=[student_id] + marks + [total_marks])

   # Clear fields
  entry_student_id.delete(0, tk.END)
  for e in entries:
      e.delete(0, tk.END)

  # GUI Window
  root = tk.Tk()
  root.title("Marks Tracker System")
  root.geometry("900x600")
  root.config(bg="#f0f0f0")

title = tk.Label(root, text="College Marks Tracker", font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)
# input frame
frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
frame.pack(pady=10)
# Student ID
tk.Label(frame, text="Student ID:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10)
entry_student_id = tk.Entry(frame, font=("Arial", 12))
entry_student_id.grid(row=0, column=1, padx=10, pady=10)
# Course Inputs
entries = []
for i in range(8):
    tk.Label(frame, text=f"{courses[i]}:", font=("Arial", 12), bg="white").grid(row=(i//2)+1, column=(i%2)*2, padx=10, pady=5)
    e = tk.Entry(frame, font=("Arial", 12), width=10)
    e.grid(row=(i//2)+1, column=(i%2)*2 + 1, padx=10, pady=5)
    entries.append(e)
# Add Record Button
btn_add = tk.Button(root, text="Add Record", font=("Arial", 14), bg="#4CAF50", fg="white", command=add_record)
btn_add.pack(pady=10)

# table view
columns = ["Student_ID"] + courses + ["Total"]
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=90)

tree.pack(pady=10)
# save button

btn_save = tk.Button(root, text="Save to Excel", font=("Arial", 14), bg="#2196F3", fg="white", command=save_to_excel)
btn_save.pack(pady=20)


root.mainloop()



  


  

  

