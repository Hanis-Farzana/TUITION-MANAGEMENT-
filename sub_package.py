import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tuition_management"
)

mycursor = mydb.cursor()

# Global list to store total prices
total_prices_list = []

def collect_data():
    stu_name = stu_name_entry.get()
    stu_id = stu_id_entry.get()
    subject_package = package_var.get()

    # Prices for different packages
    prices = {
        "Package 1": 58,
        "Package 2": 58,
        "Package 3": 68,
        "Package 4": 78,
        "Package 5": 98,
    }

    total_price = prices[subject_package] + 450

    # Check if the selected package is Package 5
    if subject_package == "Package 5":
        # Apply a 15% discount
        discount_amount = 0.15 * total_price
        disc_price = total_price - discount_amount
        output_label.config(text=f"Total Price: RM{disc_price:.2f}")
    else:
        # For other packages, no discount is applied
        disc_price = total_price
        output_label.config(text=f"Total Price: RM{disc_price:.2f}")

    # Insert data into the database
    sql = "INSERT INTO subject_information (stu_name, stu_id, sub_package, total_price) VALUES (%s, %s, %s, %s)"
    val = (stu_name, stu_id, subject_package, disc_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # Update the output label
    output_label.config(text=f"Package: {subject_package}, Total Price: RM{disc_price:.2f}")

def remove_student():
    try:
        stu_id = int(stu_id_entry.get())

        # Delete data from the database
        sql = "DELETE FROM subject_information WHERE stu_id=%s"
        val = (stu_id,)  # Ensure that val is a tuple
        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Student data deleted successfully")
    except ValueError:
        messagebox.showerror("Error", "Invalid input for student ID.")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "An error occurred while deleting the student data.")

def student_update():
    try:
        stu_id = int(stu_id_entry.get())
        new_subject_package = package_var.get()

        # Assuming package_var is a Tkinter StringVar associated with a widget
        if not new_subject_package:
            messagebox.showerror("Error", "Please select a subject package.")
            return

        # Assuming the primary key for the student is stu_id
        sql = "UPDATE subject_information SET sub_package=%s WHERE stu_id=%s"
        val = (new_subject_package, stu_id)

        mycursor.execute(sql, val)
        mydb.commit()

        messagebox.showinfo("Success", "Student information updated!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input for student ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create Window
root = tk.Tk()
root.title("Tuition Management System")
root.geometry("800x800")
root.configure(bg="salmon1")


# Title
label = tk.Label(root, text="Package Price", font=("", 10, "bold"), bg= "salmon1")
label.grid(ipadx=10, ipady=10)

# Prices text
prices_text = tk.Text(root, height=17, width=85, font=("Helvetica", 10))
prices_text.grid(row=2, column=0)

prices_text.insert(tk.END, "Package & Fees:\n\n")
prices_text.insert(tk.END, "Package 1: BM & BI \nPrice: RM58\n\n")
prices_text.insert(tk.END, "Package 2: MATHS & SCIENCE \nPrice: RM58\n\n")
prices_text.insert(tk.END, "Package 3: BM & HISTORY \nPrice: RM68\n\n")
prices_text.insert(tk.END, "Package 4: MATHS, SCIENCE, HISTORY \nPrice: RM78\n\n")
prices_text.insert(tk.END, "Package 5: BM, BI, MATHS, SCIENCE, HISTORY \nPrice: RM98\n\n")
prices_text.insert(tk.END, "Fees: RM450 per person\n\n")
prices_text.insert(tk.END, "Discount: 10% off for Package 5 only \n") 
prices_text.configure(state='disabled')

# Frame
frame = tk.Frame(root)
frame.grid()

# Student Information Frame
stu_info_frame = tk.LabelFrame(frame, text="")
stu_info_frame.grid(row=0, column=0, padx=20, pady=10)

stu_name_label = tk.Label(stu_info_frame, text="Student Name:", width=50)
stu_name_label.grid(row=0, column=0)

stu_name_entry = tk.Entry(stu_info_frame, width=50)
stu_name_entry.grid(row=1, column=0)

stu_id_label = tk.Label(stu_info_frame, text="Student Identification Number:", width=50)
stu_id_label.grid(row=0, column=1)

stu_id_entry = tk.Entry(stu_info_frame, width=50)
stu_id_entry.grid(row=1, column=1)

package_label = tk.Label(stu_info_frame, text="Subject Package:", width=50)
package_label.grid(row=3, column=0)

package_var = tk.StringVar(stu_info_frame)
package_var.set("Select Subject Package")
package_dropdown = tk.OptionMenu(stu_info_frame, package_var, "Package 1", "Package 2", "Package 3", "Package 4", "Package 5")
package_dropdown.grid(row=4, column=0)

# Button
add_button = tk.Button(root, text="Add Student", command=collect_data)
add_button.grid(pady=10)

# Delete Button
button_frame = tk.LabelFrame(root, text="")
button_frame.grid(row=10, column=0, padx=10, pady=10)
delete_button = tk.Button(button_frame, text="Remove", command=remove_student)
delete_button.grid(row=10, column=1, pady=15)

# Update Button
update_button = tk.Button(button_frame, text="Update", command= student_update)
update_button.grid(row=10, column=0, pady=10)

# Total Price Label
label = tk.Label(root, text='Total Price', font=("Times New Romans", 12), bg="salmon1")
label.grid(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.grid()


root.mainloop()