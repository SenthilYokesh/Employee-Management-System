from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox


# SET DISPLAY
db = Database("employees.db")
root = Tk()
root.title("EMPLOYEE MANAGEMENT SYSTEM")
root.geometry("1366x768+0+0")
root.config(bg="gray20")
root.state("zoomed")

# SET EMPLOYEE DETAIL VARIABLES
# id, first_name, last_name, age, doj, email, gender, contact, address, dept, job_pos
first_name = StringVar()
last_name = StringVar()
age = StringVar()
doj = StringVar()
email = StringVar()
gender = StringVar()
contact = StringVar()
dept = StringVar()
job_pos = StringVar()

# ENTRIES FRAME
# Title
entries_frame = Frame(root, bg="gray19")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="EMPLOYEE MANAGEMENT SYSTEM", font=("Calibri", 20, "bold", "underline"), bg="gray19",
              fg="gray90")
title.grid(row=0, columnspan=4, padx=10, pady=20, sticky="n")

# First Name
label_first_name = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="gray19", fg="gray90")
label_first_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
text_first_name = Entry(entries_frame, textvariable=first_name, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_first_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Last Name
label_last_name = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="gray19", fg="gray90")
label_last_name.grid(row=1, column=2, padx=10, pady=10, sticky="w")
text_last_name = Entry(entries_frame, textvariable=last_name, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_last_name.grid(row=1, column=3, padx=10, pady=10, sticky="w")

# Age
label_age = Label(entries_frame, text="Age", font=("Calibri", 16), bg="gray19", fg="gray90")
label_age.grid(row=2, column=0, padx=10, pady=10, sticky="w")
text_age = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_age.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# D.O.J
label_doj = Label(entries_frame, text="D.O.J", font=("Calibri", 16), bg="gray19", fg="gray90")
label_doj.grid(row=4, column=0, padx=10, pady=10, sticky="w")
text_doj = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_doj.grid(row=4, column=1, padx=10, pady=10, sticky="w")

# Email ID
label_email = Label(entries_frame, text="Email ID", font=("Calibri", 16), bg="gray19", fg="gray90")
label_email.grid(row=2, column=2, padx=10, pady=10, sticky="w")
text_email = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_email.grid(row=2, column=3, padx=10, pady=10, sticky="w")

# Gender
label_gender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="gray19", fg="gray90")
label_gender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
combo_box_gender = ttk.Combobox(entries_frame, textvariable=gender, font=("Calibri", 16), width=39, state="readonly")
combo_box_gender["values"] = ("Male", "Female")
combo_box_gender.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Contact
label_contact = Label(entries_frame, text="Contact", font=("Calibri", 16), bg="gray19", fg="gray90")
label_contact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
text_contact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_contact.grid(row=3, column=3, padx=10, pady=10, sticky="w")

# Address
label_address = Label(entries_frame, text="Address", font=("Calibri", 16), bg="gray19", fg="gray90")
label_address.grid(row=4, column=2, padx=10, pady=10, sticky="w")
text_address = Text(entries_frame, width=40, height=5, font=("Calibri", 16), bg="gray88", fg="gray4")
text_address.grid(row=4, column=3, rowspan=3, padx=10, pady=10, sticky="w")

