import tkinter as tk
import mysql.connector 
from tkinter import messagebox

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_management"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def student_information():
    #function of button
    name = name_entry.get()
    email = email_entry.get()
    id = int(student_id_entry.get())
    number = no_phone_entry.get()
    password = password_entry.get()

    # print the information
    print("student information:")
    print("name:", name)
    print("email:", email)
    print("Student identification:", id)
    print("phone Number:", number)
    print("password:", password)

    #  insert database
    sql = "INSERT INTO `student_information` (student_name, student_email, student_id, phone_number, student_password) VALUES (%s, %s, %s,%s,%s)"
    val = (name, email, id, number, password)
    mycursor.execute(sql, val)
    mydb.commit()

def delete_student():
    try:
        student_id = int(student_id_entry.get())
        
        # Assuming student_id is the primary key for deletion
        sql = "DELETE FROM student_information WHERE student_id = %s"
        val = (student_id, )
        
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Data deleted successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")
    except Exception as e:
        messagebox.showerror("Error", str(e))



def update_student():
    try:
        student_id = int(student_id_entry.get())
        new_phone_number = no_phone_entry.get()
        new_email = email_entry.get()

        sql = "UPDATE student_information SET phone_number = %s, student_email = %s WHERE student_id = %s"
        val = (new_phone_number, new_email, student_id)
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Student information updated!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    
#GUI
root = tk.Tk()
root.title("Tuition Brainnies")
root.geometry('1000x900')
root.configure(bg="salmon1")
 
frame = tk.Frame(root,bg="salmon1")
frame.pack()
frame.config()

#page title 
label=tk.Label(root, text ='WELCOME TO BRAINNIES TUITION', font=("Times New Roman", 20, "bold", )) 
label.pack(padx=10, pady=10) 

#student information
stu_info_frame = tk.LabelFrame(frame, text="Student Information")
stu_info_frame.grid(row=3, column=0, ipadx=20, ipady=5)
stu_info_frame.configure(bg="salmon1", fg="saddle brown", font=("Helvatica",20, "bold"))

name_label = tk.Label(stu_info_frame, text="name")
name_label.grid(row=0, column=0)
name_label.configure(fg="brown", font=("Arial",12, "bold"))

name_entry = tk.Entry(stu_info_frame, width=50)
name_entry.grid(row=1, column=0, padx=60, pady=10)

email_label = tk.Label(stu_info_frame, text="email")
email_label.grid(row=2, column=0)
email_label.configure(fg="brown", font=("Arial",12, "bold"))

email_entry = tk.Entry(stu_info_frame, width=40)
email_entry.grid(row=3, column=0, padx=60, pady=10)

student_id_label= tk.Label(stu_info_frame, text="student identification")
student_id_label.grid(row=0, column=1)
student_id_label.configure(fg="brown", font=("Arial",12, "bold"))

student_id_entry = tk.Entry(stu_info_frame, width=50)
student_id_entry.grid(row=1, column=1, padx=60, pady=10)

no_phone_label= tk.Label(stu_info_frame, text="phone number")
no_phone_label.grid(row=2, column=1)
no_phone_label.configure(fg="brown", font=("Arial",12, "bold"))

no_phone_entry = tk.Entry(stu_info_frame, width=40)
no_phone_entry.grid(row=3, column=1, padx=60, pady=10)

password_label= tk.Label(stu_info_frame, text="password")
password_label.grid(row=4, column=0)
password_label.configure(fg="brown", font=("Arial",12, "bold"))

password_entry = tk.Entry(stu_info_frame, width=40)
password_entry.grid(row=5, column=0, padx=60, pady=10)

insert_button = tk.Button(stu_info_frame, text="Register", command=student_information)
insert_button.grid(row=5, column=1)
insert_button.configure(bg="chocolate3", fg="peach puff", font=("Arial", 12 , "bold"))


# Buttons for delete and update functions
delete_button = tk.Button(stu_info_frame, text="delete", command=delete_student)
delete_button.grid(row=5, column=0, columnspan=5, pady=10)
delete_button.configure(bg="chocolate3", fg="peach puff", font=("Arial", 12 , "bold"))

update_button = tk.Button(stu_info_frame, text="update", command=update_student)
update_button.grid(row=5, column=2, columnspan=4, pady=10)
update_button.configure(bg="chocolate3", fg="peach puff", font=("Arial", 12 , "bold"))

# Loop to keep the GUI running
while True:
    try:
        root.update()
    except tk.TclError:
        break  # Exit the loop if the user closes the window
root.mainloop()
