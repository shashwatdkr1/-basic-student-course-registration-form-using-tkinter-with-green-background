from tkinter import *
from tkinter import ttk
from turtle import color
root = Tk()
root.title("Student Course Registration Form")
root.geometry("400x400")
root.configure(background="green")
style = ttk.Style()
style.configure("style.TFrame", background="green",foreground = 
"green")
style.configure("TButton", background="red",foreground = "black")
frame = ttk.Frame(root, padding="3 3 12 12", style="style.TFrame")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
nameLabel = ttk.Label(frame, 
text="Name",background="green",foreground = "black")
nameLabel.grid(column=0, row=0, sticky=W)
name = ttk.Entry(frame)
name.grid(column=1, row=0, sticky=(W, E))
courseLabel = ttk.Label(frame, 
text="Course",background="green",foreground = "black")
courseLabel.grid(column=0, row=1, sticky=W)
course = ttk.Entry(frame)
course.grid(column=1, row=1, sticky=(W, E))
semesterLabel = ttk.Label(frame, 
text="Semester",background="green",foreground = "black")
semesterLabel.grid(column=0, row=2, sticky=W)
semester = ttk.Entry(frame)
semester.grid(column=1, row=2, sticky=(W, E))
semester.insert(0,"1")
formNumberLabel = ttk.Label(frame, text="Form 
Number",background="green",foreground = "black")
formNumberLabel.grid(column=0, row=3, sticky=W)
formNumber = ttk.Entry(frame)
formNumber.grid(column=1, row=3, sticky=(W, E))
formNumber.insert(0,"123")
contactNoLabel = ttk.Label(frame, text="Contact 
No",background="green",foreground = "black")
contactNoLabel.grid(column=0, row=4, sticky=W)
contactNo = ttk.Entry(frame)
contactNo.grid(column=1, row=4, sticky=(W, E))
contactNo.insert(0,"1234567890")
emailLabel = ttk.Label(frame, 
text="Email",background="green",foreground = "black")
emailLabel.grid(column=0, row=5, sticky=W)
email = ttk.Entry(frame)
email.grid(column=1, row=5, sticky=(W, E))
addressLabel = ttk.Label(frame, 
text="Address",background="green",foreground = "black")
addressLabel.grid(column=0, row=6, sticky=W)
address = ttk.Entry(frame)
address.grid(column=1, row=6, sticky=(W, E))
submitButton = ttk.Button(frame, text="Submit")
submitButton.grid(column=1, row=7, sticky=(W, E))
root.mainloop()