from tkinter import *
from tkinter.messagebox import *
import os
import webbrowser
import json
import pickle
from tkinter import filedialog
import smtplib
from PIL import Image, ImageTk



students = []

#-------- JSON - SAVE USERS --------#

teachers_path = "teachers.json"

teachers_data = {}

try:
    with open(teachers_path, "r") as f:
        teachers_data = json.load(f)
except FileNotFoundError:
    pass


students_path = "students.json"

students_data = {}

try:
    with open(students_path, "r") as f:
        students_data = json.load(f)
except FileNotFoundError:
    pass

#-------- CLASS AND FUNCTIONS --------#

def ClearEntries():
    register_name_entry.delete(0, END)
    register_surname_entry.delete(0, END)
    register_age_entry.delete(0, END)
    register_username_entry.delete(0, END)
    register_password_entry.delete(0, END)
    register_position_entry.delete(0, END)

    login_entry.delete(0, END)
    password_entry.delete(0, END)

    add_name_entry.delete(0, END)
    add_surname_entry.delete(0, END)
    add_group_entry.delete(0, END)

def RegisterFrame():
    login_frame.place_forget()
    register_frame.place(x=0, y=0)

def RegisterBack():
    register_frame.place_forget()
    login_frame.place(x=0, y=0)

def AboutUs():
    webbrowser.open_new_tab("http://raufalizada.ga/")

def Quizzes():
    webbrowser.open_new_tab("https://www.w3schools.com/python/python_quiz.asp")

def SendMail():
    webbrowser.open_new_tab("mailto:personalwork1124@gmail.com")

def GetInstagram():
    webbrowser.open_new_tab("https://www.instagram.com/ada.university/")

def GetFacebook():
    webbrowser.open_new_tab("https://www.facebook.com/ADAUniversity")

def GetYouTube():
    webbrowser.open_new_tab("https://www.youtube.com/channel/UCsFJ476U5LQxeq1ctM6smAQ")

def AddStudent():
    name = add_name_entry.get()
    surname = add_surname_entry.get()
    group = add_group_entry.get()

    if name == "" or surname == "" or group == "":
        showerror("ERROR", "Please fill in all fields!")
    else:
        dat = f"{name} {surname}, {group}"
        students_listbox.insert(END, dat)
        students.append(dat)
        ClearEntries()

def PassStudent():
    selection = students_listbox.curselection()

    if selection:
        selected_student = students_listbox.get(selection)
        students_passbox.insert(END, selected_student)

        if selected_student in students:
            students.remove(selected_student)


def FailStudent():
    selection = students_listbox.curselection()

    if selection:
        selected_student = students_listbox.get(selection)
        students_failbox.insert(END, selected_student)

        if selected_student in students:
            students.remove(selected_student)



def LogOut():
    showinfo("INFO", "USER SUCCESFULLY LOGGED OUT!")
    teacher_frame.place_forget()
    student_frame.place_forget()
    login_frame.place(x=0, y=0)

def DeleteStudent():
    global students
    selection = students_listbox.curselection()
    if selection:
        students_listbox.delete(selection)
        students_listbox.selection_clear(0, END)

        students.pop(selection[0] - 1)

    selection = students_passbox.curselection()
    if selection:
        students_passbox.delete(selection)
        students_passbox.selection_clear(0, END)

        students.append(students_passbox.get(selection[0]))

    selection = students_failbox.curselection()
    if selection:
        students_failbox.delete(selection)
        students_failbox.selection_clear(0, END)

        students.append(students_failbox.get(selection[0]))



class Person:
    def __init__(self, name, surname, age, username, password):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__username = username
        self.__password = password


class Teacher(Person):
    def __init__(self, name, surname, age, username, password, position):
        super().__init__(name, surname, age, username, password)
        self.__position = position


class Student(Person):
    def __init__(self, name, surname, age, username, password, position):
        super().__init__(name, surname, age, username, password)
        self.__position = position


