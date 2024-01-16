import tkinter as tk  
from tkinter import ttk 
from tkinter import messagebox 
import mysql.connector 
 
# Connect to your MySQL database 
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database="tuition_management" 
) 
 
# Create a cursor object to execute SQL queries 
mycursor = mydb.cursor() 
 
def collect_data(): 
    Student_identity = int(stu_entry.get()) 
    password = int(password_entry.get()) 
    selected_method = method_online.get() 
    selected_f2f_method = f2f_method.get() 
 
    print("Student:", Student_identity) 
    print("password student:", password) 
    print("method", selected_method) 
    print("f2f method", selected_f2f_method) 
 

# Inserting data into the database 
    try: 
        sql = "INSERT INTO tuition_branches (student_id, password, method, tui_area) VALUES (%s, %s, %s, %s)" 
        val = (Student_identity, password, selected_method, selected_f2f_method) 
        mycursor.execute(sql, val) 
        mydb.commit() 
 
    # To show the data entry is successful or not. 
        if not Student_identity or not password or not selected_method or not selected_f2f_method: 
             messagebox.showerror("Error", "Please fill in all fields and enter a valid data.") 
        else: 
         messagebox.showinfo('Success', "Student data submited successfully") 
      
    except ValueError: 
        messagebox.showinfo("Error", "Invalid input. Please enter valid numeric valus for id number and password") 
    
root= tk.Tk() 
root.title("brainnies tuition") 
root.geometry('600x600') 
root.configure(bg="salmon1")

frame = tk.Frame(root,bg="salmon1")
frame.pack()
frame.config()
 
#page title 
label=tk.Label(root, text ='WELCOME TO BRAINNIES TUITION', font=("Times New Roman", 20, "bold", )) 
label.pack(padx=10, pady=10) 
 
frame= tk.Frame(root, height=40, width=50) 
frame.pack(padx=20, pady=20) 
 
#student id 
stu_label= tk.Label(frame, text= "student identity\n" , font=("Times New Roman", 10,)) 
stu_label.grid(row=1, column=0, padx=4, pady=4) 
stu_entry = tk.Entry(frame) 
stu_entry.grid(row=2, column=0) 
 
password=tk.Label(frame, text= "password", font=("Times New Roman",10)) 
password.grid(row=3, column=0, padx=5, pady=5, ipadx=6, ipady=6) 
password_entry=tk.Entry(frame) 
password_entry.grid(row=4, column=0, padx=5, pady=5, ipadx=3, ipady=3) 
 
#method 
insert_info_frame = tk.LabelFrame(frame, text="\nCHOOSE YOUR METHOD\n") 
insert_info_frame.grid( row=6, column=0, ipadx=50, ipady=50) 
 
# Default value before your selection 
method_online = ttk.Combobox(insert_info_frame, values= ["face-to-face","online"]) 
method_online.grid(row=9, column=0, padx=5, pady=5, ipadx=7, ipady=7) 
method_online.set("Select Your Method") 
 
f2f_method=ttk.Combobox(insert_info_frame, values=["Kedah : Sungai Petani", "Kedah : Kulim",  
                                                         "Johor : Muar ","Johor : Pontian ", 
                                                         "Selangor : Shah Alam", "Selangor : Sepang","ZOOM", "WEBEX"]) 
f2f_method.set("Pick the Place") 
f2f_method.grid(row=13, column=0, padx=5, pady=5, ipadx=7, ipady=7) 
 
 
 # Save Button 
save_button = tk.Button(frame, text="Submit", command=collect_data,) 
 
command=(collect_data) 
save_button.grid(row=24, column=0, padx=5, pady=5, ipadx=5, ipady=5) 
 
 
 
root.mainloop()