# Department
label_dept = Label(entries_frame, text="Department", font=("Calibri", 16), bg="gray19", fg="gray90")
label_dept.grid(row=5, column=0, padx=10, pady=10, sticky="w")
text_dept = Entry(entries_frame, textvariable=dept, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_dept.grid(row=5, column=1, padx=10, pady=10, sticky="w")

# Job Position
label_job_pos = Label(entries_frame, text="Job Position", font=("Calibri", 16), bg="gray19", fg="gray90")
label_job_pos.grid(row=6, column=0, padx=10, pady=10, sticky="w")
text_job_pos = Entry(entries_frame, textvariable=job_pos, font=("Calibri", 16), width=40, bg="gray88", fg="gray4")
text_job_pos.grid(row=6, column=1, padx=10, pady=10, sticky="w")


# ADD, UPDATE, CLEAR, DELETE, DISPLAY ALL
# Get Data(event) hint: click to display
def get_data(event):
    selected_row = tree_view.focus()
    data = tree_view.item(selected_row)
    global row
    row = data["values"]
    # print(row)
    first_name.set(row[1])
    last_name.set(row[2])
    age.set(row[3])
    doj.set(row[4])
    email.set(row[5])
    gender.set(row[6])
    contact.set(row[7])
    text_address.delete(1.0, END)
    text_address.insert(END, row[8])
    dept.set(row[9])
    job_pos.set(row[10])


# Display All
def display_all():
    tree_view.delete(*tree_view.get_children())
    for row in db.display():
        tree_view.insert("", END, values=row)


# Add
def add_employee():
    if text_first_name.get() == "" or text_last_name.get() == "" or text_age.get() == "" or text_doj.get() == "" or text_email.get() == "" or combo_box_gender.get() == "" or text_contact.get() == "" or text_dept.get() == "" or text_job_pos.get() == "" or text_address.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.insert(text_first_name.get(), text_last_name.get(), text_age.get(), text_doj.get(), text_email.get(),
              combo_box_gender.get(), text_contact.get(), text_address.get(1.0, END), text_dept.get(),
              text_job_pos.get())
    clear_all()
    display_all()
    messagebox.showinfo("Success", "Record Added")


# Update
def update_employee():
    if text_first_name.get() == "" or text_last_name.get() == "" or text_age.get() == "" or text_doj.get() == "" or text_email.get() == "" or combo_box_gender.get() == "" or text_contact.get() == "" or text_address.get(
            1.0, END) == "" or text_dept.get() == "" or text_job_pos.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return
    db.update(row[0], text_first_name.get(), text_last_name.get(), text_age.get(), text_doj.get(), text_email.get(),
              combo_box_gender.get(), text_contact.get(), text_address.get(1.0, END), text_dept.get(),
              text_job_pos.get())
    clear_all()
    display_all()
    messagebox.showinfo("Success", "Record Updated")


# Clear All
def clear_all():
    first_name.set("")
    last_name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    text_address.delete(1.0, END)
    dept.set("")
    job_pos.set("")


# Delete
def delete_employee():
    db.delete(row[0])
    clear_all()
    display_all()
    messagebox.showinfo("Success", "Record Deleted")


# SET BUTTONS
button_frame = Frame(entries_frame, bg="gray20")
button_frame.grid(row=7, column=0, padx=10, pady=10, sticky="w", columnspan=4)

# add button
add_button = Button(button_frame, command=add_employee, text="Add Details", font=("Calibri", 16, "bold"), width=25,
                    fg="gray75", bg="dark slate gray", bd=0)
add_button.grid(row=0, column=0, padx=10)

# update button
update_button = Button(button_frame, command=update_employee, text="Update Details", font=("Calibri", 16, "bold"),
                       width=25, fg="gray75", bg="dark olive green", bd=0)
update_button.grid(row=0, column=2, padx=10)

# clear all button
clear_all_button = Button(button_frame, command=clear_all, text="Clear Details", font=("Calibri", 16, "bold"),
                          width=25, fg="gray75", bg="skyblue4", bd=0)
clear_all_button.grid(row=0, column=4, padx=10)

# delete button
delete_button = Button(button_frame, command=delete_employee, text="Delete Details", font=("Calibri", 16, "bold"),
                       width=25, fg="gray75", bg="indianred4", bd=0)
delete_button.grid(row=0, column=6, padx=10)

# TABLE FRAME(Treeview)
tree_frame = Frame(root, bg="gray22")
tree_frame.place(x=0, y=450, width=1366, height=240)

style = ttk.Style()
style.theme_use("clam")
style.configure("mystyle.Treeview", font=("Calibri", 14), rowheight=50, foreground="gray85", background="gray22")
style.configure("mystyle.Treeview.Heading", foreground="gray20", font=("Calibri", 15, "bold"), background="gray80")

tree_view = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), style="mystyle.Treeview")
# heading for table
tree_view.heading("1", text="ID")
tree_view.heading("2", text="First Name")
tree_view.heading("3", text="Last Name")
tree_view.heading("4", text="Age")
tree_view.heading("5", text="D.O.B")
tree_view.heading("6", text="Email")
tree_view.heading("7", text="Gender")
tree_view.heading("8", text="Contact")
tree_view.heading("9", text="Address")
tree_view.heading("10", text="Department")
tree_view.heading("11", text="Job Position")

# width and position for table
tree_view.column("1", minwidth=50, width=50, stretch=False, anchor=W)
tree_view.column("2", minwidth=120, width=120, stretch=False, anchor=W)
tree_view.column("3", minwidth=120, width=120, stretch=False, anchor=W)
tree_view.column("4", minwidth=50, width=50, stretch=False, anchor=CENTER)
tree_view.column("5", minwidth=100, width=100, stretch=False, anchor=CENTER)
tree_view.column("6", minwidth=225, width=225, stretch=False, anchor=W)
tree_view.column("7", minwidth=75, width=75, stretch=False, anchor=CENTER)
tree_view.column("8", minwidth=140, width=140, stretch=False, anchor=CENTER)
tree_view.column("9", minwidth=240, width=240, stretch=False, anchor=W)
tree_view.column("10", minwidth=125, width=125, stretch=False, anchor=CENTER)
tree_view.column("11", minwidth=125, width=125, stretch=False, anchor=CENTER)

tree_view["show"] = "headings"
tree_view.bind("<ButtonRelease-1>", get_data)
tree_view.pack(fill=X)

display_all()
root.mainloop()