def Submit():
    name = register_name_entry.get()
    surname = register_surname_entry.get()
    age = register_age_entry.get()
    username = register_username_entry.get()
    password = register_password_entry.get()
    position = register_position_entry.get()

    if name == "":
        showerror("WRONG REGISTERED", "YOU MUST ENTER YOUR NAME!")

    elif surname == "":
        showerror("WRONG REGISTERED", "YOU MUST ENTER YOUR SURNAME!")

    elif not age.isnumeric():
        showerror("ISNUMERIC ERROR", "PLEASE ENTER NUMBERS!")

    elif int(age) < 18:
        showwarning("YOU'RE UNDER 18!", "YOU CAN'T REGISTRATION!\nBECAUSE YOU ARE UNDER 18!")

    elif len(username) < 4:
        showwarning("USERNAME ERROR", "YOUR USERNAME IS LESS THAN 4!")

    elif len(password) < 6:
        showwarning("PASSWORD ERROR", "YOUR PASSWORD IS LESS THAN 6!")

    elif position == "":
        showerror("POSITION IS EMPTY!", "YOU MUST SELECT YOUR POSITION!")

    elif position == "teacher":
        teacher = Teacher(name, surname, age, username, password, position)
        teachers_data[username] = {
        "name": name,
        "surname": surname,
        "age": age,
        "password": password,
        "position": position
    }
        with open(teachers_path, "w") as f:
            json.dump(teachers_data, f)

        showinfo("Teacher Signed Up", "Successfully Signed Up!")
        register_frame.place_forget()
        login_frame.place(x=0, y=0)

        ClearEntries()

    elif position == "student":

        student = Student(name, surname, age, username, password, position)
        students_data[username] = {
            "name": name,
            "surname": surname,
            "age": age,
            "password": password,
            "position": position
        }

        with open(students_path, "w") as f:
            json.dump(students_data, f)

        showinfo("User Signed Up", "Successfully Signed Up!")
        register_frame.place_forget()
        login_frame.place(x=0, y=0)
        ClearEntries()

    else:
        showerror("ERROR", "ERROR")


def Login():
    username = login_entry.get()
    password = password_entry.get()
    ClearEntries()
    if username in teachers_data and teachers_data[username]["password"] == password:
        showinfo("TEACHER IS LOGGED", "Teacher is logged in!")
        print(f"Logged with this teacher: {username}")
        login_frame.place_forget()
        teacher_frame.place(x=0, y=0)

    elif username in students_data and students_data[username]["password"] == password:
        showinfo("STUDENT IS LOGGED", "Student is logged in!")
        print(f"Logged with this student: {username}")
        if students_data[username]["position"] == "student":
            login_frame.place_forget()
            student_frame.place(x=0, y=0)



    else:
        showerror(title="NO FOUNDED USER", message="This user isn't available!")


#---------- IMPORT TOOLS ----------#

root = Tk()
root.title("RUMECOS CABINET")
root.geometry("800x750")
root.resizable(False, False)
root.iconbitmap("logo.ico")

#---------- LOGIN PAGE ----------#

login_frame = Frame(root, bg="#003399", width=800, height=800)
login_frame.place(x=0, y=0)



login_welcome = Label(login_frame,text="WELCOME TO RUMECOS UNIVERSITY!", font=("Arial", 15, "bold"), width=30, background="#003399",fg="white")
login_welcome.place(x=240,y=10)

login_logo = Label(login_frame,text="USER",height=3,width=20, background="green",fg="white",font=("Arial", 15))
login_logo.place(x=300,y=70)

login_label = Label(login_frame, text="Login:", font=("Arial", 20, "bold"), bg="#003399", fg="white")
login_label.place(x=180, y=200)

password_label = Label(login_frame, text="Password:", font=("Arial", 20, "bold"), bg="#003399", fg="white")
password_label.place(x=125, y=260)

login_entry = Entry(login_frame, font=("Arial", 20, "italic"))
login_entry.place(x=300, y=200)

password_entry = Entry(login_frame, font=("Arial", 20, "italic"), show="*")
password_entry.place(x=300, y=260)

login_button = Button(login_frame, text="Login", background="green", foreground="white", activebackground="white", activeforeground="green", width=15, height=2, font=("Arial", 20), command=Login)
login_button.place(x=250, y=340)

register_note = Label(login_frame, text="Don't you have an account, register now!", font=("Arial", 20, "bold", "underline"), bg="#003399", fg="white")
register_note.place(x=120, y=440)

register_button = Button(login_frame, text="Register", background="green", foreground="white", activebackground="white", activeforeground="green", width=15, height=2, font=("Arial", 20), command=RegisterFrame)
register_button.place(x=250, y=510)

