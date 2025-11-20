# VITyarthi-project
A marks tracker system offering marks of 8 courses to be stored in excel form.
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

      



  


  

  