exit_button = Button(text="Exit", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 20), width=10, height=2, command= lambda : root.destroy())
exit_button.place(x=550, y=640)

AboutUs_button = Button(login_frame, text="About Us", background="green", foreground="white", activebackground="white", activeforeground="green", width=10, height=2, font=("Arial", 20), command=AboutUs)
AboutUs_button.place(x=30, y=640)

#-------- REGISTER PAGE --------#

register_frame = Frame(root, bg="#003399", width=800, height=800)

lblRegister = Label(register_frame,text="REGISTER",height=3,width=20, background="green",fg="white",font=("Arial", 15))
lblRegister.place(x=250,y=70)

register_name = Label(register_frame, text="Your Name:", font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_name.place(x=130, y=180)

register_surname = Label(register_frame, text="Your Surname:", font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_surname.place(x=78, y=225)

register_age = Label(register_frame, text="Your Age:", font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_age.place(x=158, y=270)

register_username = Label(register_frame, text="Your Username:", font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_username.place(x=62, y=315)

register_password = Label(register_frame, text="Password:", font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_password.place(x=148, y=360)

register_position = Label(register_frame, text="Position:",font=("Arial", 25, "bold"), bg="#003399", fg="white")
register_position.place(x=172.5, y=405)

register_name_entry = Entry(register_frame, font=("Arial", 15, "italic"))
register_name_entry.place(x=350, y=185)

register_surname_entry = Entry(register_frame, font=("Arial", 15, "italic"))
register_surname_entry.place(x=350, y=235)

register_age_entry = Entry(register_frame, font=("Arial", 15, "italic"))
register_age_entry.place(x=350, y=280)

register_username_entry = Entry(register_frame, font=("Arial", 15, "italic"))
register_username_entry.place(x=350, y=325)

register_password_entry = Entry(register_frame, show="*", font=("Arial", 15, "italic"))
register_password_entry.place(x=350, y=370)

register_position_entry = Entry(register_frame, font=("Arial", 15, "italic"))
register_position_entry.place(x=350, y=415)

register_submit = Button(register_frame, text="Submit", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 30), command=Submit)
register_submit.place(x=300, y=470)

back_button = Button(register_frame, text="Back", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 20), width=10, height=2, command=RegisterBack)
back_button.place(x=30, y=640)

exit_button = Button(text="Exit", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 20), width=10, height=2, command= lambda : root.destroy())
exit_button.place(x=550, y=640)

#-------- TEACHER PAGE --------#

teacher_frame = Frame(root, bg="#003399", width=800, height=800)

text_label = Label(teacher_frame, text="ADA University Teacher Cabinet", font=("Arial", 20, "bold"), bg="#003399", fg="white")
text_label.place(x=175, y=20)

add_name = Label(teacher_frame, text="Add Name:", font=("Arial", 15), bg="#003399", fg="white")
add_name.place(x=140, y=100)

add_surname = Label(teacher_frame, text="Add Surname:", font=("Arial", 15), bg="#003399", fg="white")
add_surname.place(x=112.5, y=140)

add_group = Label(teacher_frame, text="Add Group:", font=("Arial", 15), bg="#003399", fg="white")
add_group.place(x=135, y=180)

add_name_entry = Entry(teacher_frame, font=("Arial", 10, "italic"))
add_name_entry.place(x=260, y=105)

add_surname_entry = Entry(teacher_frame, font=("Arial", 10, "italic"))
add_surname_entry.place(x=260, y=145)

add_group_entry = Entry(teacher_frame, font=("Arial", 10, "italic"))
add_group_entry.place(x=260, y=185)

add_user_button = Button(teacher_frame, text="Add Student", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=AddStudent)
add_user_button.place(x=420, y=105)

delete_user_button = Button(teacher_frame, text="Delete Student", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=DeleteStudent)
delete_user_button.place(x=560, y=105)

pass_user_button = Button(teacher_frame, text="Pass Student", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=PassStudent)
pass_user_button.place(x=420, y=155)

fail_user_button = Button(teacher_frame, text="Fail Student", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=FailStudent)
fail_user_button.place(x=560, y=155)

#-------- STUDENT PAGE --------#

student_frame = Frame(root, bg="#003399", width=800, height=800)

img = Image.open("instagram.png")
img = img.resize((60, 60), resample=Image.LANCZOS)
photo_img = ImageTk.PhotoImage(img)

img2 = Image.open("facebook.png")
img2 = img2.resize((60, 60), resample=Image.LANCZOS)
photo_img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("youtube.png")
img3 = img3.resize((60, 60), resample=Image.LANCZOS)
photo_img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("ada.png")
img4 = img4.resize((480, 270), resample=Image.LANCZOS)
photo_img4 = ImageTk.PhotoImage(img4)

text_label = Label(student_frame, text="ADA University Student Cabinet", font=("Arial", 20, "bold"), bg="#003399", fg="white")
text_label.place(x=175, y=20)

quizzes_label = Label(student_frame, text="Quizzes", font=("Arial", 20, "bold"), bg="#003399", fg="white")
quizzes_label.place(x=320, y=75)

quizzes_button = Button(student_frame, text="Start", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=Quizzes)
quizzes_button.place(x=445, y=75)

sendmail_label = Label(student_frame, text="Send E-Mail to Manager", font=("Arial", 20, "bold"), bg="#003399", fg="white")
sendmail_label.place(x=120, y=120)

sendmail_button = Button(student_frame, text="Send", font=("Arial", 15), background="green", foreground="white", activebackground="white", activeforeground="green", command=SendMail)
sendmail_button.place(x=445, y=120)

instagram_button = Button(student_frame, image=photo_img, command=GetInstagram)
instagram_button.place(x=260, y=190)

facebook_button = Button(student_frame, image=photo_img2, command=GetFacebook)
facebook_button.place(x=340, y=190)

youtube_button = Button(student_frame, image=photo_img3, command=GetYouTube)
youtube_button.place(x=420, y=190)

ada_label = Label(student_frame, image=photo_img4)
ada_label.place(x=160, y=300)

#-------- LISTBOXS --------#

students_listbox_label = Label(teacher_frame, text="All Students", font=("Arial", 15), bg="#003399", fg="white")
students_listbox_label.place(x=90, y=240)

students_listbox = Listbox(teacher_frame, width=20, height=10, font=("Arial", 15))
students_listbox.place(x=30, y=280)

students_failbox_label = Label(teacher_frame, text="Failed Students", font=("Arial", 15), bg="#003399", fg="white")
students_failbox_label.place(x=320, y=240)

students_failbox = Listbox(teacher_frame, width=20, height=10, font=("Arial", 15))
students_failbox.place(x=280, y=280)

students_passbox_label = Label(teacher_frame, text="Passed Students", font=("Arial", 15), bg="#003399", fg="white")
students_passbox_label.place(x=560, y=240)

students_passbox = Listbox(teacher_frame, width=20, height=10, font=("Arial", 15))
students_passbox.place(x=530, y=280)

#-------- FOOTER --------#

exit_button = Button(teacher_frame, text="Exit", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 20), width=10, height=2, command= lambda : root.destroy())
exit_button.place(x=550, y=640)

AboutUs_button = Button(teacher_frame, text="About Us", background="green", foreground="white", activebackground="white", activeforeground="green", width=10, height=2, font=("Arial", 20), command=AboutUs)
AboutUs_button.place(x=30, y=640)

LogOut_button = Button(teacher_frame, text="Log Out", background="green", foreground="white", activebackground="white", activeforeground="green", width=10, height=2, font=("Arial", 20), command=LogOut)
LogOut_button.place(x=290, y=640)

exit_button = Button(student_frame, text="Exit", background="green", foreground="white", activebackground="white", activeforeground="green", font=("Arial", 20), width=10, height=2, command= lambda : root.destroy())
exit_button.place(x=550, y=640)

AboutUs_button = Button(student_frame, text="About Us", background="green", foreground="white", activebackground="white", activeforeground="green", width=10, height=2, font=("Arial", 20), command=AboutUs)
AboutUs_button.place(x=30, y=640)

LogOut_button = Button(student_frame, text="Log Out", background="green", foreground="white", activebackground="white", activeforeground="green", width=10, height=2, font=("Arial", 20), command=LogOut)
LogOut_button.place(x=290, y=640)

root.mainloop()